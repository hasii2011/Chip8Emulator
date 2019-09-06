
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
        self.instructionList.add('ADD V8,0xBB')
        self.logger.info(f'testBasicFIFO - instructionList: {self.instructionList}')

        self.instructionList.add('ADDI I,V7')
        self.logger.info(f'testBasicFIFO - instructionList: {self.instructionList}')

        self.instructionList.add('CALL  0x0123')
        self.logger.info(f'testBasicFIFO - instructionList: {self.instructionList}')

        expectedValue: str = 'ADD V8,0xBB'
        actualValue:   str = self.instructionList.remove()

        self.assertEqual(expectedValue, actualValue, 'Wah!  Basic FIFO is broken')

    def testExtendedFIFO(self):

        self._setupFIFO()

        expectedValue: str = 'WAITKEY VC,K'
        actualValue:   str = self.instructionList.remove()

        self.assertEqual(expectedValue, actualValue, 'Wah!  Extended FIFO is broken')

    def testFILOSize(self):

        self._setupFIFO()

        expectedValue: int = 6
        actualValue:   int = self.instructionList.size()

        self.assertEqual(expectedValue, actualValue, 'Ouch count does not match')

    def _setupFIFO(self):

        self.instructionList.add('WAITKEY VC,K')
        self.instructionList.add('MOVM [I],V3')
        self.instructionList.add('RNDMSK V9,0x22')
        self.instructionList.add('XOR VC,V4')
        self.instructionList.add('AND VC,V4')
        self.instructionList.add('SHL VA')

        self.logger.info(f'_setupFILO - instructionList: {self.instructionList}')
