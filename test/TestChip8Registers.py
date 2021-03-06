
from logging import Logger
from logging import getLogger

from test.BaseTest import BaseTest

from org.hasii.chip8.Chip8Registers import Chip8Registers
from org.hasii.chip8.Chip8RegisterName import Chip8RegisterName

KNOWN_VALUE:          int = 0x23
KNOWN_LARGE_VALUE:    int = 0xFF
KNOWN_SMALL_VALUE:    int = 0x00
VALUE_WITH_KNOWN_MSB: int = 0xF0
VALUE_WITH_KNOWN_LSB: int = 0x0F

KNOWN_CAUSE_OVERFLOW_LEFT_OVER: int = 0x20
KNOWN_NON_BOUNDARY_VALUE:       int = 0xD0

MISSILE_VALUE_TO_SUBTRACT: int = 3
MISSILE_KNOWN_SMALL_VALUE: int = 2

LOGICAL_OP_MASK:    int = 0xF0
BITS_TO_SHIFT:      int = 1
VALUE_TO_ADD:       int = 1
VALUE_TO_SUBTRACT:  int = 3

EXPECTED_AND_VALUE: int = 0x20
EXPECTED_OR_VALUE:  int = 0xF3
EXPECTED_XOR_VALUE: int = 0xD3
EXPECTED_SHL_VALUE: int = 0x46
EXPECTED_SHR_VALUE: int = 0x11

EXPECTED_OVERFLOW_ADD_VALUE: int = 0x00
EXPECTED_OVERFLOW_LEFT_OVER: int = KNOWN_CAUSE_OVERFLOW_LEFT_OVER - 1

EXPECTED_OVERFLOW_NON_BOUNDARY_LEFT_OVER: int = 0xA0


