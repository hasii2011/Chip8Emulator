

import unittest
from unittest.suite import TestSuite
from unittest import TestLoader

from test.TestChip8Registers import TestChip8Registers
from test.TestChip8 import TestChip8
from test.TestChip8Disassembler import TestChip8Disassembler
from test.TestChip8InstructionList import TestChip8InstructionList
from test.TestChip8KeyPad import TestChip8KeyPad
from test.TestChip8Stack import TestChip8Stack


def suite() -> TestSuite:

    testLoader: TestLoader = unittest.TestLoader()
    fSuite: TestSuite = unittest.TestSuite()

    fSuite.addTest(testLoader.loadTestsFromTestCase(TestChip8))
    fSuite.addTest(testLoader.loadTestsFromTestCase(TestChip8Disassembler))
    fSuite.addTest(testLoader.loadTestsFromTestCase(TestChip8InstructionList))
    fSuite.addTest(testLoader.loadTestsFromTestCase(TestChip8KeyPad))
    fSuite.addTest(testLoader.loadTestsFromTestCase(TestChip8Registers))
    fSuite.addTest(testLoader.loadTestsFromTestCase(TestChip8Stack))

    return fSuite


def main():

    testSuite: TestSuite = suite()
    unittest.TextTestRunner().run(testSuite)


if __name__ == "__main__":
    main()
