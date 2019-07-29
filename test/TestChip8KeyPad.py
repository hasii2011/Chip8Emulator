
from logging import Logger
from logging import getLogger

from test.BaseTest import BaseTest

from org.hasii.chip8.Chip8KeyPad import Chip8KeyPad


class TestChip8KeyPad(BaseTest):

    clsLogger: Logger = None

    @classmethod
    def setUpClass(cls):
        """"""
        BaseTest.setUpLogging()
        TestChip8KeyPad.clsLogger = getLogger(__name__)

    def setUp(self):
        """"""
        self.logger:    Logger      = TestChip8KeyPad.clsLogger
        self.keypad:    Chip8KeyPad = Chip8KeyPad()

    def testStringRepr(self):

        self.logger.info(f"{self.keypad}")
