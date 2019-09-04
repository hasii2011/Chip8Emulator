
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

        self.assertEqual(f'{ADDR3_STR}    ADD V8,0xBB', asm, 'ADD Disassembly not correct')

    def testLoadFromRegister(self):
        """
        8xy0; MOV Vx, Vy;     Set Vx = Vy.
        """
        instr: int = 0x8EA0
        asm:   str = self.disassembler.disAssemble(pc=ADDR3, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR3_STR}    MOV VE,VA', asm, 'MOV Disassembly not correct')

    def testRegisterToRegisterOR(self):
        """
        8xy1; OR Vx, Vy;      Set Vx = Vx OR Vy
        """
        instr: int = 0x8C41
        asm:   str = self.disassembler.disAssemble(pc=ADDR3, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR3_STR}    OR VC,V4', asm, 'OR Disassembly not correct')

    def testRegisterToRegisterAnd(self):
        """
        8xy2; AND Vx,Vy;     Set Vx = Vx AND Vy
        """
        instr: int = 0x8C42
        asm:   str = self.disassembler.disAssemble(pc=ADDR3, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR3_STR}    AND VC,V4', asm, 'AND Disassembly not correct')

    def testRegisterToRegisterXor(self):
        """
        8xy3; XOR Vx,Vy;     Set Vx = Vx XOR Vy
        """
        instr: int = 0x8C43
        asm:   str = self.disassembler.disAssemble(pc=ADDR3, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR3_STR}    XOR VC,V4', asm, 'XOR Disassembly not correct')

    def testRegisterToRegisterAdd(self):
        """
        8xy4; ADDR Vx,Vy;     Set Vx = Vx + Vy
        """
        instr: int = 0x8D24
        asm:   str = self.disassembler.disAssemble(pc=ADDR3, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR3_STR}    ADDR VD,V2', asm, 'ADDR Disassembly not correct')

    def testRegisterToRegisterSubtract(self):
        """
        8xy5; SUB Vx,Vy;     Set Vx = Vx - Vy
        """
        instr: int = 0x8D25
        asm:   str = self.disassembler.disAssemble(pc=ADDR3, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR3_STR}    SUB VD,V2', asm, 'SUB Disassembly not correct')

    def testRegisterShiftRight(self):
        """
        8xy6; Set Vx = Vx >> 1
        """
        instr: int = 0x8A06
        asm:   str = self.disassembler.disAssemble(pc=ADDR1, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR1_STR}    SHR VA', asm, 'SHR Disassembly not correct')

    def testSubtractRegisterVyFromRegisterVx(self):
        """
        8xy7; SUBN Vx, Vy;    Set Vx = Vy - Vx
        """
        instr: int = 0x8A07
        asm:   str = self.disassembler.disAssemble(pc=ADDR1, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR1_STR}    SUBN VA,V0', asm, 'SUBN Disassembly not correct')

    def testRegisterShiftLeft(self):
        """
        8xyE; SHL Vx, Vy;     Set Vx = Vx SHL 1
        """
        instr: int = 0x8A0E
        asm:   str = self.disassembler.disAssemble(pc=ADDR2, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR2_STR}    SHL VA', asm, 'SHL Disassembly not correct')

    def testSkipIfRegisterNotEqualToRegister(self):
        """
        9xy0; SNER Vx, Vy;    Skip next instruction if Vx != Vy
        """
        instr: int = 0x9670
        asm:   str = self.disassembler.disAssemble(pc=ADDR2, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR2_STR}    SNER V6,V7', asm, 'SNER Disassembly not correct')

    def testLoadIndexRegister(self):
        """
        Annn; LDI I, addr;    Set I = nnn; The value of register I is set to nnn
        """
        instr: int = 0xA046
        asm:   str = self.disassembler.disAssemble(pc=ADDR2, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR2_STR}    LDI I,0x046', asm, 'LDI Disassembly not correct')

    def testJumpToLocationPlusVZero(self):
        """
        Bnnn; JUMP V0,addr;    Jump to location nnn + V0
        """
        instr: int = 0xB123
        asm:   str = self.disassembler.disAssemble(pc=ADDR2, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR2_STR}    JPV V0,0x123', asm, 'LDI Disassembly not correct')

    def testRndByte(self):
        """
        Cxkk; RNDMSK Vx, byte;   Set Vx = random byte AND kk
        """
        instr: int = 0xC922
        asm:   str = self.disassembler.disAssemble(pc=ADDR2, instruction=instr)

        self.logger.info(f'{asm}')

        self.assertEqual(f'{ADDR2_STR}    RNDMSK V9,0x22', asm, 'RNDMSK Disassembly not correct')
