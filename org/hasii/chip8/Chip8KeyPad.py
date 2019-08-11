
from typing import Dict
from typing import cast

from logging import Logger
from logging import getLogger


from org.hasii.chip8.Chip8KeyPadKeys import Chip8KeyPadKeys


class Chip8KeyPad:

    def __init__(self):

        self.logger: Logger = getLogger(__name__)

        self.keyPressed: Dict[Chip8KeyPadKeys, bool] = {
            Chip8KeyPadKeys.Zero:   False,
            Chip8KeyPadKeys.One:    False,
            Chip8KeyPadKeys.Two:    False,
            Chip8KeyPadKeys.Three:  False,
            Chip8KeyPadKeys.Four:   False,
            Chip8KeyPadKeys.Five:   False,
            Chip8KeyPadKeys.Six:    False,
            Chip8KeyPadKeys.Seven:  False,
            Chip8KeyPadKeys.Eight:  False,
            Chip8KeyPadKeys.Nine:   False,
            Chip8KeyPadKeys.A:      False,
            Chip8KeyPadKeys.B:      False,
            Chip8KeyPadKeys.C:      False,
            Chip8KeyPadKeys.D:      False,
            Chip8KeyPadKeys.E:      False,
            Chip8KeyPadKeys.F:      False,
        }

    def keyDown(self, key: Chip8KeyPadKeys):
        self.keyPressed[key] = True

    def keyUp(self, key: Chip8KeyPadKeys):
        self.keyPressed[key] = False

    def isKeyPressed(self, key: Chip8KeyPadKeys) -> bool:
        return self.keyPressed[key]

    def __repr__(self):

        retStr: str = 'Chip8 Keypad state dump\n'
        for key in self.keyPressed:
            retStr += f'{key.value:X}->{self.keyPressed.get(key)} '
        return retStr
