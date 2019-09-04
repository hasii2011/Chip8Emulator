
from typing import List
from typing import Dict
from typing import Callable
from typing import cast

from logging import Logger
from logging import getLogger

from random import randint
from random import seed

from pkg_resources import resource_filename

from org.hasii.chip8.Chip8Stack import Chip8Stack
from org.hasii.chip8.keyboard.Chip8KeyPad import Chip8KeyPad
from org.hasii.chip8.keyboard.Chip8KeyPadKeys import Chip8KeyPadKeys
from org.hasii.chip8.Chip8Mnemonics import Chip8Mnemonics
from org.hasii.chip8.Chip8Registers import Chip8Registers
from org.hasii.chip8.Chip8RegisterName import Chip8RegisterName
from org.hasii.chip8.Chip8SpriteType import Chip8SpriteType
from org.hasii.chip8.keyboard.Chip8KeyPressData import Chip8KeyPressData
from org.hasii.chip8.Chip8Decoder import Chip8Decoder

from org.hasii.chip8.errors.UnknownInstructionError import UnknownInstructionError
from org.hasii.chip8.errors.InvalidIndexRegisterValue import InvalidIndexRegisterValue
from org.hasii.chip8.errors.UnKnownSpecialRegistersSubOpCode import UnKnownSpecialRegistersSubOpCode
from org.hasii.chip8.errors.UnknownKeyPressedOpSubOpCode import UnknownKeyPressedOpSubOpCode