class TestChip8Registers(BaseTest):

    clsLogger: Logger = None

    @classmethod
    def setUpClass(cls):
        """"""
        BaseTest.setUpLogging()
        TestChip8Registers.clsLogger = getLogger(__name__)

    def setUp(self):
        """"""
        self.logger:    Logger         = TestChip8Registers.clsLogger
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
        self.logger.info(f'Original {Chip8RegisterName.V5.name} value,  {self.registers[Chip8RegisterName.V5]}')

        self.registers.shiftLeft(v=Chip8RegisterName.V5, numBitsToShift=BITS_TO_SHIFT)

        self.logger.info(f"Shifted binary value: {self.registers.getValue(Chip8RegisterName.V5):b}")
        self.logger.info(f"Flag Register: {self.registers.getValue(Chip8RegisterName.VF):b}")

        self.assertEqual(0x0001, self.registers.getValue(Chip8RegisterName.VF), "Flag register not set")

        self.logger.info(f'New {Chip8RegisterName.V5.name} value,  {self.registers[Chip8RegisterName.V5]}')

    def testShiftRightLSBStore(self):
        self.registers.setValue(v=Chip8RegisterName.V4, newValue=VALUE_WITH_KNOWN_LSB)
        self.logger.info(f"Binary value to shift left: {self.registers.getValue(Chip8RegisterName.V4):b}")

        self.registers.shiftRight(v=Chip8RegisterName.V4, numBitsToShift=BITS_TO_SHIFT)
        self.logger.info(f"Shifted binary value: {self.registers.getValue(Chip8RegisterName.V4):b}")
        self.logger.info(f"Flag Register: {self.registers.getValue(Chip8RegisterName.VF):b}")

        self.assertEqual(0x0001, self.registers.getValue(Chip8RegisterName.VF), "Flag register not set")

    def testBasicRegisterToRegisterAdd(self):

        self.registers.setValue(Chip8RegisterName.V7, KNOWN_VALUE)
        self.registers.setValue(Chip8RegisterName.V8, VALUE_TO_ADD)
        #
        # Clear the flag register
        self.registers.setValue(Chip8RegisterName.VF, 0)

        self.registers.addRegisterToRegister(vx=Chip8RegisterName.V7, vy=Chip8RegisterName.V8)

        expectedValue: int = KNOWN_VALUE + VALUE_TO_ADD
        actualValue:   int = self.registers.getValue(Chip8RegisterName.V7)

        self.assertEqual(expectedValue, actualValue, "Register to register add did not work")
        self.assertEqual(Chip8Registers.NO_CARRY_BIT, self.registers.getValue(Chip8RegisterName.VF), "Flag register should not overflow")

    def testOverflowRegisterToRegisterAdd(self):

        self.registers.setValue(Chip8RegisterName.V7, KNOWN_LARGE_VALUE)
        self.registers.setValue(Chip8RegisterName.V8, VALUE_TO_ADD)

        self.registers.addRegisterToRegister(vx=Chip8RegisterName.V7, vy=Chip8RegisterName.V8)
        actualValue: int = self.registers.getValue(Chip8RegisterName.V7)

        self.assertEqual(EXPECTED_OVERFLOW_ADD_VALUE, actualValue, "Register to register overflow add did not work")
        self.assertEqual(Chip8Registers.CARRY_BIT, self.registers.getValue(Chip8RegisterName.VF), "Flag register overflow")

    def testOverflowRegisterToRegisterAddKeepingLowest8Bits(self):

        self.registers[Chip8RegisterName.VA] = KNOWN_LARGE_VALUE
        self.registers[Chip8RegisterName.VC] = KNOWN_CAUSE_OVERFLOW_LEFT_OVER
        self.registers.addRegisterToRegister(vx=Chip8RegisterName.VA, vy=Chip8RegisterName.VC)

        actualValue: int = self.registers.getValue(Chip8RegisterName.VA)

        self.assertEqual(EXPECTED_OVERFLOW_LEFT_OVER, actualValue, "Register to register bpundar overflow add did not work")
        self.assertEqual(Chip8Registers.CARRY_BIT, self.registers.getValue(Chip8RegisterName.VF), "Flag register overflow")

    def testOverflowRegisterToRegisterAddKeepingLowest8BitsNonBoundaryVxValue(self):
        self.registers[Chip8RegisterName.V3] = KNOWN_NON_BOUNDARY_VALUE
        self.registers[Chip8RegisterName.V9] = KNOWN_NON_BOUNDARY_VALUE

        self.registers.addRegisterToRegister(vx=Chip8RegisterName.V3, vy=Chip8RegisterName.V9)

        actualValue: int = self.registers.getValue(Chip8RegisterName.V3)
        self.assertEqual(EXPECTED_OVERFLOW_NON_BOUNDARY_LEFT_OVER, actualValue, "Register to register non-boundary overflow add did not work")
        self.assertEqual(Chip8Registers.CARRY_BIT, self.registers.getValue(Chip8RegisterName.VF), "Flag register overflow")

    def testBasicRegisterToRegisterSubtract(self):

        self.registers.setValue(Chip8RegisterName.V7, KNOWN_VALUE)
        self.registers.setValue(Chip8RegisterName.V8, VALUE_TO_SUBTRACT)

        self.registers.setValue(Chip8RegisterName.VF, 0)    # Clear the flag register

        self.registers.subRegisterToRegister(vx=Chip8RegisterName.V7, vy=Chip8RegisterName.V8)

        expectedValue: int = KNOWN_VALUE - VALUE_TO_SUBTRACT
        actualValue:   int = self.registers.getValue(Chip8RegisterName.V7)

        self.assertEqual(expectedValue, actualValue, "Register to register subtract did not work")
        self.assertEqual(Chip8Registers.NO_BORROW_BIT, self.registers.getValue(Chip8RegisterName.VF), "Flag register incorrect")

    def testBorrowRegisterToRegisterSubtract(self):

        self.registers.setValue(Chip8RegisterName.VA, KNOWN_SMALL_VALUE)
        self.registers.setValue(Chip8RegisterName.VB, VALUE_TO_SUBTRACT)

        self.registers.setValue(Chip8RegisterName.VF, 0)    # Clear the flag register

        self.registers.subRegisterToRegister(vx=Chip8RegisterName.VA, vy=Chip8RegisterName.VB)

        expectedValue: int = 0xFD
        actualValue:   int = self.registers.getValue(Chip8RegisterName.VA)

        self.assertEqual(expectedValue, actualValue, "Register to register borrow subtract did not work")

        self.assertEqual(Chip8Registers.BORROW_BIT, self.registers.getValue(Chip8RegisterName.VF), "Flag register incorrect")

    def testSubtractRegisterVyFromRegisterVx(self):

        self.registers.setValue(Chip8RegisterName.V7, VALUE_TO_SUBTRACT)
        self.registers.setValue(Chip8RegisterName.V8, KNOWN_VALUE)

        self.registers.setValue(Chip8RegisterName.VF, 0)    # Clear the flag register

        self.registers.subRegisterVyFromRegisterVx(vx=Chip8RegisterName.V7, vy=Chip8RegisterName.V8)

        expectedValue: int = KNOWN_VALUE - VALUE_TO_SUBTRACT
        actualValue:   int = self.registers.getValue(Chip8RegisterName.V7)

        self.assertEqual(expectedValue, actualValue, "Register to register subtract did not work")
        self.assertEqual(Chip8Registers.BORROW_BIT, self.registers.getValue(Chip8RegisterName.VF), "Flag register incorrect")

    def testBorrowSubtractRegisterVyFromRegisterVx(self):

        self.registers.setValue(Chip8RegisterName.V2, VALUE_TO_SUBTRACT)
        self.registers.setValue(Chip8RegisterName.V3, KNOWN_LARGE_VALUE)

        self.registers.setValue(Chip8RegisterName.VF, 0)    # Clear the flag register

        self.registers.subRegisterVyFromRegisterVx(vx=Chip8RegisterName.V2, vy=Chip8RegisterName.V3)

        expectedValue: int = 0xFC
        actualValue:   int = self.registers.getValue(Chip8RegisterName.V2)

        self.assertEqual(expectedValue, actualValue, "Register to register borrow subtract did not work")

        self.assertEqual(Chip8Registers.BORROW_BIT, self.registers.getValue(Chip8RegisterName.VF), "Flag register incorrect")

    def testBorrowSubtractRegisterV0MissileBug(self):
        """
        Attempt to replicate Missile ROM error where V0 decrements past 0
        """
        self.registers.setValue(Chip8RegisterName.V0, MISSILE_KNOWN_SMALL_VALUE)
        self.registers.setValue(Chip8RegisterName.V2, MISSILE_VALUE_TO_SUBTRACT)

        self.registers.setValue(Chip8RegisterName.VF, 0)    # Clear the flag register

        self.registers.subRegisterToRegister(vx=Chip8RegisterName.V0, vy=Chip8RegisterName.V2)

        expectedValue: int = 0xFF
        actualValue:   int = self.registers.getValue(Chip8RegisterName.V0)

        self.assertEqual(expectedValue, actualValue, "Register to register borrow subtract did not work")
        self.assertEqual(Chip8Registers.BORROW_BIT, self.registers.getValue(Chip8RegisterName.VF), "Flag register incorrect")

    def testScTestOneMinusOne(self):
        """
        ERROR 6
        After subtraction 1-1 register VF must be 1, but is still 0.

        """
        self.registers.setValue(Chip8RegisterName.V7, 1)
        self.registers.setValue(Chip8RegisterName.V8, 1)

        self.registers.setValue(Chip8RegisterName.VF, 0)    # Clear the flag register

        self.registers.subRegisterToRegister(vx=Chip8RegisterName.V7, vy=Chip8RegisterName.V8)

        expectedValue: int = 0
        actualValue:   int = self.registers.getValue(Chip8RegisterName.V7)

        self.assertEqual(expectedValue, actualValue, "Register to register subtract did not work")
        self.assertEqual(Chip8Registers.NO_BORROW_BIT, self.registers.getValue(Chip8RegisterName.VF), "Flag register incorrect")
