
from typing import Dict
from typing import Callable

from logging import Logger
from logging import getLogger

from org.hasii.chip8.Chip8 import Chip8
from org.hasii.chip8.Chip8Mnemonics import Chip8Mnemonics
from org.hasii.chip8.Chip8RegisterName import Chip8RegisterName
from org.hasii.chip8.Chip8Decoder import Chip8Decoder

from org.hasii.chip8.errors.UnknownInstructionError import UnknownInstructionError


class Chip8Disassembler(Chip8Decoder):

    def __init__(self):

        super().__init__()
        self.logger: Logger = getLogger(__name__)

        self.pc:          int = 0x0000

        self.opCodeMethods: Dict[int, Callable] = {

            Chip8Mnemonics.RTS.value:  self.returnFromSubroutine,
            Chip8Mnemonics.CLS.value:  self.clearScreen,
            Chip8Mnemonics.JUMP.value: self.jumpToAddress,
            Chip8Mnemonics.CALL.value: self.callSubroutine,
            Chip8Mnemonics.SEL.value:  self.skipIfRegisterEqualToLiteral,
            Chip8Mnemonics.SNEL.value: self.skipIfRegisterNotEqualToLiteral,
            Chip8Mnemonics.SER.value:  self.skipIfRegisterEqualToRegister,
            Chip8Mnemonics.LDL.value:  self.loadRegisterWithLiteral,
            Chip8Mnemonics.ADD.value:  self.addLiteralToRegister,
            Chip8Mnemonics.MOV.value:  self.registerToRegisterInstructions,
            Chip8Mnemonics.OR.value:   self.registerToRegisterInstructions,
            Chip8Mnemonics.AND.value:  self.registerToRegisterInstructions,
            Chip8Mnemonics.ADDR.value: self.registerToRegisterInstructions,
            Chip8Mnemonics.SUB.value:  self.registerToRegisterInstructions,
            Chip8Mnemonics.SHR.value:  self.registerToRegisterInstructions,
            Chip8Mnemonics.SUBN.value: self.registerToRegisterInstructions,
            Chip8Mnemonics.SHL.value: self.registerToRegisterInstructions,
            Chip8Mnemonics.SNER.value: self.skipIfRegisterNotEqualToRegister,
            Chip8Mnemonics.LDI.value: self.loadIndexRegister,
        }

    def disAssemble(self, pc: int, instruction: int) -> str:
        """

        Args:
            pc:    The program counter
            instruction: The opcode at the program counter

        Returns:  An assembly language version of the input opCode
        """
        self.pc:          int = pc
        self.instruction: int = instruction

        instStr: str = hex(instruction)
        self.logger.debug(f"currentInstruction: {instStr}")
        op: int = instruction & Chip8.OPCODE_MASK

        if op == Chip8.SPECIAL_REGISTERS_BASE_OP_CODE:
            op = instruction & Chip8.ENHANCED_OP_CODE_MASK
        elif op == Chip8.SKIP_BASED_ON_KEYBOARD_OP_CODE:
            op = instruction & Chip8.SKIP_OP_CODE_MASK
        elif op == Chip8.RET_OR_CLS_OP_CODE:
            op = instruction & Chip8.RET_OR_CLS_OP_CODE_MASK

        try:
            decode: Callable = self.opCodeMethods[op]
        except KeyError:
            raise UnknownInstructionError(badInstruction=op)

        mnemonicInstr = decode()

        return mnemonicInstr

    def returnFromSubroutine(self) -> str:

        strInstruction: str = (
            f'{self._memoryAddress()}'
            f'RTS'
        )
        return strInstruction

    def clearScreen(self) -> str:
        strInstruction: str = (
            f'{self._memoryAddress()}'
            f'CLS'
        )
        return strInstruction

    def jumpToAddress(self) -> str:

        addr = self.instruction & Chip8.ADDRESS_MASK

        strInstruction: str = (
            f'{self._memoryAddress()}'
            f'JUMP  '
            f'0x{addr:04X}'
        )
        return strInstruction

    def callSubroutine(self, ) -> str:

        subroutineAddr: int = self.instruction & Chip8.ADDRESS_MASK

        strInstruction: str = (
            f'{self._memoryAddress()}'
            f'CALL  '
            f'0x{subroutineAddr:04X}'
        )
        return strInstruction

    def skipIfRegisterEqualToLiteral(self) -> str:
        """
        3xkk; SEL Vx, kk
        """
        register: Chip8RegisterName = self._decodeRegister()

        strInstruction: str = (
            f'{self._memoryAddress()}'
            f'SEL '
            f'{register.name},'
            f'{self._literal()}'
        )

        return strInstruction

    def skipIfRegisterNotEqualToLiteral(self) -> str:
        """
        4xkk; SNEL Vx, kk;
        """
        register: Chip8RegisterName = self._decodeRegister()

        strInstruction: str = (
            f'{self._memoryAddress()}'
            f'SNEL '
            f'{register.name},'
            f'{self._literal()}'
        )

        return strInstruction

    def skipIfRegisterEqualToRegister(self) -> str:
        """
        5xy0; SER Vx, Vy
        """
        vxReg: Chip8RegisterName = self._decodeLeftRegister()
        vyReg: Chip8RegisterName = self._decodeRightRegister()

        strInstruction: str = (
            f'{self._memoryAddress()}'
            f'SER '
            f'{vxReg.name},'
            f'{vyReg.name}'
        )
        return strInstruction

    def loadRegisterWithLiteral(self) -> str:
        """
        6xkk; LDL Vx, kk
        """
        register: Chip8RegisterName = self._decodeRegister()

        strInstruction: str = (
            f'{self._memoryAddress()}'
            f'LDL '
            f'{register.name},'
            f'{self._literal()}'
        )
        return strInstruction

    def addLiteralToRegister(self) -> str:
        """
        7xkk; ADD Vx, kk;
        """
        register: Chip8RegisterName = self._decodeRegister()
        strInstruction: str = (
            f'{self._memoryAddress()}'
            f'ADD '
            f'{register.name},'
            f'{self._literal()}'
        )
        return strInstruction

    def registerToRegisterInstructions(self):
        """
        Handles 0x8000 through 0x8007 and 0x800E
        """
        subOpCode: int = self._decodeRegisterToRegisterOpCode()
        self.logger.info(f"Reg to Reg subOpCode: {subOpCode:X}")

        vxReg: Chip8RegisterName = self._decodeLeftRegister()
        vyReg: Chip8RegisterName = self._decodeRightRegister()

        opStr: str = ''
        if subOpCode == 0x0:     # 8xy0; MOV Vx,Vy
            opStr = f'MOV'
        elif subOpCode == 0x1:   # 8xy1; OR VxVy
            opStr = f'OR'
        elif subOpCode == 0x2:   # 8xy2; AND Vx,Vy
            opStr = f'AND'
        elif subOpCode == 0x3:   # 8xy3; XOR Vx,Vy
            opStr = f'XOR'
        elif subOpCode == 0x4:   # 8xy4; ADD Vx,Vy;     Set Vx = Vx + Vy
            opStr = f'ADDR'
        elif subOpCode == 0x5:   # 8xy5; SUB Vx,Vy;     Set Vx = Vx - Vy
            opStr = f'SUB'
        elif subOpCode == 0x6:   # 8xy5; SHR Vx,Vy;     Set Vx = Vx >> Vy
            opStr = f'{self._memoryAddress()}SHR {vxReg.name}'
            return opStr
        elif subOpCode == 0x7:   # SUBN Vx, Vy;    Set Vx = Vy - Vx
            opStr = f'SUBN'
        elif subOpCode == 0xE:   # 8xyE; SHL Vx, Vy;     Set Vx = Vx SHL 1
            opStr = f'{self._memoryAddress()}SHL {vxReg.name}'
            return opStr

        strInstruction: str = (
            f'{self._memoryAddress()}'
            f'{opStr} {vxReg.name},{vyReg.name}'
        )

        return strInstruction

    def skipIfRegisterNotEqualToRegister(self):
        """
        SNER Vx,Vy;    Skip next instruction if Vx != Vy
        """
        vxReg:  Chip8RegisterName = self._decodeLeftRegister()
        vyReg: Chip8RegisterName = self._decodeRightRegister()

        strInstruction: str = (
            f'{self._memoryAddress()}'
            f'SNER '
            f'{vxReg.name},'
            f'{vyReg.name}'
        )
        return strInstruction

    def loadIndexRegister(self):
        """
        Annn; LDI I,addr;    Set I = nnn; The value of register I is set to nnn
        """
        valToLoad: int = self.instruction & Chip8.IDX_REG_MASK
        strInstruction: str = (
            f'{self._memoryAddress()}'
            f'LDI I,'
            f'0x{valToLoad:03X}'
        )
        return strInstruction

    def _literal(self):
        lit: int = self._decodeLiteral()
        return f'0x{lit:02X}'

    def _memoryAddress(self) -> str:
        return f'0x{self.pc:04X}    '
