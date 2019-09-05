
from logging import Logger
from logging import getLogger

from albow.widgets.TextBox import TextBox


class Chip8UIInstructionList(TextBox):

    def __init__(self, theNumberOfColumns: int = 12, theNumberOfRows: int = 10):

        self.logger: Logger = getLogger(__name__)

        super().__init__(theNumberOfColumns=theNumberOfColumns, theNumberOfRows=theNumberOfRows)
