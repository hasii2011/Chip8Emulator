
from logging import Logger
from logging import getLogger


class Chip8:

    ROM_DIRECTORY = 'roms'
    def __init__(self):

        self.logger: Logger = getLogger(__name__)

    def initializeChip(self):
        self.logger.info(f"Initializing")

    def loadROM(self, theFilename: str):
        self.logger.info(f"loading ROM: {theFilename}")
