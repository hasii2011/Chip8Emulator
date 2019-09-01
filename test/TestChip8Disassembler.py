
from logging import Logger
from logging import getLogger

from test.BaseTest import BaseTest
from org.hasii.chip8.disassembler.Chip8Disassembler import Chip8Disassembler


class TestChip8Disassembler(BaseTest):

    clsLogger: Logger = None

    @classmethod
    def setUpClass(cls):
        """"""
        BaseTest.setUpLogging()
        TestChip8Disassembler.clsLogger = getLogger(__name__)

    def setUp(self):
        """"""
        self.logger:       Logger            = TestChip8Disassembler.clsLogger
        self.disassembler: Chip8Disassembler = Chip8Disassembler()

    def testNada(self):

        self.logger.info(f'I should see this')

    def testRTS(self):

        instruction: int = 0x00EE
        asm: str = self.disassembler.disAssemble(pc=0x200, instruction=instruction)

        self.logger.info(f'{asm}')
