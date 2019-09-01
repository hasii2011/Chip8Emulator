
from logging import Logger
from logging import getLogger

from test.BaseTest import BaseTest
from org.hasii.chip8.disassembler.Chip8Disassembler import Chip8Disassembler
from org.hasii.chip8.Chip8Mnemonics import Chip8Mnemonics


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

        instruction: int = Chip8Mnemonics.RTS.value
        asm: str = self.disassembler.disAssemble(pc=0x200, instruction=instruction)

        self.logger.info(f'{asm}')
        self.assertEqual('0x0200    RTS', asm, 'RTS Disassembly not correct')

    def testCLS(self):

        instruction: int = Chip8Mnemonics.CLS.value
        asm: str = self.disassembler.disAssemble(pc=0x200, instruction=instruction)

        self.logger.info(f'{asm}')
        self.assertEqual('0x0200    CLS', asm, 'CLS Disassembly not correct')
