
from logging import getLogger
from logging import Logger

from org.hasii.chip8.Chip8RegisterName import Chip8RegisterName


class Chip8Decoder:

    def __init__(self):

        self.logger:       Logger = getLogger(__name__)
        self.instruction: int     = 0x0000

    def _decodeRegisterToRegisterOpCode(self) -> int:
        return self.instruction & 0x000F

    def _decodeLiteral(self) -> int:
        return self.instruction & 0x00FF

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

    def _decodeNibble(self) -> int:
        return self.instruction & 0x00F

    def _decodeSpecialRegistersSubOpCode(self) -> int:
        return self.instruction & 0x00FF

    def _decodeSkipKeyboardRegisterSubOpCode(self) -> int:
        """
        Same mask but want code to self-document
        """
        return self._decodeSpecialRegistersSubOpCode()
