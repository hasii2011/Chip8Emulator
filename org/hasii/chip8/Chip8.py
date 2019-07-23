
from typing import List

from logging import Logger
from logging import getLogger

from pkg_resources import resource_filename

from org.hasii.chip8.Chip8Stack import Chip8Stack
from org.hasii.chip8.Chip8Mnemonics import Chip8Mnemonics


class Chip8:

    ROM_PKG               = "org.hasii.chip8.roms"
    PROGRAM_START_ADDRESS = 0x200
    OPCODE_MASK           = 0xF000

    CPU_CYCLE: int = 1000 // 60

    def __init__(self):

        self.logger: Logger = getLogger(__name__)

        self.pc:         int = 0x200
        self.opcode:     int = 0x0000

        self.memory:     List[int]  = [0] * 4096
        self.stack:      Chip8Stack = Chip8Stack()

        self._delayTimer: int = 0
        self._soundTimer: int = 0

        self.logger.debug(f"{self.memory}")

    def getDelayTimer(self):
        return self._delayTimer

    def setDelayTimer(self, theNewValue):
        if self._delayTimer > 0:
            self._delayTimer = theNewValue

    def getSoundTimer(self):
        return self._soundTimer

    def setSoundTimer(self, theNewValue):
        if self._soundTimer > 0:
            self._soundTimer = theNewValue

    delayTimer = property(getDelayTimer, setDelayTimer)
    soundTimer = property(getSoundTimer, setSoundTimer)

    def emulateASingleCpuCycle(self):

        self.fetchOpCode()
        if (self.opcode & Chip8.OPCODE_MASK) == Chip8Mnemonics.JP:
            addr = self.opcode & 0x0FFF
            self.pc = addr
            self.logger.info(f"new pc: {self.pc}")

    def fetchOpCode(self):
        self.opcode = self.memory[self.pc] << 8 | self.memory[self.pc + 1]
        self.logger.info(f"pc: {hex(self.pc)} opcode: {hex(self.opcode)}")

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

    def _debugPrintMemory(self):

        romLength: int = len(self.memory)
        for x in range(0, romLength, 32):
            endByteIndex: int = x + 32
            subMemory = self.memory[x:endByteIndex]
            subMemoryBytes: bytes = bytes(subMemory)
            subStr: str = subMemoryBytes.hex()
            self.logger.info(f"{hex(x):6} {hex(endByteIndex-2):6}  {subStr}")
