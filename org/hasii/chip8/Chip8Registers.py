
from logging import Logger
from logging import getLogger

from org.hasii.chip8.Chip8RegisterName import Chip8RegisterName


class Chip8Registers:

    MSB_MASK:  int = 0x80
    LSB_MASK:  int = 0x01

    CARRY_BIT:    int = 0x01
    NO_CARRY_BIT: int = 0x00

    def __init__(self):

        self.logger: Logger = getLogger(__name__)

        self.registers = {

            Chip8RegisterName.V0: 0x0,
            Chip8RegisterName.V1: 0x0,
            Chip8RegisterName.V2: 0x0,
            Chip8RegisterName.V3: 0x0,
            Chip8RegisterName.V4: 0x0,
            Chip8RegisterName.V5: 0x0,
            Chip8RegisterName.V6: 0x0,
            Chip8RegisterName.V7: 0x0,
            Chip8RegisterName.V8: 0x0,
            Chip8RegisterName.V9: 0x0,
            Chip8RegisterName.VA: 0x0,
            Chip8RegisterName.VB: 0x0,
            Chip8RegisterName.VC: 0x0,
            Chip8RegisterName.VD: 0x0,
            Chip8RegisterName.VE: 0x0,
            Chip8RegisterName.VF: 0x0
        }

    def setValue(self, v: Chip8RegisterName, newValue: int):
        self.registers[v] = newValue

    def getValue(self, v: Chip8RegisterName) -> int:
        return self.registers[v]

    def andOp(self, v: Chip8RegisterName, mask: int):
        self.registers[v] = self.registers[v] & mask

    def orOp(self, v: Chip8RegisterName, mask: int):
        self.registers[v] = self.registers[v] | mask

    def xorOp(self, v: Chip8RegisterName, mask: int):
        self.registers[v] = self.registers[v] ^ mask

    def notOp(self, v: Chip8RegisterName):
        self.registers[v] = ~self.registers[v]

    def shiftLeft(self, v: Chip8RegisterName, numBitsToShift: int):
        """
        Stores most significant bit of Vx in VF; shifts Vx to the left by 1

        Args:
            v:
            numBitsToShift:
        """
        self.registers[Chip8RegisterName.VF] = (self.registers[v] & Chip8Registers.MSB_MASK) >> 7
        self.registers[v] = self.registers[v] << numBitsToShift

    def shiftRight(self, v: Chip8RegisterName, numBitsToShift: int):
        """
        Store least significant bit of Vx in VF; shifts Vx to the right by 1
        Args:
            v:
            numBitsToShift:
        """
        self.registers[Chip8RegisterName.VF] = (self.registers[v] & Chip8Registers.LSB_MASK)
        self.registers[v] = self.registers[v] >> numBitsToShift

    def addRegisterToRegister(self, vx: Chip8RegisterName, vy: Chip8RegisterName):
        """
        8xy4; ADD Vx, Vy;     Set Vx = Vx + Vy
        VF is set to 1 when there is a carry, and to 0 when there is not

        Args:
            vx:  Source register
            vy:  Register with value to add

        """
        src: int = self.registers[vx]
        val: int = self.registers[vy]
        tempReg: int = src + val

        if tempReg > 255:
            self.registers[Chip8RegisterName.VF] = Chip8Registers.CARRY_BIT
            self.registers[vx] = tempReg - 255
        else:
            self.registers[Chip8RegisterName.VF] = Chip8Registers.NO_CARRY_BIT
            self.registers[vx] = tempReg

    def __repr__(self):

        strMe: str = ""

        for v in Chip8RegisterName:
            strMe += f"{v.name}:0x{self.registers[v]:x} "
        return strMe
