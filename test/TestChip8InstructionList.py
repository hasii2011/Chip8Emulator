
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

    def testBasicFILO(self):

        self.logger.info(f'testBasicFILO - instructionList: {self.instructionList}')
        self.instructionList.add(0xFF)
        self.logger.info(f'testBasicFILO - instructionList: {self.instructionList}')

        self.instructionList.add(0xEE)
        self.logger.info(f'testBasicFILO - instructionList: {self.instructionList}')

        self.instructionList.add(0xDD)
        self.logger.info(f'testBasicFILO - instructionList: {self.instructionList}')

        expectedValue: int = 0xDD
        actualValue:   int = self.instructionList.remove()

        self.assertEqual(hex(expectedValue), hex(actualValue), 'Wah!  Basic FILO is broken')

    def testExtendedFilo(self):

        self._setupFILO()

        expectedValue: int = 0xAA
        actualValue:   int = self.instructionList.remove()

        self.assertEqual(expectedValue, actualValue, 'Wah!  Extended FILO is broken')

    def testFILOSize(self):

        self._setupFILO()

        expectedValue: int = 6
        actualValue:   int = self.instructionList.size()

        self.assertEqual(expectedValue, actualValue, 'Ouch count does not match')

    def _setupFILO(self):

        self.instructionList.add(0xFF)
        self.instructionList.add(0xEE)
        self.instructionList.add(0xDD)
        self.instructionList.add(0xCC)
        self.instructionList.add(0xBB)
        self.instructionList.add(0xAA)

        self.logger.info(f'_setupFILO - instructionList: {self.instructionList}')
