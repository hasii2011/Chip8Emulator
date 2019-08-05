
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
from org.hasii.chip8.Chip8KeyPad import Chip8KeyPad
from org.hasii.chip8.Chip8Mnemonics import Chip8Mnemonics
from org.hasii.chip8.Chip8Registers import Chip8Registers
from org.hasii.chip8.Chip8RegisterName import Chip8RegisterName

from org.hasii.chip8.errors.UnknownInstructionError import UnknownInstructionError
from org.hasii.chip8.errors.InvalidIndexRegisterValue import InvalidIndexRegisterValue
from org.hasii.chip8.errors.UnKnownSpecialRegistersSubOpCode import UnKnownSpecialRegistersSubOpCode

BIT0_MASK: int = 0x80
BIT1_MASK: int = 0x40
BIT2_MASK: int = 0x20
BIT3_MASK: int = 0x10
BIT4_MASK: int = 0x08
BIT5_MASK: int = 0x04
BIT6_MASK: int = 0x02
BIT7_MASK: int = 0x01

BIT_MASKS: List[int] = [BIT0_MASK, BIT1_MASK, BIT2_MASK, BIT3_MASK, BIT4_MASK, BIT5_MASK, BIT6_MASK, BIT7_MASK]


class Chip8:

    debugVirtualScreen: bool = True

    ROM_PKG               = "org.hasii.chip8.roms"
    PROGRAM_START_ADDRESS = 0x200
    OPCODE_MASK           = 0xF000
    ENHANCED_OP_CODE_MASK = 0xF0FF
    IDX_REG_MASK          = 0x0FFF
    LOC_JMP_MASK          = 0x0FFF
    MAX_IDX_REG_VAL       = 0x0FFF

    INSTRUCTION_SIZE      = 2       # in bytes

    SPECIAL_REGISTERS_BASE_OP_CODE = 0xF000

    CPU_CYCLE: int = 1000 // 60

    VIRTUAL_WIDTH:        int = 64
    VIRTUAL_HEIGHT:       int = 32

    VIRTUAL_SCREEN_ROW = List[int]
    virtualScreen: List[VIRTUAL_SCREEN_ROW] = []

    def __init__(self):

        self.logger: Logger = getLogger(__name__)

        self.pc:            int = Chip8.PROGRAM_START_ADDRESS
        self.instruction:   int = 0x0000

        self.memory:     List[int]      = [0] * 4096
        self.stack:      Chip8Stack     = Chip8Stack()
        self.registers:  Chip8Registers = Chip8Registers()
        self.keypad:     Chip8KeyPad    = Chip8KeyPad()

        self._indexRegister: int = 0
        self._delayTimer:    int = 0
        self._soundTimer:    int = 0

        seed()
        self.opCodeMethods: Dict[int, Callable] = {

            Chip8Mnemonics.JP.value:   self.jumpToAddress,
            Chip8Mnemonics.SEL.value:  self.skipIfRegisterEqualToLiteral,
            Chip8Mnemonics.SNEL.value: self.skipIfRegisterNotEqualToLiteral,
            Chip8Mnemonics.SER.value:  self.skipIfRegisterEqualToRegister,
            Chip8Mnemonics.LDL.value:  self.loadRegisterWithLiteral,
            Chip8Mnemonics.ADD.value:  self.addLiteralToRegister,
            Chip8Mnemonics.LDR.value:  self.registerToRegisterInstructions,
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
            Chip8Mnemonics.RND.value:  self.rndByte,
            Chip8Mnemonics.DRW.value:  self.displaySprite,
            Chip8Mnemonics.SKP.value:  self.skipNextVxDependingOnKeyPressed,
            Chip8Mnemonics.SKNP.value: self.skipNextVxDependingOnKeyPressed,
            Chip8Mnemonics.LDRT.value: self.specialRegistersInstructions,
            Chip8Mnemonics.LDK.value:  self.specialRegistersInstructions,
            Chip8Mnemonics.SDT.value:  self.specialRegistersInstructions,
            Chip8Mnemonics.SST.value:  self.specialRegistersInstructions,
            Chip8Mnemonics.ADDI.value: self.specialRegistersInstructions,
            Chip8Mnemonics.LDIS.value: self.specialRegistersInstructions,
            Chip8Mnemonics.LDB.value:  self.specialRegistersInstructions,
            Chip8Mnemonics.STR.value:  self.specialRegistersInstructions,
            Chip8Mnemonics.RDR.value:  self.specialRegistersInstructions,
        }
        self.logger.debug(f"{self.memory}")

        for row in range(0, self.VIRTUAL_HEIGHT):
            columns: List[int] = []
            for col in range(0, self.VIRTUAL_WIDTH):
                columns. append(0)
            self.virtualScreen.append(columns)

    def getDelayTimer(self) -> int:
        return self._delayTimer

    def setDelayTimer(self, theNewValue: int):
        if theNewValue > 0:
            self._delayTimer = theNewValue

    def decrementDelayTimer(self):
        if self._delayTimer > 0:
            self._delayTimer -= 1

    def getSoundTimer(self) -> int:
        return self._soundTimer

    def setSoundTimer(self, theNewValue: int):
        if theNewValue > 0:
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

        instStr: str = hex(self.instruction)
        self.logger.debug(f"currentInstruction: {instStr}")

        op: int = self.instruction & Chip8.OPCODE_MASK

        if op == Chip8.SPECIAL_REGISTERS_BASE_OP_CODE:
            op = self.instruction & Chip8.ENHANCED_OP_CODE_MASK

        opStr: str = hex(op)
        self.logger.debug(f"opStr: {opStr}")
        try:
            instruction: Callable = self.opCodeMethods[op]
        except KeyError:
            raise UnknownInstructionError(badInstruction=op)

        instruction()

    def fetchInstruction(self):
        self.instruction = self.memory[self.pc] << 8 | self.memory[self.pc + 1]
        self.logger.info(f"pc: {hex(self.pc)} instruction: {hex(self.instruction)}")

    def jumpToAddress(self):
        addr = self.instruction & 0x0FFF
        self.pc = addr
        self.logger.info(f"new pc: {hex(self.pc)}")

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
        self.logger.info(f"Reg to Reg subOpCode: {subOpCode:X}")

        leftRegister:  Chip8RegisterName = self._decodeLeftRegister()
        rightRegister: Chip8RegisterName = self._decodeRightRegister()

        rightRegVal: int = self.registers.getValue(rightRegister)

        if subOpCode == 0x0:    # 8xy0; LDR Vx, Vy;     Set Vx = Vy.
            self.registers.setValue(v=leftRegister, newValue=rightRegVal)
        elif subOpCode == 0x1:  # 8xy1; OR Vx, Vy;      Set Vx = Vx OR Vy
            self.registers.orOp(v=leftRegister, mask=rightRegVal)
        elif subOpCode == 0x2:  # 8xy2; AND Vx, Vy;     Set Vx = Vx AND Vy
            self.registers.andOp(v=leftRegister, mask=rightRegVal)
        elif subOpCode == 0x3:   # 8xy3; XOR Vx, Vy;     Set Vx = Vx XOR Vy
            self.registers.xorOp(v=leftRegister, mask=rightRegVal)
        elif subOpCode == 0x4:   # 8xy4; ADD Vx, Vy;     Set Vx = Vx + Vy
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
        Bnnn; JP V0, addr;    Jump to location nnn + V0       The program counter is set to nnn plus the value of V0
        """
        v0Val:    int = self.registers.getValue(Chip8RegisterName.V0)
        instrVal: int = self.instruction & 0x0FFF

        self.pc = self.pc + v0Val + instrVal

    def rndByte(self):
        """
        Cxkk; RND Vx, byte;   Set Vx = random byte AND kk

        Interpreter generates a random number from 0 to 255

        """
        targetRegister: Chip8RegisterName = self._decodeLeftRegister()
        lit:        int = self._decodeLiteral()
        randByte:   int = self.generateRandomByte()
        self.logger.info(f"randByte: {randByte:X}")

        tempReg: int = randByte & lit
        self.registers.setValue(v=targetRegister, newValue=tempReg)

    def displaySprite(self):
        """
        Dxyn; DRW Vx, Vy, nibble;

        Display n-byte sprite starting at memory location I at (Vx, Vy), set VF = collision

        TODO:
        """
        pass

    def skipNextVxDependingOnKeyPressed(self):
        """
        Ex9E; SKP Vx;

        Skip next instruction if key with the value of Vx is pressed

        ExA1; SKNP Vx;

        Skip next instruction if key with the value of Vx is not pressed

        TODO:
        """
        pass

    def specialRegistersInstructions(self):
        """
        LDRT = 0xF007   # Fx07; LDT Vx, DT;     Set Vx = delay timer value
        LDK  = 0xF00A   # Fx0A; LDK Vx, K;      Wait for a key press, store the value of the key in Vx.
        SDT  = 0xF015   # Fx15; SDT DT, Vx;     Set delay timer = Vx
        SST  = 0xF018   # Fx18; SST ST, Vx;     Set sound timer = Vx
        ADDI = 0xF01E   # Fx1E; ADDI I, Vx;     Set I = I + Vx
        LDIS = 0xF029   # Fx29; LDIS F, Vx;     I equals location of sprite for the character in Vx; chars 0-F represented by a 4x5 font
        LDB  = 0xF033   # Fx33; LDB B, Vx;      Store BCD representation of Vx in memory locations I, I+1, and I+2
        STR  = 0xF055   # Fx55; STR [I], Vx;    Store registers V0-Vx in memory starting at location I.
        RDR  = 0xF065   # Fx65; RDR Vx, [I];    Read registers V0-Vx from memory starting at location I.
        """
        subOpCode: int = self._decodeSpecialRegistersSubOpCode()
        self.logger.info(f"Special Registers subOpCode: {subOpCode:X}")

        regName: Chip8RegisterName = self._decodeLeftRegister()

        if subOpCode == 0x07:
            self.registers.setValue(v=regName, newValue=self.delayTimer)
        elif subOpCode == 0x0A:
            pass
        elif subOpCode == 0x15:
            self.delayTimer = self.registers.getValue(regName)
        elif subOpCode == 0x18:
            self.soundTimer = self.registers.getValue(regName)
        elif subOpCode == 0x1E:
            self.indexRegister += self.registers.getValue(regName)
        elif subOpCode == 0x29:
            pass
        elif subOpCode == 0x33:
            regVal:  int  = self.registers.getValue(regName)
            memLoc:  int = self.indexRegister

            self.memory[memLoc]     = regVal // 100
            self.memory[memLoc + 1] = (regVal // 10) % 10
            self.memory[memLoc + 2] = (regVal % 100) % 10
            self.logger.info(f"memLoc: '{self.memory[memLoc]}' memLoc+1: '{self.memory[memLoc+1]}' memLoc+2: '{self.memory[memLoc+2]}'")

        elif subOpCode == 0x55:
            lastRegValue: int = cast(int, regName.value)
            for x in range(0, lastRegValue + 1):
                self.memory[self.indexRegister + x] = self.registers.getValue(regName)
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

        self.logger.debug(f"{self.memory}")
        self._debugPrintMemory(startByteNbr=0, nBytes=len(self.memory))

    def loadSprite(self, theSprite: List[int], startMemoryAddress: int):

        memAddress: int = startMemoryAddress
        for sprite in theSprite:
            self.memory[memAddress] = sprite
            memAddress += 1

    def drawOnVirtualScreen(self, xCoord: int, yCoord: int, nBytes: int):
        """

        Args:
            xCoord: x-coordinate on virtual screen
            yCoord: y-coordinate on virtual screen
            nBytes: The number of bytes to copy from where the `indexRegister` points
        """
        self.registers.setValue(Chip8RegisterName.VF, Chip8Registers.NO_SPRITE_COLLISION_BIT)

        startAddress: int = self.indexRegister

        for byteNum in range(nBytes):
            currentVirtualScreenRow: Chip8.VIRTUAL_SCREEN_ROW = self.virtualScreen[yCoord]

            for bitNum in range(8):
                spriteByte:       int = self.memory[startAddress + byteNum]
                maskedSpriteBit:  int = spriteByte & BIT_MASKS[bitNum]
                spriteBit = maskedSpriteBit >> (7 - bitNum)
                self.logger.debug(f"spriteByte: {bin(spriteByte)} spriteBit: {spriteBit:X}")
                currentVirtualScreenRow[xCoord + bitNum] = spriteBit
            yCoord += 1
        self._dumpVirtualScreen()

    def _findTheROM(self, theFileName: str):

        fileName = resource_filename(Chip8.ROM_PKG, theFileName)

        self.logger.debug(f"The full file name: {fileName}")
        return fileName

    def _decodeLeftRegister(self) -> Chip8RegisterName:
        return self._decodeRegister()

    def _decodeRightRegister(self) -> Chip8RegisterName:
        vx = (self.instruction & 0x00F0) >> 4
        register: Chip8RegisterName = Chip8RegisterName(vx)

        return register

    def _decodeRegister(self) -> Chip8RegisterName:

        vx = (self.instruction & 0x0F00) >> 8
        register: Chip8RegisterName = Chip8RegisterName(vx)

        return register

    def _decodeLiteral(self) -> int:
        return self.instruction & 0x00FF

    def _decodeSpecialRegistersSubOpCode(self):
        return self.instruction & 0x00FF

    def _decodeRegisterToRegisterOpCode(self):
        return self.instruction & 0x000F

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

        z: int = startByteNbr
        while z < (startByteNbr + nBytes):

            endByteIndex: int = z + bytesPerRow
            subMemory = self.memory[z:endByteIndex]
            subMemoryBytes: bytes = bytes(subMemory)
            subStr:         str   = subMemoryBytes.hex()

            self.logger.info(f"{z:05X} {endByteIndex-2:05X}  {subStr.upper()}")

            z += bytesPerRow

    def _dumpVirtualScreen(self,
                           startRow: int = 0, xCoord: int = 0, nRows: int = VIRTUAL_HEIGHT,
                           startCol: int = 0, yCoord: int = 0, nCols: int = VIRTUAL_WIDTH):

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

    @classmethod
    def generateRandomByte(cls) -> int:
        return randint(0, 255)
