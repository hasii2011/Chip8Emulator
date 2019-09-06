
from typing import List

from logging import Logger
from logging import getLogger

from pygame import Surface

from albow.widgets.TextBox import TextBox

from org.hasii.chip8.Chip8InstructionList import Chip8InstructionList


class Chip8UIInstructionList(TextBox):

    def __init__(self, instructionList: Chip8InstructionList, theNumberOfColumns: int = 16, theNumberOfRows: int = 10):

        self.instructionList: Chip8InstructionList = instructionList

        super().__init__(theNumberOfColumns=theNumberOfColumns, theNumberOfRows=theNumberOfRows)

        self.logger: Logger = getLogger(__name__)

    def draw(self, theSurface: Surface):

        if self.instructionList.dirty is True:
            self.clearText()
            stackList: List[str] = self.instructionList.toString().split('\n')

            for stkItem in stackList:
                self.addText(stkItem)
            self.instructionList.dirty = False

        super().draw(theSurface=theSurface)
