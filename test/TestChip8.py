
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

    def testAddToRegisterNoOverflow(self):
        """
        7xkk; ADD Vx, kk;     Adds the value kk to the value of register Vx, then stores the result in Vx

        """
        instruction: int = 0x78BB
        self.chip8.registers.setValue(v=Chip8RegisterName.VF, newValue=0x01)    # Clear carry flag
        self.chip8.registers.setValue(v=Chip8RegisterName.V8, newValue=0x01)    # Init value in register

        self.chip8.emulateSingleCpuCycle(instruction)

        expectedValue:   int = 0xBC
        actualValue:     int = self.chip8.registers.getValue(Chip8RegisterName.V8)
        carryFlagActual: int = self.chip8.registers.getValue(Chip8RegisterName.VF)

        self.assertEqual(expectedValue, actualValue, f"Register V{Chip8RegisterName.V8.value:X} not added to")
        self.assertEqual(0x01, carryFlagActual, f"Carry flag incorrectly cleared")

    def testAddToRegisterWithOverflow(self):

        instruction: int = 0x7801

        self.chip8.registers.setValue(v=Chip8RegisterName.VF, newValue=0x00)    # Clear carry flag
        self.chip8.registers.setValue(v=Chip8RegisterName.V8, newValue=0xFF)    # Init value in register

        self.chip8.emulateSingleCpuCycle(instruction)

        expectedValue:   int = 0x01
        actualValue:     int = self.chip8.registers.getValue(Chip8RegisterName.V8)
        carryFlagActual: int = self.chip8.registers.getValue(Chip8RegisterName.VF)

        self.assertEqual(expectedValue, actualValue, f"Register V{Chip8RegisterName.V8.value:X} not added to")
        self.assertEqual(0x00, carryFlagActual, f"Carry flag incorrectly cleared")

    def testLoadFromRegister(self):
        """
        8xy0; LDR Vx, Vy;     Set Vx = Vy.
        """
        instruction: int = 0x8EA0

        self.chip8.registers.setValue(v=Chip8RegisterName.VE, newValue=0x00)
        self.chip8.registers.setValue(v=Chip8RegisterName.VA, newValue=0xFF)

        self.chip8.emulateSingleCpuCycle(instruction)

        expectedValue: int = 0xFF
        actualValue:   int = self.chip8.registers.getValue(Chip8RegisterName.VE)

        self.assertEqual(expectedValue, actualValue,
                         f"Register V{Chip8RegisterName.VE.value:X} not set to value from V{Chip8RegisterName.VA.value:X}")

    def testRegisterToRegisterOR(self):
        """
        8xy1; OR Vx, Vy;      Set Vx = Vx OR Vy
        """
        instruction: int = 0x8C41

        self.chip8.registers.setValue(v=Chip8RegisterName.VC, newValue=0xAA)    # 10101010
        self.chip8.registers.setValue(v=Chip8RegisterName.V4, newValue=0x23)    # 00100011

        self.chip8.emulateSingleCpuCycle(instruction)

        expectedValue: int = 0xAB                                               # 10101011
        actualValue:   int = self.chip8.registers.getValue(Chip8RegisterName.VC)

        self.assertEqual(expectedValue, actualValue, f"Register V{Chip8RegisterName.VC.value:X} not correctly OR'ed")

    def testRegisterToRegisterAnd(self):
        """
        8xy2; AND Vx, Vy;     Set Vx = Vx AND Vy
        """
        instruction: int = 0x8C42

        self.chip8.registers.setValue(v=Chip8RegisterName.VC, newValue=0xAA)    # 1010 1010
        self.chip8.registers.setValue(v=Chip8RegisterName.V4, newValue=0x23)    # 0010 0011

        self.chip8.emulateSingleCpuCycle(instruction)

        expectedValue: int = 0x22                                               # 0010 0010
        actualValue:   int = self.chip8.registers.getValue(Chip8RegisterName.VC)

        self.assertEqual(expectedValue, actualValue, f"Register V{Chip8RegisterName.VC.value:X} not correctly AND'ed")

    def testRegisterToRegisterXor(self):
        """
        8xy3; XOR Vx, Vy;     Set Vx = Vx XOR Vy
        """
        instruction: int = 0x8C43

        self.chip8.registers.setValue(v=Chip8RegisterName.VC, newValue=0xAA)    # 1010 1010
        self.chip8.registers.setValue(v=Chip8RegisterName.V4, newValue=0x23)    # 0010 0011

        self.chip8.emulateSingleCpuCycle(instruction)

        expectedValue: int = 0x89                                               # 1000 1000
        actualValue:   int = self.chip8.registers.getValue(Chip8RegisterName.VC)

        self.assertEqual(expectedValue, actualValue, f"Register V{Chip8RegisterName.VC.value:X} not correctly XOR'ed")

    def testBasicRegisterToRegisterAdd(self):
        """
        Already tested by TestChip8Registers.testBasicRegisterToRegisterAdd
        """
        pass

    def testOverflowRegisterToRegisterAdd(self):
        """
        Already tested by TestChip8Registers.testOverflowRegisterToRegisterAdd
        """
        pass

    def testBasicRegisterToRegisterSubtract(self):
        """
        Already tested by TestChip8Registers.testBasicRegisterToRegisterSubtract
        """
        pass

    def testBorrowRegisterToRegisterSubtract(self):
        """
        Already tested by TestChip8Registers.testBorrowRegisterToRegisterSubtract
        """
        pass

    def testSubRegisterVyFromRegisterVx(self):
        """
        Already tested by TestChip8Registers.testSubRegisterVyFromRegisterVx
        """
        pass

    def testBorrowSubRegisterVyFromRegisterVx(self):
        """
        Already tested by TestChip8Registers.testBorrowSubRegisterVyFromRegisterVx
        """
        pass

    def testRegisterShiftRight(self):
        """
        Already tested by TestChip8Registers.testShiftRightOp
        """
        pass

    def testRegisterShiftLeft(self):
        """
        Already test by TestChip8Registers.testShiftLeftOp
        """
        pass

    def testSkipIfRegisterNotEqualToRegister(self):
        """
        9xy0; SNER Vx, Vy;    Skip next instruction if Vx != Vy
        """
        instruction: int = 0x9670
        self.chip8.pc = Chip8.PROGRAM_START_ADDRESS + 0xFE

        self.logger.info(f"pc Before: {self.chip8.pc:X}")
        self.chip8.registers.setValue(v=Chip8RegisterName.V6, newValue=0xCC)
        self.chip8.registers.setValue(v=Chip8RegisterName.V7, newValue=0x42)

        self.chip8.emulateSingleCpuCycle(instruction)

        expectedPC: int = Chip8.PROGRAM_START_ADDRESS + 0xFE + Chip8.INSTRUCTION_SIZE

        self.logger.info(f"pc After: {self.chip8.pc:X}")

        self.assertEqual(expectedPC, self.chip8.pc, "Should skip next instruction")

    def testSkipIfRegisterNotEqualToRegisterFailSkip(self):
        instruction: int = 0x9670
        nonIncrementedAddress: int = Chip8.PROGRAM_START_ADDRESS + 0xFE
        self.chip8.pc = nonIncrementedAddress

        self.logger.info(f"pc Before: {self.chip8.pc:X}")
        self.chip8.registers.setValue(v=Chip8RegisterName.V6, newValue=0x42)    # They are
        self.chip8.registers.setValue(v=Chip8RegisterName.V7, newValue=0x42)    # the same

        self.chip8.emulateSingleCpuCycle(instruction)

        expectedPC: int = nonIncrementedAddress

        self.logger.info(f"pc After: {self.chip8.pc:X}")

        self.assertEqual(expectedPC, self.chip8.pc, "Should not skip next instruction")

    def testLoadIndexRegister(self):
        """
        # Annn; LDI I, addr;    Set I = nnn; The value of register I is set to nnn
        """
        instruction: int = 0xA046
        self.chip8.indexRegister = 0x0FFF

        self.chip8.emulateSingleCpuCycle(instruction)

        expectedIndexRegisterValue: int = 0x0046
        actualValue:                int = self.chip8.indexRegister

        self.assertEqual(expectedIndexRegisterValue, actualValue, "Index register not correctly set")


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
