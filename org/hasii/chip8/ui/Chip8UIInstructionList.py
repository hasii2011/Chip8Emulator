
from logging import Logger
from logging import getLogger

from albow.widgets.TextBox import TextBox

from org.hasii.chip8.Chip8InstructionList import Chip8InstructionList


class Chip8UIInstructionList(TextBox):

    def __init__(self, instructionList: Chip8InstructionList, theNumberOfColumns: int = 12, theNumberOfRows: int = 10):

        self.instructionList: Chip8InstructionList = instructionList

        super().__init__(theNumberOfColumns=theNumberOfColumns, theNumberOfRows=theNumberOfRows)

        self.logger: Logger = getLogger(__name__)
