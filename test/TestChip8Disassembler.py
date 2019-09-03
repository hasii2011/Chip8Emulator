
from logging import Logger
from logging import getLogger

from test.BaseTest import BaseTest
from org.hasii.chip8.disassembler.Chip8Disassembler import Chip8Disassembler
from org.hasii.chip8.Chip8Mnemonics import Chip8Mnemonics

ADDR1: int = 0x0200
ADDR2: int = 0x0222
ADDR3: int = 0x02F0

ADDR1_STR: str = '0x0200'
ADDR2_STR: str = '0x0222'
ADDR3_STR: str = '0x02F0'


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

    def testRTS(self):

        instruction: int = Chip8Mnemonics.RTS.value
        asm: str = self.disassembler.disAssemble(pc=ADDR1, instruction=instruction)

        self.logger.info(f'{asm}')
        self.assertEqual(f'{ADDR1_STR}    RTS', asm, 'RTS Disassembly not correct')

    def testJumpToAddress(self):

        instr: int = 0x1219
        asm:   str = self.disassembler.disAssemble(pc=ADDR1, instruction=instr)
        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR1_STR}    JUMP  0x0219', asm, 'Call Disassembly not correct')

    def testCLS(self):

        instruction: int = Chip8Mnemonics.CLS.value
        asm: str = self.disassembler.disAssemble(pc=ADDR1, instruction=instruction)

        self.logger.info(f'{asm}')
        self.assertEqual(f'{ADDR1_STR}    CLS', asm, 'CLS Disassembly not correct')

    def testCallSubroutine(self):

        instr: int = 0x2123
        asm:   str = self.disassembler.disAssemble(pc=ADDR1, instruction=instr)
        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR1_STR}    CALL  0x0123', asm, 'Call Disassembly not correct')

    def testSkipBasedOnRegisterEqualToLiteral(self):
        """
        3xkk SE V0, #40;

        """
        instr: int = 0x3C0c
        asm:   str = self.disassembler.disAssemble(pc=ADDR2, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR2_STR}    SEL VC,0x0C', asm, 'SEL Disassembly not correct')

    def testSkipBasedOnRegisterNotEqualToLiteral(self):

        instr: int = 0x4C0c
        asm:   str = self.disassembler.disAssemble(pc=ADDR2, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR2_STR}    SNEL VC,0x0C', asm, 'SNEL Disassembly not correct')

    def testSkipBasedOnRegisterToRegisterEqual(self):

        instr: int = 0x55C0
        asm:   str = self.disassembler.disAssemble(pc=ADDR2, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR2_STR}    SER V5,VC', asm, 'SER Disassembly not correct')

    def testLoadRegisterWithLiteral(self):
        """
        6xkk; LDL Vx, kk
        """
        instr: int = 0x6ABB
        asm:   str = self.disassembler.disAssemble(pc=ADDR3, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR3_STR}    LDL VA,0xBB', asm, 'LDL Disassembly not correct')

    def testAddLiteralToRegister(self):
        """
        7xkk; ADD Vx, kk

        """
        instr: int = 0x78BB
        asm:   str = self.disassembler.disAssemble(pc=ADDR3, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR3_STR}    ADD V8,0xBB', asm, 'LDL Disassembly not correct')
