
from typing import List

from pygame import Surface

from logging import Logger
from logging import getLogger

from albow.widgets.TextBox import TextBox

from org.hasii.chip8.Chip8Stack import Chip8Stack


class Chip8UIStack(TextBox):

    def __init__(self, theChipStack: Chip8Stack, theNumberOfColumns: int = 12, theNumberOfRows: int = 10):

        self.logger:       Logger     = getLogger(__name__)
        self.chip8Stack:   Chip8Stack = theChipStack
        self.lastStackLen: int        = self.chip8Stack.size()

        super().__init__(theNumberOfColumns=theNumberOfColumns, theNumberOfRows=theNumberOfRows)

    def draw(self, theSurface: Surface):

        if self.chip8Stack.size() != self.lastStackLen:
            self.clearText()
            stackList: List[str] = self.chip8Stack.toString().split('\n')

            for stkItem in stackList:
                self.addText(stkItem)
            self.lastStackLen = self.chip8Stack.size()

        super().draw(theSurface=theSurface)
