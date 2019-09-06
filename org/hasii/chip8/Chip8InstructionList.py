
from logging import Logger
from logging import getLogger

from collections import deque


class Chip8InstructionList:
    """
    Implements a FIFO queue;  Items enter on the left and exit on the right.
    """
    MAX_INSTRUCTIONS: int = 10

    def __init__(self):

        self.logger: Logger = getLogger(__name__)
        self.deque:  deque  = deque(maxlen=Chip8InstructionList.MAX_INSTRUCTIONS)

    def add(self, item: str):
        self.deque.appendleft(item)

    def remove(self) -> str:
        return self.deque.pop()

    def size(self) -> int:
        return len(self.deque)

    def __repr__(self):

        retStr: str = '['
        for item in self.deque:
            retStr += f'{item}, '

        retStr = retStr.strip(', ')
        retStr += f', maxlen={self.deque.maxlen}'
        retStr += ']'

        return retStr
