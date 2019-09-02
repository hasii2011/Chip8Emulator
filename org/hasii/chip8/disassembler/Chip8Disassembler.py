
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

        self.logger: Logger = getLogger(__name__)

        self.pc:          int = 0x0000
        self.instruction: int = 0x0000

        self.opCodeMethods: Dict[int, Callable] = {

            Chip8Mnemonics.RTS.value:  self.returnFromSubroutine,
            Chip8Mnemonics.CLS.value:  self.clearScreen,
            Chip8Mnemonics.JUMP.value: self.jumpToAddress,
            Chip8Mnemonics.CALL.value: self.callSubroutine,
            Chip8Mnemonics.SEL.value:  self.skipIfRegisterEqualToLiteral,
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
        self.pc = addr
        self.logger.debug(f"new pc: {hex(self.pc)}")

    def callSubroutine(self, ) -> str:

        subroutineAddr: int = self.instruction & Chip8.ADDRESS_MASK

        strInstruction: str = (
            f'{self._memoryAddress()}'
            f'Call  '
            f'0x{subroutineAddr:04X}'
        )

        return strInstruction

    def skipIfRegisterEqualToLiteral(self) -> str:
        """
        3xkk; SEL Vx, kk
        """
        register: Chip8RegisterName = self._decodeRegister()
        lit:      int               = self._decodeLiteral()

        strInstruction: str = (
            f'{self._memoryAddress()}'
            f'SEL '
            f'{register.name},'
            f'0x{lit:02X}'
        )

        return strInstruction

    def _memoryAddress(self) -> str:
        return f'0x{self.pc:04X}    '
