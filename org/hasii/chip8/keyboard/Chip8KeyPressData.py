
from typing import cast

from dataclasses import dataclass

from org.hasii.chip8.Chip8RegisterName import Chip8RegisterName
from org.hasii.chip8.keyboard.Chip8KeyPadKeys import Chip8KeyPadKeys


@dataclass
class Chip8KeyPressData:

    waitingForKey: bool = False
    pressedKey:    Chip8KeyPadKeys   = cast(Chip8KeyPadKeys, None)
    storeRegister: Chip8RegisterName = cast(Chip8RegisterName, None)

    def __repr__(self):

        retStr: str = (
            f'waitingForKey: "{self.waitingForKey}" '
            f'pressedKey: "{self.pressedKey}" '
            f'storeRegister: "{self.storeRegister}"'
        )
        return retStr
