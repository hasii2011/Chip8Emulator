
from typing import List
from typing import Dict
import random

from albow.core.ui.Widget import Widget

from org.hasii.chip8.Chip8SpriteName import Chip8SpriteName

POLYGON_BORDER_WIDTH: int = 2

CHIP8_SPRITE = List[int]


class Chip8Screen(Widget):
    """
    The interpreter
        * Reads n bytes from memory starting at the address stored in I.
        * These bytes are then displayed as sprites on screen at coordinates (Vx, Vy).
        * Sprites are XORed onto the existing screen.
            1 If this causes any pixels to be erased, VF is set to 1,
            2 otherwise it is set to 0.
        * If the sprite is positioned so part of it is outside the coordinates of the display,
            it wraps around to the opposite side of the screen.
    See instruction 8xy3 for more information on XOR,

    The original implementation of the Chip-8 language used a 64x32-pixel monochrome display with this format:

                                        |------------------------|
                                        |(0,0)           (63,0)  |
                                        |(0,31)          (63,31) |
                                        |------------------------|


    * Chip-8 draws graphics on screen through the use of sprites.
    * A sprite is a group of bytes which are a binary representation of the desired picture.
    * Chip-8 sprites may be up to 15 bytes, for a possible sprite size of 8x15.

    * Graphics are drawn as 8 x 1...15 sprites (they are byte coded). The origin of the screen is the upper left corner.
    * All the coordinates are positive, start at 0, and are calculated modulo 64 for X, and 32 for Y when drawing sprites.
    * All drawings are done in XOR mode. When one or more pixels are erased while a sprite is drawn, the VF register is set to
    0x01, otherwise 0x00.
    * CHIP8 has a 4 x 5 pixels hexadecimal font to draw characters. These ones are 0-9 and A-F.

    """
    SPRITE_0: CHIP8_SPRITE = [0xF0, 0x90, 0x90, 0x90, 0xF0]   # 0
    SPRITE_1: CHIP8_SPRITE = [0x20, 0x60, 0x20, 0x20, 0x70]   # 1
    SPRITE_2: CHIP8_SPRITE = [0xF0, 0x10, 0xF0, 0x80, 0xF0]   # 2
    SPRITE_3: CHIP8_SPRITE = [0xF0, 0x10, 0xF0, 0x10, 0xF0]   # 3
    SPRITE_4: CHIP8_SPRITE = [0x90, 0x90, 0xF0, 0x10, 0x10]   # 4
    SPRITE_5: CHIP8_SPRITE = [0xF0, 0x80, 0xF0, 0x10, 0xF0]   # 5
    SPRITE_6: CHIP8_SPRITE = [0xF0, 0x80, 0xF0, 0x90, 0xF0]   # 6
    SPRITE_7: CHIP8_SPRITE = [0xF0, 0x10, 0x20, 0x40, 0x50]   # 7
    SPRITE_8: CHIP8_SPRITE = [0xF0, 0x90, 0xF0, 0x90, 0xF0]   # 8
    SPRITE_9: CHIP8_SPRITE = [0xF0, 0x90, 0xF0, 0x10, 0xF0]   # 9
    SPRITE_A: CHIP8_SPRITE = [0xF0, 0x90, 0xF0, 0x90, 0x90]   # A
    SPRITE_B: CHIP8_SPRITE = [0xE0, 0x90, 0xE0, 0x90, 0xE0]   # B
    SPRITE_C: CHIP8_SPRITE = [0xF0, 0x80, 0x80, 0x80, 0xF0]   # C
    SPRITE_D: CHIP8_SPRITE = [0xE0, 0x90, 0x90, 0x90, 0xE0]   # D
    SPRITE_E: CHIP8_SPRITE = [0xF0, 0x80, 0xF0, 0x80, 0xF0]   # E
    SPRITE_F: CHIP8_SPRITE = [0xF0, 0x80, 0xF0, 0x80, 0x80]   # F

    SPRITES: Dict[Chip8SpriteName, CHIP8_SPRITE] = {
        Chip8SpriteName.SPRITE_0: SPRITE_0,
        Chip8SpriteName.SPRITE_1: SPRITE_1,
        Chip8SpriteName.SPRITE_2: SPRITE_2,
        Chip8SpriteName.SPRITE_3: SPRITE_3,
        Chip8SpriteName.SPRITE_4: SPRITE_4,
        Chip8SpriteName.SPRITE_5: SPRITE_5,
        Chip8SpriteName.SPRITE_6: SPRITE_6,
        Chip8SpriteName.SPRITE_7: SPRITE_7,
        Chip8SpriteName.SPRITE_8: SPRITE_8,
        Chip8SpriteName.SPRITE_9: SPRITE_9,
        Chip8SpriteName.SPRITE_A: SPRITE_A,
        Chip8SpriteName.SPRITE_B: SPRITE_B,
        Chip8SpriteName.SPRITE_C: SPRITE_C,
        Chip8SpriteName.SPRITE_D: SPRITE_D,
        Chip8SpriteName.SPRITE_E: SPRITE_E,
        Chip8SpriteName.SPRITE_F: SPRITE_F,
    }
    SCALE_FACTOR: int = 10
    WIDTH:        int = 64
    HEIGHT:       int = 32

    def __init__(self, parent, **attrs):

        self.border_width = 1
        super().__init__(**attrs)

        self.rect = parent.rect.inflate(-100, -100)
        w, h = self.size
        self.points = [[100, 50], [w - 50, 100], [50, h - 50]]

        def randomValue():
            return random.randint(-5, 5)

        self.velocities = [
            [randomValue(), randomValue()] for i in range(len(self.points))
        ]

    def getSprite(self, spriteName: Chip8SpriteName) -> CHIP8_SPRITE:
        return self.SPRITES[spriteName]

    def draw(self, surface):
        from pygame.draw import polygon
        polygon(surface, (128, 200, 255), self.points)
        polygon(surface, (255, 128, 0),   self.points, POLYGON_BORDER_WIDTH)
        self.animate()

    def animate(self):
        r = self.rect
        w, h = r.size
        for p, v in zip(self.points, self.velocities):
            p[0] += v[0]
            p[1] += v[1]
            if not 0 <= p[0] <= w:
                v[0] = -v[0]
            if not 0 <= p[1] <= h:
                v[1] = -v[1]
        self.invalidate()
