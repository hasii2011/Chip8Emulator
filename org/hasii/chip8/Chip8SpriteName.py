
from typing import List
from enum import Enum


class Chip8SpriteName(Enum):

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

        for spriteName in Chip8SpriteName:
            retList.append(spriteName.name)
        return retList
