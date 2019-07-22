
from typing import List

from logging import Logger
from logging import getLogger

from pkg_resources import resource_filename

from org.hasii.chip8.Chip8Stack import Chip8Stack


class Chip8:

    ROM_PKG               = "org.hasii.chip8.roms"
    PROGRAM_START_ADDRESS = 0x200

    def __init__(self):

        self.logger: Logger = getLogger(__name__)

        self.memory: List[int]  = [0] * 4096
        self.pc:     int        = 0x200
        self.opcode: int        = 0x0000
        self.stack:  Chip8Stack = Chip8Stack()

        self.initializeChip()
        self.logger.debug(f"{self.memory}")

    def initializeChip(self):
        self.logger.info(f"Initializing")

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

    def emulateASingleCpuCycle(self):
        self.fetchOpCode()

    def fetchOpCode(self):
        self.opcode = self.memory[self.pc] << 8 | self.memory[self.pc + 1]
        self.logger.info(f"pc: {hex(self.pc)} opcode: {hex(self.opcode)}")

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
