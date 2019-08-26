
from typing import List

from logging import getLogger
from logging import Logger

from test.BaseTest import BaseTest

from org.hasii.chip8.Chip8Stack import Chip8Stack


class TestChip8Stack(BaseTest):

    clsLogger: Logger = None

    @classmethod
    def setUpClass(cls):
        """"""
        BaseTest.setUpLogging()
        TestChip8Stack.clsLogger = getLogger(__name__)

    def setUp(self):
        """"""
        self.chip8Stack:  Chip8Stack  = Chip8Stack()
        self.chip8Stack.push(0x0200)
        self.chip8Stack.push(0x0300)
        self.chip8Stack.push(0x0400)
        self.chip8Stack.push(0x0500)
        self.logger: Logger = TestChip8Stack.clsLogger

    def testString(self):
        self.logger.info(f'\n{self.chip8Stack.toString()}')

        stackList: List[str] = self.chip8Stack.toString().split('\n')

        self.logger.info(f'{stackList}')
