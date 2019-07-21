
from logging import Logger
from logging import getLogger

from pkg_resources import resource_filename


class Chip8:

    ROM_PKG               = "org.hasii.chip8.roms"
    PROGRAM_START_ADDRESS = 0x200

    def __init__(self):

        self.logger: Logger = getLogger(__name__)

        self.memory = [0] * 4096

        self.logger.info(f"{self.memory}")

    def initializeChip(self):
        self.logger.info(f"Initializing")

    def loadROM(self, theFilename: str):

        self.logger.info(f"loading ROM: {theFilename}")
        fullFileName: str = self.findTheROM(theFilename)

        fd = open(fullFileName, 'rb')
        rom: bytes = fd.read()
        fd.close()

        for byte in range(len(rom)):
            self.memory[byte] = rom[byte]

        self.logger.info(f"{self.memory}")
        self._debugPrintROM(rom)

    def findTheROM(self, theFileName: str):

        fileName = resource_filename(Chip8.ROM_PKG, theFileName)

        self.logger.debug(f"The full file name: {fileName}")
        return fileName

    def _debugPrintROM(self, rom: bytes):
        hexROM: str = rom.hex()
        romLength: int = len(hexROM)
        for x in range(0, romLength, 32):
            endByteIndex: int = x + 32
            subStr: str = hexROM[x:endByteIndex]
            self.logger.info(f"{subStr}")
