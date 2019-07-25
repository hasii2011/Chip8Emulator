
from logging import Logger
from logging import getLogger

from test.BaseTest import BaseTest

from org.hasii.chip8.Chip8 import Chip8
from org.hasii.chip8.Chip8RegisterName import Chip8RegisterName


class TestChip8(BaseTest):

    clsLogger: Logger = None

    @classmethod
    def setUpClass(cls):
        """"""
        BaseTest.setUpLogging()
        TestChip8.clsLogger = getLogger(__name__)

    def setUp(self):
        """"""
        self.chip8:  Chip8  = Chip8()
        self.logger: Logger = TestChip8.clsLogger

    def testJumpToAddress(self):

        instruction = 0x1219
        self.chip8.emulateSingleCpuCycle(instruction)
        newPc = self.chip8.pc

        self.assertEqual(newPc, 0x219, "Did not do jump")

    def testSkipBasedOnRegisterEqualToLiteral(self):
        """
        3xkk SE V0, #40;

        """
        instruction = 0x3C0c
        lit = 0x0c

        self.chip8.pc = Chip8.PROGRAM_START_ADDRESS
        self.chip8.registers.setValue(v=Chip8RegisterName.VC, newValue=lit)

        self.chip8.emulateSingleCpuCycle(instruction)
        expectedPC: int = Chip8.PROGRAM_START_ADDRESS + Chip8.INSTRUCTION_SIZE

        self.assertEqual(expectedPC, self.chip8.pc, "Did not correctly skip next instruction")

    def testSkipBasedOnRegisterEqualToLiteralFail(self):

        instruction = 0x3C0c
        lit = 0x0c

        self.chip8.pc = Chip8.PROGRAM_START_ADDRESS
        self.chip8.registers.setValue(v=Chip8RegisterName.VC, newValue=lit+1)

        self.chip8.emulateSingleCpuCycle(instruction)
        expectedPC: int = Chip8.PROGRAM_START_ADDRESS

        self.assertEqual(expectedPC, self.chip8.pc, "incorrectly skipped next instruction")

    def testSkipBasedOnRegisterNotEqualToLiteral(self):

        instruction = 0x4C0c
        lit = 0x0f

        self.chip8.pc = Chip8.PROGRAM_START_ADDRESS
        self.chip8.registers.setValue(v=Chip8RegisterName.VC, newValue=lit+1)

        self.chip8.emulateSingleCpuCycle(instruction)
        expectedPC: int = Chip8.PROGRAM_START_ADDRESS + Chip8.INSTRUCTION_SIZE

        self.assertEqual(expectedPC, self.chip8.pc, "Did not skip next instruction")

    def testSkipBasedOnRegisterNotEqualToLiteralFail(self):
        """
        The register and literal are equal;  Should not skip
        """
        instruction = 0x4C0c
        lit = 0x0c

        self.chip8.pc = Chip8.PROGRAM_START_ADDRESS
        self.chip8.registers.setValue(v=Chip8RegisterName.VC, newValue=lit)

        self.chip8.emulateSingleCpuCycle(instruction)
        expectedPC: int = Chip8.PROGRAM_START_ADDRESS

        self.assertEqual(expectedPC, self.chip8.pc, "Should not skip next instruction")

    def testSkipBasedOnRegisterToRegisterEqual(self):

        instruction = 0x55C0
        self.chip8.pc = Chip8.PROGRAM_START_ADDRESS
        self.chip8.registers.setValue(v=Chip8RegisterName.V5, newValue=0x04)
        self.chip8.registers.setValue(v=Chip8RegisterName.VC, newValue=0x04)

        self.chip8.emulateSingleCpuCycle(instruction)
        expectedPC: int = Chip8.PROGRAM_START_ADDRESS + Chip8.INSTRUCTION_SIZE

        self.assertEqual(expectedPC, self.chip8.pc, "Should skip next instruction")

    def testSkipBasedOnRegisterToRegisterEqualFail(self):
        """
            V5 != VC
        """
        instruction = 0x55C0
        self.chip8.pc = Chip8.PROGRAM_START_ADDRESS
        self.chip8.registers.setValue(v=Chip8RegisterName.V5, newValue=0x04)
        self.chip8.registers.setValue(v=Chip8RegisterName.VC, newValue=0x0F)

        self.chip8.emulateSingleCpuCycle(instruction)
        expectedPC: int = Chip8.PROGRAM_START_ADDRESS

        self.assertEqual(expectedPC, self.chip8.pc, "Should not skip next instruction")

    def testLoadRegisterWithLiteral(self):
        """
        6xkk; LDL Vx, kk
        """
        instruction: int = 0x6ABB
        self.chip8.registers.setValue(v=Chip8RegisterName.V6, newValue=0x04)
        self.chip8.emulateSingleCpuCycle(instruction)

        expectedValue: int = 0xBB
        actualValue:   int = self.chip8.registers.getValue(Chip8RegisterName.VA)
        self.assertEqual(expectedValue, actualValue, f"Register V{Chip8RegisterName.VA.value:X} not set")

    def testChipInitialization(self):

        self.assertEqual(self.chip8.pc, Chip8.PROGRAM_START_ADDRESS, "Initial Program Counter is bad")
        self.logger.info(f"Program counter correctly initialized")
        self.assertEqual(self.chip8.delayTimer, 0, "Delay timer should start at zero")
        self.logger.info(f"Delay timer correctly initialized")
        self.assertEqual(self.chip8.soundTimer, 0, "Sound timer should start at zero")
        self.logger.info(f"Sound timer correctly initialized")
        self.assertEqual(self.chip8.stack.size(), 0, "Stack has stuff on it")
        self.logger.info(f"Stack correctly initialized")

    def testChipDelayTimer(self):

        self.chip8.delayTimer += 1
        self.assertEqual(self.chip8.delayTimer, 0, "Should not become negative")

    def testChipSoundTimer(self):

        self.chip8.soundTimer += 1
        self.assertEqual(self.chip8.soundTimer, 0, "Should not become negative")

    def testLoadROM(self):

        self.logger.info(f"Start load ROM test")

        self.chip8.loadROM("Missile")
