
from pygame import draw

from typing import List
from typing import Dict
import random

from albow.core.ui.Widget import Widget

from org.hasii.chip8.Chip8SpriteType import Chip8SpriteType

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

    SPRITES: Dict[Chip8SpriteType, CHIP8_SPRITE] = {
        Chip8SpriteType.SPRITE_0: SPRITE_0,
        Chip8SpriteType.SPRITE_1: SPRITE_1,
        Chip8SpriteType.SPRITE_2: SPRITE_2,
        Chip8SpriteType.SPRITE_3: SPRITE_3,
        Chip8SpriteType.SPRITE_4: SPRITE_4,
        Chip8SpriteType.SPRITE_5: SPRITE_5,
        Chip8SpriteType.SPRITE_6: SPRITE_6,
        Chip8SpriteType.SPRITE_7: SPRITE_7,
        Chip8SpriteType.SPRITE_8: SPRITE_8,
        Chip8SpriteType.SPRITE_9: SPRITE_9,
        Chip8SpriteType.SPRITE_A: SPRITE_A,
        Chip8SpriteType.SPRITE_B: SPRITE_B,
        Chip8SpriteType.SPRITE_C: SPRITE_C,
        Chip8SpriteType.SPRITE_D: SPRITE_D,
        Chip8SpriteType.SPRITE_E: SPRITE_E,
        Chip8SpriteType.SPRITE_F: SPRITE_F,
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

    def getSprite(self, spriteType: Chip8SpriteType) -> CHIP8_SPRITE:
        return self.SPRITES[spriteType]

    def draw(self, surface):
        from pygame.draw import polygon
        polygon(surface, (128, 200, 255), self.points)
        polygon(surface, (255, 128, 0),   self.points, POLYGON_BORDER_WIDTH)
        self.animate()

    def draw_normal(self, x_pos, y_pos, num_bytes):
        """
        Draws a sprite on the screen while in NORMAL mode.

        Args:
            x_pos:      the X position of the sprite
            y_pos:      the Y position of the sprite
            num_bytes:  the number of bytes to draw
        """
        for y_index in range(num_bytes):

            color_byte = bin(self.memory[self.registers['index'] + y_index])
            color_byte = color_byte[2:].zfill(8)
            y_coord = y_pos + y_index
            y_coord = y_coord % Chip8Screen.HEIGHT

            for x_index in range(8):

                x_coord = x_pos + x_index
                x_coord = x_coord % Chip8Screen.WIDTH

                color = int(color_byte[x_index])
                current_color = self.screen.get_pixel(x_coord, y_coord)

                if color == 1 and current_color == 1:
                    self.registers['v'][0xF] = self.registers['v'][0xF] | 1
                    color = 0

                elif color == 0 and current_color == 1:
                    color = 1

                self.draw_pixel(x_coord, y_coord, color)

        self.screen.update()

    def draw_pixel(self, surface, x_pos, y_pos, pixel_color):
        """
        Turn a pixel on or off at the specified location on the screen. Note
        that the pixel will not automatically be drawn on the screen, you
        must call the update() function to flip the drawing buffer to the
        display. The coordinate system starts with (0, 0) being in the top
        left of the screen.

        Args:
            surface: The surface to drawn on
            x_pos: the x coordinate to place the pixel
            y_pos: the y coordinate to place the pixel
            pixel_color: the color of the pixel to draw
        """
        x_base = x_pos * self.SCALE_FACTOR
        y_base = y_pos * self.SCALE_FACTOR
        draw.rect(surface,
                  PIXEL_COLORS[pixel_color],
                  (x_base, y_base, self.SCALE_FACTOR, self.SCALE_FACTOR))

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
