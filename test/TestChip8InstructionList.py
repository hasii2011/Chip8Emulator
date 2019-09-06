
from typing import List

from logging import Logger
from logging import getLogger

from test.BaseTest import BaseTest

from org.hasii.chip8.Chip8InstructionList import Chip8InstructionList


class TestChip8InstructionList(BaseTest):

    clsLogger: Logger = None

    @classmethod
    def setUpClass(cls):
        """"""
        BaseTest.setUpLogging()
        TestChip8InstructionList.clsLogger = getLogger(__name__)

    def setUp(self):
        """"""
        self.instructionList:  Chip8InstructionList  = Chip8InstructionList()

        self.logger: Logger = TestChip8InstructionList.clsLogger

    def testBasicFIFO(self):

        self.logger.info(f'testBasicFIFO - instructionList: {self.instructionList}')
        self.instructionList.add('0x300  ADD V8,0xBB')
        self.logger.info(f'testBasicFIFO - instructionList: {self.instructionList}')

        self.instructionList.add('0x302  ADDI I,V7')
        self.logger.info(f'testBasicFIFO - instructionList: {self.instructionList}')

        self.instructionList.add('0x304  CALL  0x0123')
        self.logger.info(f'testBasicFIFO - instructionList: {self.instructionList}')

        expectedValue: str = '0x300  ADD V8,0xBB'
        actualValue:   str = self.instructionList.remove()

        self.assertEqual(expectedValue, actualValue, 'Wah!  Basic FIFO is broken')

    def testExtendedFIFO(self):

        self._setupFIFO()

        expectedValue: str = '0x200  WAITKEY VC,K'
        actualValue:   str = self.instructionList.remove()

        self.assertEqual(expectedValue, actualValue, 'Wah!  Extended FIFO is broken')

    def testFIFOSize(self):

        self._setupFIFO()

        expectedValue: int = 6
        actualValue:   int = self.instructionList.size()

        self.assertEqual(expectedValue, actualValue, 'Ouch count does not match')

    def testString(self):

        self._setupFIFO()
        self.logger.info(f'\n{self.instructionList.toString()}')

        instructionList: List[str] = self.instructionList.toString().split('\n')

        self.logger.info(f'{instructionList}')

    def _setupFIFO(self):

        self.instructionList.add('0x200  WAITKEY VC,K')
        self.instructionList.add('0x202  MOVM [I],V3')
        self.instructionList.add('0x204  RNDMSK V9,0x22')
        self.instructionList.add('0x206  XOR VC,V4')
        self.instructionList.add('0x208  AND VC,V4')
        self.instructionList.add('0x20A  SHL VA')

        self.logger.info(f'_setupFILO - instructionList: {self.instructionList}')
