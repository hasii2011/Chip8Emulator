
import random

from albow.core.ui.Widget import Widget

POLYGON_BORDER_WIDTH: int = 2


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

    """
    SCALE_FACTOR: int = 10
    WIDTH:        int = 64
    HEIGHT:       int = 32

    def __init__(self, parent, **attrs):

        super().__init__(**attrs)

        self.rect = parent.rect.inflate(-100, -100)
        w, h = self.size
        self.points = [[100, 50], [w - 50, 100], [50, h - 50]]

        def randomValue():
            return random.randint(-5, 5)

        self.velocities = [
            [randomValue(), randomValue()] for i in range(len(self.points))
        ]

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
