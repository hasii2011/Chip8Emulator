
from logging import Logger
from logging import getLogger

from test.BaseTest import BaseTest

from org.hasii.chip8.Chip8 import Chip8


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
