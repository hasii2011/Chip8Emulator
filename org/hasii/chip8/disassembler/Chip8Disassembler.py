
from logging import Logger
from logging import getLogger


class Chip8Disassembler:

    def __init__(self):

        self.logger: Logger = getLogger(__name__)

    def disAssemble(self, opCode: int) -> str:

        mnemonicInstr: str = ''

        return mnemonicInstr
