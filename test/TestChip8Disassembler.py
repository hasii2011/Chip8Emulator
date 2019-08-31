
from logging import Logger
from logging import getLogger

from test.BaseTest import BaseTest


class TestChip8Disassembler(BaseTest):

    clsLogger: Logger = None

    @classmethod
    def setUpClass(cls):
        """"""
        BaseTest.setUpLogging()
        TestChip8Disassembler.clsLogger = getLogger(__name__)

    def setUp(self):
        """"""
        self.logger:       Logger                = TestChip8Disassembler.clsLogger
        self.disassembler: TestChip8Disassembler = TestChip8Disassembler()

    def testNada(self):

        self.logger.info(f'I should see this')
