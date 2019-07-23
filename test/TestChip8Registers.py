
from logging import Logger
from logging import getLogger

from test.BaseTest import BaseTest

from org.hasii.chip8.Chip8Registers import Chip8Registers
from org.hasii.chip8.Chip8RegisterName import Chip8RegisterName

KNOWN_VALUE:          int = 0x0023
VALUE_WITH_KNOWN_MSB: int = 0xF000
VALUE_WITH_KNOWN_LSB: int = 0x000F

LOGICAL_OP_MASK:    int = 0x00F0
BITS_TO_SHIFT:      int = 1
EXPECTED_AND_VALUE: int = 0x0020
EXPECTED_OR_VALUE:  int = 0x00F3
EXPECTED_XOR_VALUE: int = 0x00D3
EXPECTED_SHL_VALUE: int = 0x0046
EXPECTED_SHR_VALUE: int = 0x0011


class TestChipRegisters(BaseTest):

    clsLogger: Logger = None

    @classmethod
    def setUpClass(cls):
        """"""
        BaseTest.setUpLogging()
        TestChipRegisters.clsLogger = getLogger(__name__)

    def setUp(self):
        """"""
        self.logger:    Logger         = TestChipRegisters.clsLogger
        self.registers: Chip8Registers = Chip8Registers()

    def testRegisterSet(self):

        self.registers.setValue(v=Chip8RegisterName.V0, newValue=KNOWN_VALUE)

        newValue =  self.registers.getValue(v=Chip8RegisterName.V0)

        self.assertEqual(KNOWN_VALUE, newValue, "Register sets not working")

        self.logger.info(f"Register dump: {self.registers}")

    def testAndOp(self):
        self.registers.setValue(v=Chip8RegisterName.V7, newValue=KNOWN_VALUE)
        self.registers.andOp(v=Chip8RegisterName.V7, mask=LOGICAL_OP_MASK)
        self.assertEqual(EXPECTED_AND_VALUE, self.registers.getValue(Chip8RegisterName.V7), "And does not appear to work")

    def testOrOp(self):
        self.registers.setValue(v=Chip8RegisterName.VA, newValue=KNOWN_VALUE)
        self.registers.orOp(v=Chip8RegisterName.VA, mask=LOGICAL_OP_MASK)
        self.assertEqual(EXPECTED_OR_VALUE, self.registers.getValue(Chip8RegisterName.VA), "Or op does not appear to work")

    def testXorOp(self):
        self.registers.setValue(v=Chip8RegisterName.VE, newValue=KNOWN_VALUE)
        self.registers.xorOp(v=Chip8RegisterName.VE, mask=LOGICAL_OP_MASK)
        self.assertEqual(EXPECTED_XOR_VALUE, self.registers.getValue(Chip8RegisterName.VE), "Xor op does not appear to work")

    def testShiftLeftOp(self):
        self.registers.setValue(v=Chip8RegisterName.V2, newValue=KNOWN_VALUE)
        self.registers.shiftLeft(v=Chip8RegisterName.V2, numBitsToShift=BITS_TO_SHIFT)
        self.assertEqual(EXPECTED_SHL_VALUE, self.registers.getValue(Chip8RegisterName.V2), "Shift left is not working")

    def testShiftRightOp(self):
        self.registers.setValue(v=Chip8RegisterName.V5, newValue=KNOWN_VALUE)
        self.logger.info(f"Binary value to shift right: {self.registers.getValue(Chip8RegisterName.V5):b}")

        self.registers.shiftRight(v=Chip8RegisterName.V5, numBitsToShift=BITS_TO_SHIFT)
        self.logger.info(f"Shifted binary value: {self.registers.getValue(Chip8RegisterName.V5):b}")

        self.assertEqual(EXPECTED_SHR_VALUE, self.registers.getValue(Chip8RegisterName.V5), "Shift right is not working")

    def testShiftLeftMSBStore(self):

        self.registers.setValue(v=Chip8RegisterName.V5, newValue=VALUE_WITH_KNOWN_MSB)
        self.logger.info(f"Binary value to shift left: {self.registers.getValue(Chip8RegisterName.V5):b}")
        self.registers.shiftLeft(v=Chip8RegisterName.V5, numBitsToShift=BITS_TO_SHIFT)
        self.logger.info(f"Shifted binary value: {self.registers.getValue(Chip8RegisterName.V5):b}")

        self.logger.info(f"Flag Register: {self.registers.getValue(Chip8RegisterName.VF):b}")

        self.assertEqual(0x0001, self.registers.getValue(Chip8RegisterName.VF), "Flag register not set")

    def testShiftRightLSBStore(self):
        self.registers.setValue(v=Chip8RegisterName.V4, newValue=VALUE_WITH_KNOWN_LSB)
        self.logger.info(f"Binary value to shift left: {self.registers.getValue(Chip8RegisterName.V4):b}")

        self.registers.shiftRight(v=Chip8RegisterName.V4, numBitsToShift=BITS_TO_SHIFT)
        self.logger.info(f"Shifted binary value: {self.registers.getValue(Chip8RegisterName.V4):b}")
        self.logger.info(f"Flag Register: {self.registers.getValue(Chip8RegisterName.VF):b}")

        self.assertEqual(0x0001, self.registers.getValue(Chip8RegisterName.VF), "Flag register not set")

