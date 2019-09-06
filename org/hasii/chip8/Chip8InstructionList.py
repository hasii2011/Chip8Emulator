
from logging import Logger
from logging import getLogger

from collections import deque


class Chip8InstructionList:
    """
    Implements a FIFO queue;  Items enter on the left and exit on the right.
    It is up to the consumer to set `dirty` to False when it reads the list
    """
    MAX_INSTRUCTIONS: int = 10

    def __init__(self):

        self.logger: Logger = getLogger(__name__)
        self.deque:  deque  = deque(maxlen=Chip8InstructionList.MAX_INSTRUCTIONS)
        self._dirty: bool   = False

    def getDirty(self) -> bool:
        return self._dirty

    def setDirty(self, newValue: bool):
        self._dirty = newValue

    dirty    = property(getDirty, setDirty)

    def add(self, item: str):
        self.deque.appendleft(item)
        self.dirty = True

    def remove(self) -> str:
        self.dirty = True
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
