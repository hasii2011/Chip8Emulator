
from typing import List

from logging import Logger
from logging import getLogger

import random

from pygame import Rect

from albow.core.ui.Widget import Widget
from albow.themes.Theme import Theme

POLYGON_BORDER_WIDTH: int = 2

CHIP8_SPRITE = List[int]

PIXEL_COLORS = {
    0: (0, 0, 0),
    1: (250, 250, 250)
}


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

    Dxyn - DRAW x, y, num_bytes

        Draws the sprite pointed to in the index register at the specified
        x and y coordinates. Drawing is done via an XOR routine, meaning that
        if the target pixel is already turned on, and a pixel is set to be
        turned on at that same location via the draw, then the pixel is turned
        off. The routine will wrap the pixels if they are drawn off the edge
        of the screen. Each sprite is 8 bits (1 byte) wide. The num_bytes
        parameter sets how tall the sprite is. Consecutive bytes in the memory
        pointed to by the index register make up the bytes of the sprite. Each
        bit in the sprite byte determines whether a pixel is turned on (1) or
        turned off (0). For example, assume that the index register pointed
        to the following 7 bytes:

                       bit 0 1 2 3 4 5 6 7

           byte 0          0 1 1 1 1 1 0 0
           byte 1          0 1 0 0 0 0 0 0
           byte 2          0 1 0 0 0 0 0 0
           byte 3          0 1 1 1 1 1 0 0
           byte 4          0 1 0 0 0 0 0 0
           byte 5          0 1 0 0 0 0 0 0
           byte 6          0 1 1 1 1 1 0 0

        This would draw a character on the screen that looks like an 'E'. The
        x_source and y_source tell which registers contain the x and y
        coordinates for the sprite. If writing a pixel to a location causes
        that pixel to be turned off, then VF will be set to 1.

           Bits:  15-12     11-8      7-4       3-0
                  unused    x_source  y_source  num_bytes
    """

    SCALE_FACTOR: int = 10
    WIDTH:        int = 64
    HEIGHT:       int = 32

    def __init__(self, **attrs):

        self.border_width = 1
        self.border_color = Theme.BLACK

        super().__init__(**attrs)

        self.logger: Logger = getLogger(__name__)

        self.rect = Rect(0, 0, (self.WIDTH * self.SCALE_FACTOR), (self.HEIGHT * self.SCALE_FACTOR))

        w, h = self.size
        self.logger.info(f" w: {w} h: {h} rect: {self.rect}")
        self.points = [[100, 50], [w - 50, 100], [50, h - 50]]

        def randomValue():
            return random.randint(-5, 5)

        self.velocities = [
            [randomValue(), randomValue()] for i in range(len(self.points))
        ]

    def draw(self, surface):
        from pygame.draw import polygon

        surface.fill(Theme.BLUE)
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