class Chip8(Chip8Decoder):

    debugVirtualScreen: bool = False
    debugPrintMemory:   bool = False

    MEMORY_SIZE: int = 4096             # in bytes
    ROM_PKG:     str = "org.hasii.chip8.roms"
    #
    # from http://www.multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter/
    #
    SPRITE_START_ADDRESS:  int = 0x50
    PROGRAM_START_ADDRESS: int = 0x200
    INSTRUCTION_SIZE:      int = 2       # in bytes

    OPCODE_MASK             = 0xF000
    ENHANCED_OP_CODE_MASK   = 0xF0FF
    SKIP_OP_CODE_MASK       = 0xF0FF
    RET_OR_CLS_OP_CODE_MASK = 0x00FF
    ADDRESS_MASK            = 0x0FFF

    SPECIAL_REGISTERS_BASE_OP_CODE: int = 0xF000
    SKIP_BASED_ON_KEYBOARD_OP_CODE: int = 0xE000
    RET_OR_CLS_OP_CODE:             int = 0x0000

    IDX_REG_MASK:    int = 0x0FFF
    LOC_JMP_MASK:    int = 0x0FFF
    MAX_IDX_REG_VAL: int = 0x0FFF

    CPU_CYCLE: int = 1000 // 60

    VIRTUAL_WIDTH:  int = 64
    VIRTUAL_HEIGHT: int = 32

    BIT0_MASK: int = 0x80
    BIT1_MASK: int = 0x40
    BIT2_MASK: int = 0x20
    BIT3_MASK: int = 0x10
    BIT4_MASK: int = 0x08
    BIT5_MASK: int = 0x04
    BIT6_MASK: int = 0x02
    BIT7_MASK: int = 0x01

    BIT_MASKS: List[int] = [BIT0_MASK, BIT1_MASK, BIT2_MASK, BIT3_MASK, BIT4_MASK, BIT5_MASK, BIT6_MASK, BIT7_MASK]

    VIRTUAL_SCREEN_ROW = List[int]
    virtualScreen: List[VIRTUAL_SCREEN_ROW] = []

    NUM_SPRITES:      int = 16
    BYTES_PER_SPRITE: int = 5

    CHIP8_SPRITE = List[int]
    SPRITE_0: CHIP8_SPRITE = [0xF0, 0x90, 0x90, 0x90, 0xF0]   # 0
    SPRITE_1: CHIP8_SPRITE = [0x20, 0x60, 0x20, 0x20, 0x70]   # 1
    SPRITE_2: CHIP8_SPRITE = [0xF0, 0x10, 0xF0, 0x80, 0xF0]   # 2
    SPRITE_3: CHIP8_SPRITE = [0xF0, 0x10, 0xF0, 0x10, 0xF0]   # 3
    SPRITE_4: CHIP8_SPRITE = [0x90, 0x90, 0xF0, 0x10, 0x10]   # 4
    SPRITE_5: CHIP8_SPRITE = [0xF0, 0x80, 0xF0, 0x10, 0xF0]   # 5
    SPRITE_6: CHIP8_SPRITE = [0xF0, 0x80, 0xF0, 0x90, 0xF0]   # 6
    SPRITE_7: CHIP8_SPRITE = [0xF0, 0x10, 0x20, 0x40, 0x50]   # 7
    SPRITE_8: CHIP8_SPRITE = [0xF0, 0x90, 0xF0, 0x90, 0xF0]   # 8
    SPRITE_9: CHIP8_SPRITE = [0xF0, 0x90, 0xF0, 0x10, 0xF0]   # 9
    SPRITE_A: CHIP8_SPRITE = [0xF0, 0x90, 0xF0, 0x90, 0x90]   # A
    SPRITE_B: CHIP8_SPRITE = [0xE0, 0x90, 0xE0, 0x90, 0xE0]   # B
    SPRITE_C: CHIP8_SPRITE = [0xF0, 0x80, 0x80, 0x80, 0xF0]   # C
    SPRITE_D: CHIP8_SPRITE = [0xE0, 0x90, 0x90, 0x90, 0xE0]   # D
    SPRITE_E: CHIP8_SPRITE = [0xF0, 0x80, 0xF0, 0x80, 0xF0]   # E
    SPRITE_F: CHIP8_SPRITE = [0xF0, 0x80, 0xF0, 0x80, 0x80]   # F

    SPRITES: Dict[Chip8SpriteType, CHIP8_SPRITE] = {
        Chip8SpriteType.SPRITE_0: SPRITE_0,
        Chip8SpriteType.SPRITE_1: SPRITE_1,
        Chip8SpriteType.SPRITE_2: SPRITE_2,
        Chip8SpriteType.SPRITE_3: SPRITE_3,
        Chip8SpriteType.SPRITE_4: SPRITE_4,
        Chip8SpriteType.SPRITE_5: SPRITE_5,
        Chip8SpriteType.SPRITE_6: SPRITE_6,
        Chip8SpriteType.SPRITE_7: SPRITE_7,
        Chip8SpriteType.SPRITE_8: SPRITE_8,
        Chip8SpriteType.SPRITE_9: SPRITE_9,
        Chip8SpriteType.SPRITE_A: SPRITE_A,
        Chip8SpriteType.SPRITE_B: SPRITE_B,
        Chip8SpriteType.SPRITE_C: SPRITE_C,
        Chip8SpriteType.SPRITE_D: SPRITE_D,
        Chip8SpriteType.SPRITE_E: SPRITE_E,
        Chip8SpriteType.SPRITE_F: SPRITE_F,
    }

    def __init__(self):

        super().__init__()
        self.logger: Logger = getLogger(__name__)

        self.pc:            int = Chip8.PROGRAM_START_ADDRESS
        self.instruction:   int = 0x0000

        self.memory:     List[int]      = [0] * Chip8.MEMORY_SIZE
        self.stack:      Chip8Stack     = Chip8Stack()
        self.registers:  Chip8Registers = Chip8Registers()
        self.keypad:     Chip8KeyPad    = Chip8KeyPad()

        self.keyPressData: Chip8KeyPressData = Chip8KeyPressData()

        self._indexRegister: int = 0
        self._delayTimer:    int = 0
        self._soundTimer:    int = 0

        seed()
        self.opCodeMethods: Dict[int, Callable] = {

            Chip8Mnemonics.RTS.value:  self.returnFromSubroutine,
            Chip8Mnemonics.CLS.value:  self.clearScreen,
            Chip8Mnemonics.JUMP.value: self.jumpToAddress,
            Chip8Mnemonics.CALL.value: self.callSubroutine,
            Chip8Mnemonics.SEL.value:  self.skipIfRegisterEqualToLiteral,
            Chip8Mnemonics.SNEL.value: self.skipIfRegisterNotEqualToLiteral,
            Chip8Mnemonics.SER.value:  self.skipIfRegisterEqualToRegister,
            Chip8Mnemonics.LDL.value:  self.loadRegisterWithLiteral,
            Chip8Mnemonics.ADD.value:  self.addLiteralToRegister,
            Chip8Mnemonics.MOV.value:  self.registerToRegisterInstructions,
            Chip8Mnemonics.OR.value:   self.registerToRegisterInstructions,
            Chip8Mnemonics.AND.value:  self.registerToRegisterInstructions,
            Chip8Mnemonics.XOR.value:  self.registerToRegisterInstructions,
            Chip8Mnemonics.ADDR.value: self.registerToRegisterInstructions,
            Chip8Mnemonics.SUB.value:  self.registerToRegisterInstructions,
            Chip8Mnemonics.SHR.value:  self.registerToRegisterInstructions,
            Chip8Mnemonics.SUBN.value: self.registerToRegisterInstructions,
            Chip8Mnemonics.SHL.value:  self.registerToRegisterInstructions,
            Chip8Mnemonics.SNER.value: self.skipIfRegisterNotEqualToRegister,
            Chip8Mnemonics.LDI.value:  self.loadIndexRegister,
            Chip8Mnemonics.JPV.value:  self.jumpToLocationPlusVZero,
            Chip8Mnemonics.RNDMSK.value:  self.rndMask,
            Chip8Mnemonics.DRAW.value:  self.displaySprite,
            Chip8Mnemonics.SKP.value:  self.skipNextKeyPressedInstructions,
            Chip8Mnemonics.SKNP.value: self.skipNextKeyPressedInstructions,
            Chip8Mnemonics.LDDT.value: self.specialRegistersInstructions,
            Chip8Mnemonics.WAITKEY.value:  self.specialRegistersInstructions,
            Chip8Mnemonics.SDT.value:  self.specialRegistersInstructions,
            Chip8Mnemonics.SST.value:  self.specialRegistersInstructions,
            Chip8Mnemonics.ADDI.value: self.specialRegistersInstructions,
            Chip8Mnemonics.LDIS.value: self.specialRegistersInstructions,
            Chip8Mnemonics.MOVBCD.value:  self.specialRegistersInstructions,
            Chip8Mnemonics.MOVM.value:  self.specialRegistersInstructions,
            Chip8Mnemonics.READM.value:  self.specialRegistersInstructions,
        }
        self.logger.debug(f"{self.memory}")

        for row in range(0, self.VIRTUAL_HEIGHT):
            columns: List[int] = []
            for col in range(0, self.VIRTUAL_WIDTH):
                columns. append(0)
            self.virtualScreen.append(columns)

        self._loadAllSpritesInMemory()
        self.romLoaded:        bool = False

        self.instructionCount: int  = 0

    def resetCPU(self):
        """
        Reset the emulator to its initial state.  Note some of this code is duplicated from the class
        constructor.  PEP-8 requires that you define instance variables in the constructor
        """
        self.pc            = Chip8.PROGRAM_START_ADDRESS
        self.instruction   = 0x0000
        self.delayTimer    = 0x0
        self.soundTimer    = 0x0
        self.indexRegister = 0x0
        self.instructionCount = 0
        self.keyPressData.waitingForKey = False
        self.keyPressData.storeRegister = cast(Chip8RegisterName, None)
        self.keyPressData.pressedKey    = cast(Chip8KeyPadKeys, None)

        self._clearMemory()
        self._clearVirtualScreen()
        self._loadAllSpritesInMemory()
        self.stack.empty()
        self.registers.initialize()
        self.keypad.initialize()

    def getDelayTimer(self) -> int:
        return self._delayTimer

    def setDelayTimer(self, theNewValue: int):
        if theNewValue > -1:
            self._delayTimer = theNewValue

    def decrementDelayTimer(self):
        if self._delayTimer > 0:
            self._delayTimer -= 1

    def getSoundTimer(self) -> int:
        return self._soundTimer

    def setSoundTimer(self, theNewValue: int):
        if theNewValue > -1:
            self._soundTimer = theNewValue

    def decrementSoundTimer(self):
        if self._soundTimer > 0:
            self._soundTimer -= 1

    def getIndexRegister(self) -> int:
        return self._indexRegister

    def setIndexRegister(self, theNewValue: int):

        if theNewValue < 0 or theNewValue > Chip8.MAX_IDX_REG_VAL:
            raise InvalidIndexRegisterValue(theNewValue)

        self._indexRegister = theNewValue

    delayTimer    = property(getDelayTimer, setDelayTimer)
    soundTimer    = property(getSoundTimer, setSoundTimer)
    indexRegister = property(getIndexRegister, setIndexRegister)

    def emulateSingleCpuCycle(self, instruction: int = None):
        """

        Args:
            instruction: Set to real instruction in
            order to allow testing

        """

        if instruction is None:
            self.fetchInstruction()
        else:
            self.instruction = instruction
        self.pc += Chip8.INSTRUCTION_SIZE

        instStr: str = hex(self.instruction)
        self.logger.debug(f"currentInstruction: {instStr}")

        op: int = self.instruction & Chip8.OPCODE_MASK

        if op == Chip8.SPECIAL_REGISTERS_BASE_OP_CODE:
            op = self.instruction & Chip8.ENHANCED_OP_CODE_MASK
        elif op == Chip8.SKIP_BASED_ON_KEYBOARD_OP_CODE:
            op = self.instruction & Chip8.SKIP_OP_CODE_MASK
        elif op == Chip8.RET_OR_CLS_OP_CODE:
            op = self.instruction & Chip8.RET_OR_CLS_OP_CODE_MASK

        opStr: str = hex(op)
        self.logger.debug(f"opStr: {opStr}")
        try:
            instruction: Callable = self.opCodeMethods[op]
        except KeyError:
            raise UnknownInstructionError(badInstruction=op)

        instruction()
        self.instructionCount += 1

    def fetchInstruction(self):
        self.instruction = self.memory[self.pc] << 8 | self.memory[self.pc + 1]
        self.logger.debug(f"pc: {hex(self.pc)} instruction: {hex(self.instruction)}")

    def jumpToAddress(self):
        addr = self.instruction & Chip8.ADDRESS_MASK
        self.pc = addr
        self.logger.debug(f"new pc: {hex(self.pc)}")

    def callSubroutine(self):
        """
        2nnn - CALL addr
        Call subroutine at nnn.

        The interpreter increments the stack pointer, then puts the current PC on the top of the stack. The PC is then set to nnn.
        """
        self.stack.push(self.pc)
        subroutineAddr: int = self.instruction & Chip8.ADDRESS_MASK
        self.pc = subroutineAddr

    def returnFromSubroutine(self):
        """
            RTS = 0x00EE    # 00EE;
            Return from a subroutine; Set PC to the address at top of the stack, then subtracts 1 from the stack pointer.
        """
        self.pc = self.stack.pop()

    def clearScreen(self):
        self._clearVirtualScreen()

    def skipIfRegisterEqualToLiteral(self):
        """
        3xkk; SEL Vx, kk; Skip next instruction if Vx = kk;  Skip based on literal
        """
        register: Chip8RegisterName = self._decodeRegister()

        lit:    int = self._decodeLiteral()
        regVal: int = self.registers.getValue(v=register)

        if regVal == lit:
            self.pc += Chip8.INSTRUCTION_SIZE

    def skipIfRegisterNotEqualToLiteral(self):
        """
        4xkk; SNEL Vx, kk;    Skip next instruction if Vx != kk   Skip based on literal
        """
        register: Chip8RegisterName = self._decodeRegister()

        lit:    int = self._decodeLiteral()
        regVal: int = self.registers.getValue(v=register)

        if regVal != lit:
            self.pc += Chip8.INSTRUCTION_SIZE

    def skipIfRegisterEqualToRegister(self):
        """
        5xy0; SER Vx, Vy;     Skip next instruction if Vx = Vy    Skip based on register compares

        """
        leftRegister:  Chip8RegisterName = self._decodeLeftRegister()
        rightRegister: Chip8RegisterName = self._decodeRightRegister()
        self.logger.info(f"leftRegister: V{leftRegister.value:X}  rightRegister: V{rightRegister.value:X}")

        leftRegVal:  int = self.registers.getValue(leftRegister)
        rightRegVal: int = self.registers.getValue(rightRegister)
        if leftRegVal == rightRegVal:
            self.pc += Chip8.INSTRUCTION_SIZE

    def skipIfRegisterNotEqualToRegister(self):
        """
        SNER Vx, Vy;    Skip next instruction if Vx != Vy
        """
        leftRegister:  Chip8RegisterName = self._decodeLeftRegister()
        rightRegister: Chip8RegisterName = self._decodeRightRegister()

        leftRegVal:  int = self.registers.getValue(leftRegister)
        rightRegVal: int = self.registers.getValue(rightRegister)

        if leftRegVal != rightRegVal:
            self.pc += Chip8.INSTRUCTION_SIZE

    def loadRegisterWithLiteral(self):
        """
        6xkk; LDL Vx, kk;     Set Vx = kk     Load literal
        """
        register: Chip8RegisterName = self._decodeRegister()
        lit:      int               = self._decodeLiteral()

        self.registers.setValue(v=register, newValue=lit)

    def addLiteralToRegister(self):
        """
        7xkk; ADD Vx, kk;     Adds the value kk to the value of register Vx, then stores the result in Vx
        (Carry flag is not changed)
        """
        register: Chip8RegisterName = self._decodeRegister()
        lit:      int               = self._decodeLiteral()
        self.registers.addToRegister(vx=register, val=lit)

    def registerToRegisterInstructions(self):
        """
        Handles 0x8000 through 0x8007 and 0x800E
        """

        subOpCode: int = self._decodeRegisterToRegisterOpCode()
        self.logger.debug(f"Reg to Reg subOpCode: {subOpCode:X}")

        leftRegister:  Chip8RegisterName = self._decodeLeftRegister()
        rightRegister: Chip8RegisterName = self._decodeRightRegister()

        rightRegVal: int = self.registers.getValue(rightRegister)

        if subOpCode == 0x0:    # 8xy0; MOV Vx, Vy;     Set Vx = Vy.
            self.registers.setValue(v=leftRegister, newValue=rightRegVal)
        elif subOpCode == 0x1:  # 8xy1; OR Vx, Vy;      Set Vx = Vx OR Vy
            self.registers.orOp(v=leftRegister, mask=rightRegVal)
        elif subOpCode == 0x2:  # 8xy2; AND Vx, Vy;     Set Vx = Vx AND Vy
            self.registers.andOp(v=leftRegister, mask=rightRegVal)
        elif subOpCode == 0x3:   # 8xy3; XOR Vx, Vy;     Set Vx = Vx XOR Vy
            self.registers.xorOp(v=leftRegister, mask=rightRegVal)
        elif subOpCode == 0x4:   # 8xy4; ADDR Vx, Vy;     Set Vx = Vx + Vy
            self.registers.addRegisterToRegister(leftRegister, rightRegister)
        elif subOpCode == 0x5:   # 8xy5; SUB Vx, Vy;     Set Vx = Vx - Vy
            self.registers.subRegisterToRegister(leftRegister, rightRegister)
        elif subOpCode == 0x6:   # 8xy6; SHR Vx, Vy;     Set Vx = Vx SHR 1
            self.registers.shiftRight(v=leftRegister, numBitsToShift=1)
        elif subOpCode == 0x7:   # SUBN Vx, Vy;    Set Vx = Vy - Vx
            self.registers.subRegisterVyFromRegisterVx(vx=leftRegister, vy=rightRegister)
        elif subOpCode == 0xE:   # 8xyE; SHL Vx, Vy;     Set Vx = Vx SHL 1
            self.registers.shiftLeft(v=leftRegister, numBitsToShift=1)

    def loadIndexRegister(self):
        """
        # Annn; LDI I, addr;    Set I = nnn; The value of register I is set to nnn
        """
        valToLoad: int = self.instruction & Chip8.IDX_REG_MASK

        self.indexRegister = valToLoad

    def jumpToLocationPlusVZero(self):
        """
        Bnnn; JUMP V0, addr;    Jump to location nnn + V0
        The program counter is set to nnn plus the value of V0
        """
        v0Val:    int = self.registers.getValue(Chip8RegisterName.V0)
        instrVal: int = self.instruction & 0x0FFF

        self.pc = instrVal + v0Val

    def rndMask(self):
        """
        Cxkk; RNDMSK Vx, byte;   Set Vx = random byte AND kk

        Interpreter generates a random number from 0 to 255

        """
        targetRegister: Chip8RegisterName = self._decodeLeftRegister()
        lit:        int = self._decodeLiteral()
        randByte:   int = self.generateRandomByte()
        self.logger.debug(f"randByte: {randByte:X}")

        tempReg: int = randByte & lit
        self.registers.setValue(v=targetRegister, newValue=tempReg)

    def displaySprite(self):
        """
        Dxyn; DRAW Vx, Vy, nibble;

        Display n-byte sprite starting at memory location I at (Vx, Vy), set VF = collision

        """
        vxRegName: Chip8RegisterName = self._decodeLeftRegister()
        vyRegName: Chip8RegisterName = self._decodeRightRegister()

        vxValue: int = self.registers.getValue(vxRegName)
        vyValue: int = self.registers.getValue(vyRegName)
        nibble:  int = self._decodeNibble()
        self.drawOnVirtualScreen(xCoord=vxValue, yCoord=vyValue, nBytes=nibble)

    def skipNextKeyPressedInstructions(self):

        subOpCode: int = self._decodeSkipKeyboardRegisterSubOpCode()
        vxRegName: Chip8RegisterName = self._decodeLeftRegister()
        vxValue:   int = self.registers.getValue(vxRegName)
        keyPadKey: Chip8KeyPadKeys = Chip8KeyPadKeys(vxValue)

        if subOpCode == 0x9E:
            self.skipNextVxDependingOnKeyPressed(keyPadKey)
        elif subOpCode == 0xA1:
            self.skipNextVxDependingOnKeyNotPressed(keyPadKey)
        else:
            raise UnknownKeyPressedOpSubOpCode(invalidSubOpCode=subOpCode)

    def skipNextVxDependingOnKeyPressed(self, keyPadKey: Chip8KeyPadKeys):
        """
        Ex9E; SKP Vx;

        Skip next instruction if key with the value of Vx is pressed
        """
        if self.keypad.isKeyPressed(keyPadKey) is True:
            self.pc += Chip8.INSTRUCTION_SIZE

    def skipNextVxDependingOnKeyNotPressed(self, keyPadKey: Chip8KeyPadKeys):
        """
        ExA1; SKNP Vx;
        Skip next instruction if key with the value of Vx is not pressed
        """
        if self.keypad.isKeyPressed(keyPadKey) is False:
            self.pc += Chip8.INSTRUCTION_SIZE

    def specialRegistersInstructions(self):
        """
        LDDT = 0xF007   # Fx07; LDT Vx, DT;     Set Vx = delay timer value
        WAITKEY  = 0xF00A   # Fx0A; WAITKEY Vx, K;      Wait for a key press, store the value of the key in Vx.
        SDT  = 0xF015   # Fx15; SDT DT, Vx;     Set delay timer = Vx
        SST  = 0xF018   # Fx18; SST ST, Vx;     Set sound timer = Vx
        ADDI = 0xF01E   # Fx1E; ADDI I, Vx;     Set I = I + Vx
        LDIS = 0xF029   # Fx29; LDIS F, Vx;     I equals location of sprite for the character in Vx; chars 0-F represented by a 4x5 font
        MOVBCD  = 0xF033   # Fx33; MOVBCD B, Vx;      Store BCD representation of Vx in memory locations I, I+1, and I+2
        MOVM  = 0xF055   # Fx55; MOVM [I], Vx;    Store registers V0-Vx in memory starting at location I.
        READM  = 0xF065   # Fx65; READM Vx, [I];    Read registers V0-Vx from memory starting at location I.
        """
        subOpCode: int = self._decodeSpecialRegistersSubOpCode()
        self.logger.debug(f"Special Registers subOpCode: {subOpCode:X}")

        regName: Chip8RegisterName = self._decodeLeftRegister()

        if subOpCode == 0x07:
            self.registers.setValue(v=regName, newValue=self.delayTimer)
        elif subOpCode == 0x0A:
            self.logger.info(f"Wait for key press; store value in {regName}")
            self.setupChipToWaitForKeyPress(regName=regName)
        elif subOpCode == 0x15:
            self.delayTimer = self.registers.getValue(regName)
        elif subOpCode == 0x18:
            self.soundTimer = self.registers.getValue(regName)
        elif subOpCode == 0x1E:
            self.indexRegister += self.registers.getValue(regName)
        elif subOpCode == 0x29:
            spriteDigit: int = self.registers.getValue(v=regName)
            memAddress:  int = Chip8.SPRITE_START_ADDRESS + (spriteDigit * Chip8.BYTES_PER_SPRITE)
            self.logger.info(f"Sprite: 0x{spriteDigit} is at address: 0x{memAddress}")
            self.indexRegister = memAddress
        elif subOpCode == 0x33:
            regVal:  int  = self.registers.getValue(regName)
            memLoc:  int = self.indexRegister

            self.memory[memLoc]     = regVal // 100
            self.memory[memLoc + 1] = (regVal // 10) % 10
            self.memory[memLoc + 2] = (regVal % 100) % 10
            self.logger.info(f"memLoc: '{self.memory[memLoc]}' memLoc+1: '{self.memory[memLoc+1]}' memLoc+2: '{self.memory[memLoc+2]}'")
        elif subOpCode == 0x55:
            lastRegValue: int               = cast(int, regName.value)
            for x in range(0, lastRegValue + 1):
                currRegName = Chip8RegisterName(x)
                self.memory[self.indexRegister + x] = self.registers.getValue(currRegName)
                self.logger.debug(f'currRegName: {currRegName} value: {self.registers[currRegName]:04X}')
        elif subOpCode == 0x65:
            lastRegValue: int = cast(int, regName.value)
            self._debugPrintMemory(startByteNbr=self.indexRegister, nBytes=lastRegValue, bytesPerRow=8)

            for x in range(0, lastRegValue + 1):
                currentRegName = Chip8RegisterName(x)
                self.logger.debug(f"regName: {currentRegName} memory value: {self.memory[self.indexRegister + x]}")
                self.registers.setValue(currentRegName, self.memory[self.indexRegister + x])
                self.logger.debug(f"Register dump: {self.registers}")
        else:
            raise UnKnownSpecialRegistersSubOpCode(invalidSubOpCode=subOpCode)

    def loadROM(self, theFilename: str):

        self.logger.info(f"loading ROM: {theFilename}")
        fullFileName: str = self._findTheROM(theFilename)

        fd = open(fullFileName, 'rb')
        rom: bytes = fd.read()
        fd.close()

        for byte in range(len(rom)):
            self.memory[self.pc + byte] = rom[byte]

        self.romLoaded = True
        self.logger.debug(f"{self.memory}")
        self._debugPrintMemory(startByteNbr=0, nBytes=len(self.memory))

    def isCPUWaitingForKeyPress(self) -> bool:
        return self.keyPressData.waitingForKey

    def setupChipToWaitForKeyPress(self, regName: Chip8RegisterName):
        """
        Called by the CPU instruction (Fx0A; WAITKEY Vx, K) to set the CPU into wait mode
        Args:
            regName:  The register into which to store the key that was pressed
        """
        self.keyPressData.waitingForKey = True
        self.keyPressData.storeRegister = regName

    def setKeyPressed(self, pressedKey: Chip8KeyPadKeys):
        """
        The external keyboard handler should only call this method when it detects a keypress event
        and `keyPressData.waitingForKey` is set to True

        Called by the external keyboard handler when it detects a keypres
        Args:
            pressedKey:  The keyname that was pressed
        """
        self.keyPressData.waitingForKey = False
        self.keyPressData.pressedKey    = pressedKey
        self.registers.setValue(v=self.keyPressData.storeRegister, newValue=pressedKey.value)
        self.logger.info(f'Key pressed: {self.keyPressData}')

    def drawOnVirtualScreen(self, xCoord: int, yCoord: int, nBytes: int):
        """

        Args:
            xCoord: x-coordinate on virtual screen
            yCoord: y-coordinate on virtual screen
            nBytes: The number of bytes to copy from where the `indexRegister` points
        """
        self.registers.setValue(Chip8RegisterName.VF, Chip8Registers.NO_SPRITE_COLLISION_BIT)

        self.logger.debug(f'Draw ({xCoord},{yCoord}) {self.registers}')
        startAddress: int = self.indexRegister

        drawY: int = yCoord
        for byteNum in range(nBytes):
            if drawY > (Chip8.VIRTUAL_HEIGHT - 1):
                drawY = 0
            currentVirtualScreenRow: Chip8.VIRTUAL_SCREEN_ROW = self.virtualScreen[drawY]

            drawX: int = xCoord
            for bitNum in range(8):
                spriteByte:       int = self.memory[startAddress + byteNum]
                maskedSpriteBit:  int = spriteByte & Chip8.BIT_MASKS[bitNum]
                spriteBit = maskedSpriteBit >> (7 - bitNum)
                self.logger.debug(f"spriteByte: {bin(spriteByte)} spriteBit: {spriteBit:X}")
                #
                # Wrap on x if necessary
                #
                if drawX  > (Chip8.VIRTUAL_WIDTH - 1):
                    drawX = 0
                #
                # TODO: This should be an XOR and set of VF register if there was a collision
                #
                if currentVirtualScreenRow[drawX] == 1 and spriteBit == 1:
                    self.registers.setValue(v=Chip8RegisterName.VF, newValue=Chip8Registers.SPRITE_COLLISION_BIT)
                currentVirtualScreenRow[drawX] ^= spriteBit
                drawX += 1
            drawY += 1

        self._dumpVirtualScreen()

    def _findTheROM(self, theFileName: str):

        fileName = resource_filename(Chip8.ROM_PKG, theFileName)

        self.logger.debug(f"The full file name: {fileName}")
        return fileName

    def _decodeSkipKeyboardRegisterSubOpCode(self) -> int:
        """
        Same mask but want code to self-document
        """
        return self._decodeSpecialRegistersSubOpCode()

    def _decodeSpecialRegistersSubOpCode(self) -> int:
        return self.instruction & 0x00FF

    def _loadAllSpritesInMemory(self):
        startAddress: int = Chip8.SPRITE_START_ADDRESS
        spriteLen: int = len(Chip8.SPRITE_0)

        loadAddress: int = startAddress
        for spriteType in Chip8.SPRITES:
            sprite: List[int] = Chip8.SPRITES[spriteType]
            self._loadSprite(sprite, loadAddress)
            loadAddress += spriteLen

    def _loadSprite(self, theSprite: List[int], startMemoryAddress: int):

        memAddress: int = startMemoryAddress
        for sprite in theSprite:
            self.memory[memAddress] = sprite
            memAddress += 1

    def _clearMemory(self):
        """
        Clear everything from the start of program memory to the end;  Don't stomp
        on the sprite space
        """
        for x in range(Chip8.PROGRAM_START_ADDRESS, Chip8.MEMORY_SIZE):
            self.memory[x] = 0

    def _clearVirtualScreen(self):

        for yCoord in range(0, self.VIRTUAL_HEIGHT):
            currentVirtualScreenRow: Chip8.VIRTUAL_SCREEN_ROW = self.virtualScreen[yCoord]
            for xCoord in range(0, self.VIRTUAL_WIDTH):
                currentVirtualScreenRow[xCoord] = 0

    def _debugPrintMemory(self, startByteNbr: int, nBytes: int, bytesPerRow: int = 32):
        """
        I know this is not Pythonic;  But for x in range(startByteNbr, nBytes, bytesPerRow):
        does not work

        Args:
            startByteNbr:
            nBytes:
            bytesPerRow:

        Returns:

        """
        # for x in range(startByteNbr, nBytes, bytesPerRow):
        #     endByteIndex: int = x + bytesPerRow
        #     subMemory = self.memory[x:endByteIndex]
        #     subMemoryBytes: bytes = bytes(subMemory)
        #     subStr:         str   = subMemoryBytes.hex()
        #
        #     self.logger.info(f"{hex(x):6} {hex(endByteIndex-2):6}  {subStr}")

        if self.debugPrintMemory is True:
            z: int = startByteNbr
            while z < (startByteNbr + nBytes):

                endByteIndex: int = z + bytesPerRow
                subMemory = self.memory[z:endByteIndex]
                subMemoryBytes: bytes = bytes(subMemory)
                subStr:         str   = subMemoryBytes.hex()

                self.logger.info(f"{z:04X}-{endByteIndex-2:04X}  {subStr.upper()}")

                z += bytesPerRow

    def _dumpVirtualScreen(self,
                           startRow: int = 0, nRows: int = VIRTUAL_HEIGHT, startCol: int = 0, nCols: int = VIRTUAL_WIDTH):

        if self.debugVirtualScreen is True:
            self.logger.info("DUMPING VIRTUAL SCREEN")
            self.logger.info("                             1                   2                   3                   4                   5                   6")
            self.logger.info("         0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3")
            for rowNum in range(startRow, nRows):
                bitRow: str = f'Row: {rowNum:2} |'
                virtualScreenRow: Chip8.VIRTUAL_SCREEN_ROW = self.virtualScreen[rowNum]
                for colNum in range(startCol, nCols):
                    bitRow = bitRow + f"{virtualScreenRow[colNum]:1}|"
                self.logger.info(f"{bitRow}")

    def __repr__(self):
        cpuDump: str = (
            f'Debug dump the CPU\n'
            f'__________________________________________________\n'
            f'pc: 0x{self.pc:04X}\n'
            f'Index register: 0x{self.indexRegister:04X}\n'
            f'Sound timer: 0x{self.soundTimer:04X}\n'
            f'Delay timer: 0x{self.delayTimer:04X}\n'            
            f'Current instruction: 0x{self.instruction:04X}\n'
            f'Instruction count: {self.instructionCount}\n'
            f'Rom loaded? {self.romLoaded}'
            f'{self.registers}\n'
            f'{self.stack}\n'
            f'{self.keypad}'
        )

        return cpuDump

    @classmethod
    def generateRandomByte(cls) -> int:
        return randint(0, 255)
