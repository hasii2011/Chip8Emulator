
from typing import List
from enum import Enum


class Chip8SpriteType(Enum):

    SPRITE_0 = 0x0
    SPRITE_1 = 0x1
    SPRITE_2 = 0x2
    SPRITE_3 = 0x3
    SPRITE_4 = 0x4
    SPRITE_5 = 0x5
    SPRITE_6 = 0x6
    SPRITE_7 = 0x7
    SPRITE_8 = 0x8
    SPRITE_9 = 0x9
    SPRITE_A = 0xA
    SPRITE_B = 0xB
    SPRITE_C = 0xC
    SPRITE_D = 0xD
    SPRITE_E = 0xE
    SPRITE_F = 0xF

    @staticmethod
    def toStrList() -> List[str]:

        retList: List[str] = []

        for spriteType in Chip8SpriteType:
            retList.append(spriteType.name)
        return retList

    @staticmethod
    def toEnum(spriteType: str) -> 'Chip8SpriteType':
        """
        TODO: make up for a deficiency in the Albow list box;  It can only return strings
        Args:
            spriteType: The string version of the type

        Returns: The associated enumeration or raises the XXX exception if it cannot match
        the string

         Raises: ValueError
        """
        if spriteType == 'SPRITE_0':
            return Chip8SpriteType.SPRITE_0
        elif spriteType == 'SPRITE_1':
            return Chip8SpriteType.SPRITE_1
        elif spriteType == 'SPRITE_2':
            return Chip8SpriteType.SPRITE_2
        elif spriteType == 'SPRITE_3':
            return Chip8SpriteType.SPRITE_3
        elif spriteType == 'SPRITE_4':
            return Chip8SpriteType.SPRITE_4
        elif spriteType == 'SPRITE_5':
            return Chip8SpriteType.SPRITE_5
        elif spriteType == 'SPRITE_6':
            return Chip8SpriteType.SPRITE_6
        elif spriteType == 'SPRITE_7':
            return Chip8SpriteType.SPRITE_7
        elif spriteType == 'SPRITE_8':
            return Chip8SpriteType.SPRITE_8
        elif spriteType == 'SPRITE_9':
            return Chip8SpriteType.SPRITE_9
        elif spriteType == 'SPRITE_A':
            return Chip8SpriteType.SPRITE_A
        elif spriteType == 'SPRITE_B':
            return Chip8SpriteType.SPRITE_B
        elif spriteType == 'SPRITE_C':
            return Chip8SpriteType.SPRITE_C
        elif spriteType == 'SPRITE_D':
            return Chip8SpriteType.SPRITE_D
        elif spriteType == 'SPRITE_E':
            return Chip8SpriteType.SPRITE_E
        elif spriteType == 'SPRITE_F':
            return Chip8SpriteType.SPRITE_F
        else:
            raise ValueError(f"Do not understand sprite type of {spriteType}")
