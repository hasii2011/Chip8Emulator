
from typing import List

from logging import Logger
from logging import getLogger


class Chip8Stack:

    STACK_LIMIT: int = 16

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
