
from typing import List

from logging import Logger
from logging import getLogger


class Chip8InstructionList:
    """
    Implements a FIFO queue;  Items enter on the left and exit on the right.
    It is up to the consumer to set `dirty` to False when it reads the list
    """
    MAX_INSTRUCTIONS: int = 10

    def __init__(self, maxItems: int = MAX_INSTRUCTIONS):

        self.logger: Logger = getLogger(__name__)
        self.maxlen: int       = maxItems
        self.items:  List[str] = []

        self._dirty: bool   = False

    def getDirty(self) -> bool:
        return self._dirty

    def setDirty(self, newValue: bool):
        self._dirty = newValue

    dirty = property(getDirty, setDirty)

    def add(self, item: str):
        self.items.append(item)
        self.dirty = True

    def remove(self) -> str:
        self.dirty = True
        return self.items.pop(0)

    def size(self) -> int:
        return len(self.items)

    def toString(self):
        queueDump: str = ''
        queueDepth: int = len(self.items)
        for x in range(queueDepth):
            queueDump += f'{self.items[x]}\n'
        return queueDump

    def __repr__(self):

        retStr: str = '['
        for item in self.items:
            retStr += f'{item}, '

        retStr = retStr.strip(', ')
        retStr += f', maxlen={self.maxlen}'
        retStr += ']'

        return retStr
