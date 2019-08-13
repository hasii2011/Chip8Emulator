
from logging import Logger
from logging import getLogger

from test.BaseTest import BaseTest

from org.hasii.chip8.Chip8 import Chip8

from org.hasii.chip8.Chip8RegisterName import Chip8RegisterName
from org.hasii.chip8.Chip8SpriteType import Chip8SpriteType
from org.hasii.chip8.Chip8KeyPadKeys import Chip8KeyPadKeys

from org.hasii.chip8.errors.InvalidIndexRegisterValue import InvalidIndexRegisterValue


class TestChip8(BaseTest):

    MAX_GEN_RAND_LOOP_COUNT: int = 256
    REGISTER_STORE_VALUE:    int = 0xFE
    REGISTER_READ_VALUE:     int = 0xCC
    RANDOM_VALUE:            int = 0xBB
    TEST_STACK_DEPTH:        int = 5

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

    def testRepr(self):

        self.chip8.loadROM("Missile")
        self.chip8.registers.setValue(Chip8RegisterName.V1, Chip8.generateRandomByte())
        self.chip8.registers.setValue(Chip8RegisterName.V3, Chip8.generateRandomByte())
        self.chip8.registers.setValue(Chip8RegisterName.V5, Chip8.generateRandomByte())
        self.chip8.registers.setValue(Chip8RegisterName.V7, Chip8.generateRandomByte())
        self.chip8.registers.setValue(Chip8RegisterName.V9, Chip8.generateRandomByte())
        self.chip8.registers.setValue(Chip8RegisterName.VA, Chip8.generateRandomByte())
        self.chip8.registers.setValue(Chip8RegisterName.VC, Chip8.generateRandomByte())

        self.chip8.indexRegister = Chip8.PROGRAM_START_ADDRESS + 100
        self.chip8.soundTimer    = 0x20
        self.chip8.delayTimer    = 0x40
        for x in range(TestChip8.TEST_STACK_DEPTH):
            self.chip8.stack.push(Chip8.PROGRAM_START_ADDRESS + self.chip8.generateRandomByte())
        self.chip8.fetchInstruction()

        self.logger.info(f'{self.chip8.__repr__()}')

    def testJumpToAddress(self):

        instruction = 0x1219
        self.chip8.emulateSingleCpuCycle(instruction)
        newPc = self.chip8.pc

        self.assertEqual(newPc, 0x219, "Did not do jump")

    def testCallSubroutine(self):
        """
            CALL = 0x2000   # 2nnn;     Call subroutine at location nnn
        """
        self.chip8.pc = Chip8.PROGRAM_START_ADDRESS + 0x100
        self.chip8.stack.empty()

        instruction: int = 0x2200

        self.chip8.emulateSingleCpuCycle(instruction)

        expectedPC: int = 0x200
        actualPC:   int = self.chip8.pc

        self.assertEqual(expectedPC, actualPC, 'Program counter not set to subroutine address')

        expectedStackSize: int = 1
        actualStackSize:   int = self.chip8.stack.size()
        self.assertEqual(expectedStackSize, actualStackSize, 'Stack has been improperly manipulated')

        #
        # The PC is already pointing to the next address when the Call op is executed; That is where we want to return
        #
        expectedTopOfStackValue: int = Chip8.PROGRAM_START_ADDRESS + 0x100 + Chip8.INSTRUCTION_SIZE
        actualTopOfStackValue:   int = self.chip8.stack.peek()
        self.assertEqual(expectedTopOfStackValue, actualTopOfStackValue, 'PC not correctly stored on stack')

    def testSkipBasedOnRegisterEqualToLiteral(self):
        """
        3xkk SE V0, #40;

        """
        instruction = 0x3C0c
        lit = 0x0c

        self.chip8.pc = Chip8.PROGRAM_START_ADDRESS
        self.chip8.registers.setValue(v=Chip8RegisterName.VC, newValue=lit)

        self.chip8.emulateSingleCpuCycle(instruction)
        expectedPC: int = Chip8.PROGRAM_START_ADDRESS + (Chip8.INSTRUCTION_SIZE * 2)

        self.assertEqual(expectedPC, self.chip8.pc, "Did not correctly skip next instruction")

    def testSkipBasedOnRegisterEqualToLiteralFail(self):

        instruction = 0x3C0c
        lit = 0x0c

        self.chip8.pc = Chip8.PROGRAM_START_ADDRESS
        self.chip8.registers.setValue(v=Chip8RegisterName.VC, newValue=lit+1)

        self.chip8.emulateSingleCpuCycle(instruction)
        expectedPC: int = Chip8.PROGRAM_START_ADDRESS + Chip8.INSTRUCTION_SIZE

        self.assertEqual(expectedPC, self.chip8.pc, "incorrectly skipped next instruction")

    def testSkipBasedOnRegisterNotEqualToLiteral(self):

        instruction = 0x4C0c
        lit = 0x0f

        self.chip8.pc = Chip8.PROGRAM_START_ADDRESS
        self.chip8.registers.setValue(v=Chip8RegisterName.VC, newValue=lit+1)

        self.chip8.emulateSingleCpuCycle(instruction)
        expectedPC: int = Chip8.PROGRAM_START_ADDRESS + (Chip8.INSTRUCTION_SIZE * 2)

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
        expectedPC: int = Chip8.PROGRAM_START_ADDRESS + Chip8.INSTRUCTION_SIZE

        self.assertEqual(expectedPC, self.chip8.pc, "Should not skip next instruction")

    def testSkipBasedOnRegisterToRegisterEqual(self):

        instruction = 0x55C0
        self.chip8.pc = Chip8.PROGRAM_START_ADDRESS
        self.chip8.registers.setValue(v=Chip8RegisterName.V5, newValue=0x04)
        self.chip8.registers.setValue(v=Chip8RegisterName.VC, newValue=0x04)

        self.chip8.emulateSingleCpuCycle(instruction)
        expectedPC: int = Chip8.PROGRAM_START_ADDRESS + (Chip8.INSTRUCTION_SIZE * 2)

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
        expectedPC: int = Chip8.PROGRAM_START_ADDRESS + Chip8.INSTRUCTION_SIZE

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

        expectedPC: int = Chip8.PROGRAM_START_ADDRESS + 0xFE + (Chip8.INSTRUCTION_SIZE * 2)

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

        #
        # The PC however does increment to the next instruction, not past it
        #
        expectedPC: int = nonIncrementedAddress + Chip8.INSTRUCTION_SIZE

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

    def testBadLoadIndexRegister(self):

        with self.assertRaises(InvalidIndexRegisterValue):
            self.chip8.setIndexRegister(theNewValue=0xFFFF)

    def testJumpToLocationPlusVZero(self):
        """
        Bnnn; JP V0, addr;    Jump to location nnn + V0       The program counter is set to nnn plus the value of V0
        """
        instruction: int = 0xB123

        self.chip8.pc = Chip8.PROGRAM_START_ADDRESS
        self.chip8.registers.setValue(v=Chip8RegisterName.V0, newValue=0x123)

        self.logger.info(f"pc Before: {self.chip8.pc:X}")

        self.chip8.emulateSingleCpuCycle(instruction)

        self.logger.info(f"pc After: {self.chip8.pc:X}")
        expectedValue: int =  0x123 + 0x123
        actualValue:   int = self.chip8.pc

        self.assertEqual(expectedValue, actualValue, "Program count did not properly increment")

    def testRndByte(self):
        """
        Cxkk; RND Vx, byte;   Set Vx = random byte AND kk

        The Interpreter generates a random number from 0 to 255
        """
        instruction: int = 0xC922

        for x in range(10):
            self.chip8.registers.setValue(Chip8RegisterName.V9, x + 0xF)
            self.chip8.emulateSingleCpuCycle(instruction)
            andedRandomVal: int = self.chip8.registers.getValue(Chip8RegisterName.V9)
            self.logger.info(f"registerVal: {x:X} andedRandomVal: {andedRandomVal}")
            self.assertTrue((andedRandomVal >= 0) and (andedRandomVal <= 255), "rand val not in range")

    def testSetVxToDelayTimer(self):
        """
        # Fx07; LDT Vx, DT;     Set Vx = delay timer value
        """
        instruction: int = 0xF107
        self.chip8.registers.setValue(Chip8RegisterName.V1, 0xFF)
        self.chip8.delayTimer = 0x44

        self.chip8.emulateSingleCpuCycle(instruction)

        expectedValue: int = 0x44
        actualValue:   int = self.chip8.registers.getValue(Chip8RegisterName.V1)

        self.assertEqual(expectedValue, actualValue, f"Load from delay timer failed; Register: V{Chip8RegisterName.V1.value:X}")
        #
        # Test a different register
        #
        newInstruction: int = 0xFA07
        self.chip8.registers.setValue(Chip8RegisterName.VA, 0xCC)
        self.chip8.delayTimer = 0x55

        self.chip8.emulateSingleCpuCycle(newInstruction)

        expectedValue: int = 0x55
        actualValue:   int = self.chip8.registers.getValue(Chip8RegisterName.VA)

        self.assertEqual(expectedValue, actualValue, f"Load from delay timer failed; Register: V{Chip8RegisterName.VA.value:X}")

    def testSetDelayTimerToVx(self):
        """
        Fx15; SDT DT, Vx;     Set delay timer = Vx
        """
        self._runDelayTimerEqualsVxTest(0xF115, Chip8RegisterName.V1, 0x23)
        self._runDelayTimerEqualsVxTest(0xF515, Chip8RegisterName.V5, 0x33)
        self._runDelayTimerEqualsVxTest(0xFA15, Chip8RegisterName.VA, 0x66)

    def testSetSoundTimerToVx(self):
        """
        # Fx18; SST ST, Vx;         Set sound timer = Vx
        """
        self._runSoundTimerEqualsVxTest(0xF918, Chip8RegisterName.V9, 0x32)
        self._runSoundTimerEqualsVxTest(0xF418, Chip8RegisterName.V4, 0x01)
        self._runSoundTimerEqualsVxTest(0xF718, Chip8RegisterName.V7, 0x10)

    def testIncrementIndexRegisterFromVx(self):
        """
        Fx1E; ADDI I, Vx;     Set I = I + Vx
        """
        regName:  Chip8RegisterName = Chip8RegisterName.V0
        incValue:      int = 0x0123
        initIdxRegVal: int = 0x0323
        instruction:   int = 0xF01E

        self.chip8.registers.setValue(v=regName, newValue=incValue)
        self.chip8.indexRegister = initIdxRegVal

        self.chip8.emulateSingleCpuCycle(instruction)

        expectedValue: int = initIdxRegVal + incValue
        actualValue:   int = self.chip8.indexRegister

        self.assertEqual(expectedValue, actualValue, "Index register not correctly incremented")

    def testLoadIndexRegWithLocationOfSprite(self):
        """
        Fx29; LDIS F, Vx;
        Set I = location of sprite for digit Vx.
        """
        self.chip8.indexRegister = 0x0
        regName:     Chip8RegisterName = Chip8RegisterName.VA
        spriteDigit: int               = Chip8SpriteType.SPRITE_B.value
        self.chip8.registers.setValue(v=regName, newValue=spriteDigit)

        instruction: int = 0xFA29

        self.chip8.emulateSingleCpuCycle(instruction)

        expectedValue: int = Chip8.SPRITE_START_ADDRESS + (spriteDigit * Chip8.BYTES_PER_SPRITE)
        actualValue:   int = self.chip8.indexRegister

        self.assertEqual(expectedValue, actualValue, f"Index register does not point to sprite {spriteDigit}")

    def testStoreBCD(self):
        """
        # Fx33; LDB B, Vx;
        Store BCD representation of Vx in memory locations I, I+1, and I+2
        """
        instruction: int = 0xF033
        bcdVal:      int = 128
        memLocation: int = 0x0400

        self.chip8.registers.setValue(Chip8RegisterName.V0, bcdVal)
        self.chip8.indexRegister = memLocation
        self.chip8.emulateSingleCpuCycle(instruction)

        expectedValue1: int = 1
        expectedValue2: int = 2
        expectedValue3: int = 8
        actualValue1:   int = self.chip8.memory[memLocation]
        actualValue2:   int = self.chip8.memory[memLocation + 1]
        actualValue3:   int = self.chip8.memory[memLocation + 2]

        self.assertEqual(expectedValue1, actualValue1, f"bcdValue1 @ 0x{memLocation:X} not incorrectly encoded")
        self.assertEqual(expectedValue2, actualValue2, f"bcdValue2 @ 0x{memLocation+1:X} not incorrectly encoded")
        self.assertEqual(expectedValue3, actualValue3, f"bcdValue3 @ 0x{memLocation+2:X} not incorrectly encoded")

    def testStoreRegisters(self):
        """
        Fx55; STR [I], Vx;
        Store registers V0-Vx in memory starting at location I.
        """
        self._setupRegisters(TestChip8.REGISTER_STORE_VALUE)
        #
        # Set memory we are about to save registers into to some random value
        #
        self._setupMemory(TestChip8.RANDOM_VALUE)

        instruction: int = 0xF355
        self.chip8.emulateSingleCpuCycle(instruction)

        expectedValue: int = TestChip8.REGISTER_STORE_VALUE
        for y in range(0, Chip8RegisterName.V3.value + 1):
            actualValue: int = self.chip8.memory[self.chip8.indexRegister + y]
            self.assertEqual(expectedValue, actualValue, f"Register V{y:X} not correctly stored")

    def testReadRegisters(self):
        """
        Fx65 RDR Vx, [I];
        Read registers V0-Vx from memory starting at location I.
        """
        self._setupRegisters(TestChip8.RANDOM_VALUE)
        self._setupMemory(TestChip8.REGISTER_READ_VALUE)

        instruction: int = 0xF365

        self.chip8.emulateSingleCpuCycle(instruction)

        expectedValue: int = TestChip8.REGISTER_READ_VALUE
        for regName in Chip8RegisterName:
            if regName.value >= Chip8RegisterName.V4.value:
                break
            else:
                actualValue: int = self.chip8.registers.getValue(regName)
                self.assertEqual(expectedValue, actualValue, f"Register V{regName.value:X} did not get set correctly")

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

        self.chip8.delayTimer -= 1
        self.assertEqual(self.chip8.delayTimer, 0, "Should not become negative")

    def testChipSoundTimer(self):

        self.chip8.soundTimer -= 1
        self.assertEqual(self.chip8.soundTimer, 0, "Should not become negative")

    def testLoadROM(self):

        self.logger.info(f"Start load ROM test")

        self.chip8.loadROM("Missile")

    def testGenerateRandomByte(self):

        for x in range(TestChip8.MAX_GEN_RAND_LOOP_COUNT):
            randByte: int = Chip8.generateRandomByte()
            self.logger.info(f"x: {x} randByte: 0x{randByte:2X}")
            self.assertTrue(randByte <= 255, "Too big of a random byte")

    def testLoadSprites(self):

        spriteLen: int = len(Chip8.SPRITE_0)
        startAddress: int = Chip8.SPRITE_START_ADDRESS

        self.chip8._debugPrintMemory(startByteNbr=startAddress, nBytes=(len(Chip8.SPRITES) * spriteLen), bytesPerRow=spriteLen)

        memAddress: int = startAddress
        for spriteByte in Chip8.SPRITE_0:
            expectedValue: int = spriteByte
            actualValue:   int = self.chip8.memory[memAddress]
            self.assertEqual(expectedValue, actualValue, "Sprite not correctly copied")
            memAddress += 1

    def testDrawOnVirtualScreen(self):
        """
        Simplest test.  Load sprite (SPRITE_F) at screen address 0,0

        """

        self.chip8.indexRegister = Chip8.SPRITE_START_ADDRESS + ((Chip8.NUM_SPRITES - 1) * Chip8.BYTES_PER_SPRITE)

        xCoord: int = 0
        yCoord: int = 0
        nBytes: int = len(Chip8.SPRITE_F)
        startAddress: int = self.chip8.indexRegister

        self.chip8.drawOnVirtualScreen(xCoord=xCoord, yCoord=yCoord, nBytes=nBytes)

        self._verifyVirtualDraw(xCoord=xCoord, yCoord=yCoord, startAddress=startAddress, nBytes=nBytes)

    def testDrawOnVirtualScreenCrossColumns(self):
        """
        Slightly more complicated; Draw in middle of screen

        """
        self.chip8.indexRegister = Chip8.SPRITE_START_ADDRESS

        xCoord: int = Chip8.VIRTUAL_WIDTH//2
        yCoord: int  = Chip8.VIRTUAL_HEIGHT // 2
        nBytes: int = len(Chip8.SPRITE_0)

        startAddress: int = self.chip8.indexRegister

        self.chip8.drawOnVirtualScreen(xCoord=xCoord, yCoord=yCoord, nBytes=nBytes)

        self._verifyVirtualDraw(xCoord=xCoord, yCoord=yCoord, startAddress=startAddress, nBytes=nBytes)

    def testDrawOnVirtualScreenWrapRightAxis(self):
        """
        Draw on upper right-hand corner
        """
        xCoord: int = Chip8.VIRTUAL_WIDTH - 2
        yCoord: int = 0
        nBytes: int = len(Chip8.SPRITE_6)

        spriteDigit:        int = Chip8SpriteType.SPRITE_6.value
        spriteStartAddress: int = Chip8.SPRITE_START_ADDRESS + (spriteDigit * Chip8.BYTES_PER_SPRITE)

        self.chip8.indexRegister = spriteStartAddress

        self.chip8.drawOnVirtualScreen(xCoord=xCoord, yCoord=yCoord, nBytes=nBytes)

        self._verifyVirtualDraw(xCoord=xCoord, yCoord=yCoord, startAddress=spriteStartAddress, nBytes=nBytes)

    def testDrawOnVirtualScreenWrapLeftAxis(self):
        pass

    def testDrawOnVirtualScreenWrapOnNorthAxis(self):
        pass

    def testDrawOnVirtualScreenWrapOnSouthAxis(self):
        """
        Draw on the lower left-hand corner
        """
        xCoord: int = 0
        yCoord: int = Chip8.VIRTUAL_HEIGHT - 2
        nBytes: int = len(Chip8.SPRITE_6)
        spriteDigit:        int = Chip8SpriteType.SPRITE_6.value
        spriteStartAddress: int = Chip8.SPRITE_START_ADDRESS + (spriteDigit * Chip8.BYTES_PER_SPRITE)

        self.chip8.indexRegister = spriteStartAddress

        self.chip8.drawOnVirtualScreen(xCoord=xCoord, yCoord=yCoord, nBytes=nBytes)

    def testSkipNextVxDependingOnKeyPressed(self):
        """
        Ex9E; SKP Vx;
        Skip next instruction if key with the value of Vx is pressed
        """
        self.chip8.keypad.keyDown(Chip8KeyPadKeys.C)
        expectedPC: int = self.chip8.PROGRAM_START_ADDRESS + (Chip8.INSTRUCTION_SIZE * 2)

        self._setupAndExecuteKeyPressedTest(expectedPC, 'CPU did not properly increment the PC')

    def testSkipNextVxDependingOnKeyPressedFail(self):
        """
        Ex9E; SKP Vx;
        Skip next instruction if key with the value of Vx is pressed

        Key is not pressed
        """
        self.chip8.keypad.keyUp(Chip8KeyPadKeys.C)
        expectedPC: int = self.chip8.PROGRAM_START_ADDRESS + Chip8.INSTRUCTION_SIZE

        self._setupAndExecuteKeyPressedTest(expectedPC, 'CPU should not increment PC past next instruction')

    def testSkipNextVxDependingOnKeyNotPressed(self):
        """
        ExA1; SKNP Vx;
        Skip next instruction if key with the value of Vx is not pressed
        """
        self.chip8.keypad.keyUp(Chip8KeyPadKeys.A)      # Key is NOT pressed
        expectedPC: int = Chip8.PROGRAM_START_ADDRESS + (Chip8.INSTRUCTION_SIZE * 2)

        self._setupAndExecuteKeyNotPressedTest(expectedPC, 'PC should have skipped next instruction')

    def testSkipNextVxDependingOnKeyNotPressedFail(self):
        self.chip8.keypad.keyDown(Chip8KeyPadKeys.A)      # Key IS pressed
        expectedPC: int = Chip8.PROGRAM_START_ADDRESS + Chip8.INSTRUCTION_SIZE

        self._setupAndExecuteKeyNotPressedTest(expectedPC, 'PC should NOT have skipped next instruction')

    def _setupAndExecuteKeyNotPressedTest(self, expectedPC: int, failureMessage: str):
        instruction: int = 0xEAA1
        self.chip8.pc = self.chip8.PROGRAM_START_ADDRESS
        self.chip8.registers.setValue(v=Chip8RegisterName.VA, newValue=Chip8KeyPadKeys.A.value)

        self.chip8.emulateSingleCpuCycle(instruction)

        actualPC:   int = self.chip8.pc

        self.assertEqual(expectedPC, actualPC, failureMessage)

    def _setupAndExecuteKeyPressedTest(self, expectedPC: int, failureMessage: str):

        self.chip8.pc = self.chip8.PROGRAM_START_ADDRESS
        instruction: int = 0xE99E
        self.chip8.registers.setValue(v=Chip8RegisterName.V9, newValue=Chip8KeyPadKeys.C.value)
        self.chip8.emulateSingleCpuCycle(instruction)
        actualPC:   int = self.chip8.pc

        self.assertEqual(expectedPC, actualPC, failureMessage)

    def _verifyVirtualDraw(self, xCoord: int, yCoord: int, startAddress: int, nBytes: int):

        readY: int = yCoord
        for byteNum in range(nBytes):
            cvRow: Chip8.VIRTUAL_SCREEN_ROW = self.chip8.virtualScreen[readY]
            self.logger.info(f"cvRow: {cvRow}")
            spriteByte: int = self.chip8.memory[startAddress + byteNum]
            self.logger.info(f"spriteByte: {spriteByte:X}")

            readX: int = xCoord
            for bitNum in range(8):
                maskedSpriteBit: int = spriteByte & Chip8.BIT_MASKS[bitNum]
                spriteBit = maskedSpriteBit >> (7 - bitNum)
                if readX > (Chip8.VIRTUAL_WIDTH - 1):
                    readX = 0
                bitFromScreen: int = cvRow[readX]
                readX += 1
                self.assertEqual(bitFromScreen, spriteBit, f"Virtual screen bit {byteNum + bitNum} not set sprite byteNum {byteNum}, ")
            readY += 1

    def _setupRegisters(self, registerValue: int):
        """
        Initializes registers V0-V3
        Args:
            registerValue: Load into registers
        """
        self.chip8.indexRegister = 0x0400
        self.chip8.registers.setValue(Chip8RegisterName.V0, registerValue)
        self.chip8.registers.setValue(Chip8RegisterName.V1, registerValue)
        self.chip8.registers.setValue(Chip8RegisterName.V2, registerValue)
        self.chip8.registers.setValue(Chip8RegisterName.V3, registerValue)

    def _setupMemory(self, memoryValue: int):
        for x in range(0, Chip8RegisterName.V3.value + 1):
            self.chip8.memory[self.chip8.indexRegister + x] = memoryValue

    def _runSoundTimerEqualsVxTest(self, instruction: int, vx: Chip8RegisterName, expectedValue: int):

        self.chip8.registers.setValue(vx, expectedValue)
        self.chip8.soundTimer = 0x22

        self.chip8.emulateSingleCpuCycle(instruction)

        actualValue: int = self.chip8.soundTimer

        self.assertEqual(expectedValue, actualValue, "Delay timer incorrectly set")

    def _runDelayTimerEqualsVxTest(self, instruction: int, vx: Chip8RegisterName, expectedValue: int):

        self.chip8.registers.setValue(vx, expectedValue)
        self.chip8.delayTimer = 0x44

        self.chip8.emulateSingleCpuCycle(instruction)

        actualValue: int = self.chip8.delayTimer

        self.assertEqual(expectedValue, actualValue, "Delay timer incorrectly set")
