
from typing import List

from logging import Logger
from logging import getLogger


class Chip8Stack:

    STACK_LIMIT: int = 32
    """
    From https://en.wikipedia.org/wiki/CHIP-8#Notes  See the pdf that
    references CHIP-8.com
    """

    def __init__(self):

        self.logger: Logger    = getLogger(__name__)
        self.items:  List[int] = []

    def isEmpty(self):
        return self.items == []

    def push(self, item: int):
        self.items.append(item)
        if len(self.items) > Chip8Stack.STACK_LIMIT:
            self.logger.warning(f"Exceeded artificial stack limit of: {Chip8Stack.STACK_LIMIT}")

    def pop(self) -> int:
        return self.items.pop()

    def peek(self) -> int:
        return self.items[len(self.items) - 1]

    def size(self) -> int:
        return len(self.items)

    def __repr__(self):
        stackDump: str = (
            f'Stack Dump\n'
            f'_____________________________\n'
        )
        stackDepth: int = len(self.items)
        if stackDepth == 0:
            stackDump += f'empty {{}}'
        else:
            for x in range(stackDepth):
                stackDump += f'\nStack entry[{x}] - 0x{self.items[x]:04X}'

        return stackDump
