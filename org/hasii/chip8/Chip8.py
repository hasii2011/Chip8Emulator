
from typing import List
from typing import Dict
from typing import Callable

from logging import Logger
from logging import getLogger

from pkg_resources import resource_filename

from org.hasii.chip8.Chip8Stack import Chip8Stack
from org.hasii.chip8.Chip8Mnemonics import Chip8Mnemonics
from org.hasii.chip8.Chip8Registers import Chip8Registers
from org.hasii.chip8.Chip8RegisterName import Chip8RegisterName

from org.hasii.chip8.errors.UnknownInstructionError import UnknownInstructionError
from org.hasii.chip8.errors.InvalidIndexRegisterValue import InvalidIndexRegisterValue


class Chip8:

    ROM_PKG               = "org.hasii.chip8.roms"
    PROGRAM_START_ADDRESS = 0x200
    OPCODE_MASK           = 0xF000
    IDX_REG_MASK          = 0x0FFF
    MAX_IDX_REG_VAL       = 0x0FFF
    INSTRUCTION_SIZE      = 2       # in bytes

    CPU_CYCLE: int = 1000 // 60

    def __init__(self):

        self.logger: Logger = getLogger(__name__)

        self.pc:            int = Chip8.PROGRAM_START_ADDRESS
        self.instruction:   int = 0x0000

        self.memory:     List[int]      = [0] * 4096
        self.stack:      Chip8Stack     = Chip8Stack()
        self.registers:  Chip8Registers = Chip8Registers()

        self._indexRegister: int = 0
        self._delayTimer:    int = 0
        self._soundTimer:    int = 0

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
            Chip8Mnemonics.LDI.value:  self.loadIndexRegister
        }

        self.logger.debug(f"{self.memory}")

    def getDelayTimer(self) -> int:
        return self._delayTimer

    def setDelayTimer(self, theNewValue: int):
        if self._delayTimer > 0:
            self._delayTimer = theNewValue

    def getSoundTimer(self) -> int:
        return self._soundTimer

    def setSoundTimer(self, theNewValue: int):
        if self._soundTimer > 0:
            self._soundTimer = theNewValue

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
        self.logger.debug(f"currentInstruction {instStr}")

        op: int = self.instruction & Chip8.OPCODE_MASK

        try:
            instruction = self.opCodeMethods[op]
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

    def loadROM(self, theFilename: str):

        self.logger.info(f"loading ROM: {theFilename}")
        fullFileName: str = self._findTheROM(theFilename)

        fd = open(fullFileName, 'rb')
        rom: bytes = fd.read()
        fd.close()

        for byte in range(len(rom)):
            self.memory[self.pc + byte] = rom[byte]

        self.logger.debug(f"{self.memory}")
        self._debugPrintMemory()

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

    def _decodeRegisterToRegisterOpCode(self):
        return self.instruction & 0x000f

    def _debugPrintMemory(self):

        romLength: int = len(self.memory)
        for x in range(0, romLength, 32):
            endByteIndex: int = x + 32
            subMemory = self.memory[x:endByteIndex]
            subMemoryBytes: bytes = bytes(subMemory)
            subStr: str = subMemoryBytes.hex()

            self.logger.info(f"{hex(x):6} {hex(endByteIndex-2):6}  {subStr}")
