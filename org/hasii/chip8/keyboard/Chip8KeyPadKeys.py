
from enum import Enum

from pygame import K_0
from pygame import K_1
from pygame import K_2
from pygame import K_3
from pygame import K_4
from pygame import K_5
from pygame import K_6
from pygame import K_7
from pygame import K_8
from pygame import K_9
from pygame import K_a
from pygame import K_b
from pygame import K_c
from pygame import K_d
from pygame import K_e
from pygame import K_f


class Chip8KeyPadKeys(Enum):

    Zero  = 0x0
    One   = 0x1
    Two   = 0x2
    Three = 0x3
    Four  = 0x4
    Five  = 0x5
    Six   = 0x6
    Seven = 0x7
    Eight = 0x8
    Nine  = 0x9
    A     = 0xA
    B     = 0xB
    C     = 0xC
    D     = 0xD
    E     = 0xE
    F     = 0xF
    UNSUPPORTED = 0xFFFF

    @staticmethod
    def toEnum(key: int) -> 'Chip8KeyPadKeys':
        """
        Converts pygame keyboard keys to the Chip 8 equivalent
        Args:
            key:   The pygame keyboard value

        Returns:  The Chip 8 enumeration value

        """

        if key == K_0:
            return Chip8KeyPadKeys.Zero
        elif key == K_1:
            return Chip8KeyPadKeys.One
        elif key == K_2:
            return Chip8KeyPadKeys.Two
        elif key == K_3:
            return Chip8KeyPadKeys.Three
        elif key == K_4:
            return Chip8KeyPadKeys.Four
        elif key == K_5:
            return Chip8KeyPadKeys.Five
        elif key == K_6:
            return Chip8KeyPadKeys.Six
        elif key == K_7:
            return Chip8KeyPadKeys.Seven
        elif key == K_8:
            return Chip8KeyPadKeys.Eight
        elif key == K_9:
            return Chip8KeyPadKeys.Nine
        elif key == K_a:
            return Chip8KeyPadKeys.A
        elif key == K_b:
            return Chip8KeyPadKeys.B
        elif key == K_c:
            return Chip8KeyPadKeys.C
        elif key == K_d:
            return Chip8KeyPadKeys.D
        elif key == K_e:
            return Chip8KeyPadKeys.E
        elif key == K_f:
            return Chip8KeyPadKeys.F
        else:
            return Chip8KeyPadKeys.UNSUPPORTED
