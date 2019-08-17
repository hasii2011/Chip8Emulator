
from typing import List
from typing import cast

from logging import Logger
from logging import getLogger

from pygame import Surface
from pygame.event import Event

from albow.core.ui.Widget import Widget
from albow.core.ui.Screen import Screen
from albow.core.ui.Shell import Shell
from albow.core.ui.AlbowEventLoop import AlbowEventLoop

from albow.widgets.Label import Label
from albow.widgets.Button import Button
from albow.widgets.ListBox import ListBox

from albow.input.IntField import IntField

from albow.layout.Column import Column
from albow.layout.Row import Row
from albow.layout.Frame import Frame

from albow.dialog.DialogUtilities import alert

from albow.References import AttrRef

from org.hasii.chip8.Chip8 import Chip8
from org.hasii.chip8.keyboard.Chip8KeyPadKeys import Chip8KeyPadKeys
from org.hasii.chip8.Chip8Screen import Chip8Screen
from org.hasii.chip8.Chip8SpriteType import Chip8SpriteType


class Chip8ScreenTestUIScreen(Screen):

    CPU_CYCLE_EVENT = AlbowEventLoop.MUSIC_END_EVENT + 1
    SIXTY_HERTZ       = 1000 // 60

    def __init__(self, theShell: Shell, theSurface: Surface):
        """

        Args:
            self:

            theShell:  The shell that wraps this screen

            theSurface: The pygame surface to use to drawn on

        Returns:  An instance of itself

        """
        self.surface: Surface = theSurface
        super().__init__(theShell)

        self.logger:  Logger = getLogger(__name__)
        self.chip8:   Chip8 = Chip8()
        self.selectedSprite: Chip8SpriteType = cast(Chip8SpriteType, None)
        self.vXvalue: int = 0
        self.vYvalue: int = 0
        vxAttrRef: AttrRef = AttrRef(base=self, name="vXvalue")
        vyAttrRef: AttrRef = AttrRef(base=self, name="vYvalue")

        vXLabel: Label = Label("Vx:")
        vYLabel: Label = Label("Vy:")

        vXField: IntField = IntField(width=100, ref=vxAttrRef)
        vYField: IntField = IntField(width=100, ref=vyAttrRef)

        spriteSelector: ListBox = ListBox(nrows=2,
                                          theClient=self, theItems=Chip8SpriteType.toStrList(), selectAction=self.selectAction)
        self.logger.info(f"list box width: {spriteSelector.width}")
        drawButton:    Button       = Button("Draw", action=self.drawAction)
        widgetList:    List[Widget] = [drawButton, vXLabel, vXField, vYLabel, vYField, spriteSelector]

        rowAttrs = {'margin': 3}
        inputRow:      Row    = Row(items=widgetList, **rowAttrs)
        framedInputRow: Frame = Frame(client=inputRow)

        chip8Screen:   Chip8Screen = Chip8Screen(Chip8.virtualScreen)

        columnAttrs = {
            "align": "l",
            'expand': 0,
            'margin': 3
        }
        contents = Column([framedInputRow, chip8Screen], **columnAttrs)

        self.logger.info(f"framedInputRow size: {framedInputRow.size}, shell width: {self.shell.width} shell.height: {self.shell.height}")
        self.add(contents)

    def selectAction(self, theSelectedItem: str):
        self.selectedSprite = Chip8SpriteType.toEnum(theSelectedItem)
        self.logger.info(f"selectedSprite: {self.selectedSprite.name}")

    def drawAction(self):
        self.logger.info(f"Button pressed")
        if self.selectedSprite is None:
            alert("Please select a sprite type")
        else:
            self.logger.info(f"vX: {self.vXvalue} vY: {self.vYvalue}")
            spriteDigit: int = self.selectedSprite.value
            spriteStartAddress: int = Chip8.SPRITE_START_ADDRESS + (spriteDigit * Chip8.BYTES_PER_SPRITE)

            self.chip8.indexRegister = spriteStartAddress
            self.chip8.drawOnVirtualScreen(xCoord=self.vXvalue, yCoord=self.vYvalue, nBytes=Chip8.BYTES_PER_SPRITE)

    def timer_event(self, theEvent: Event):
        """
        The shell set this up to be called at the CHIP8 60Hz rate;
        So here we will
         * emulate a CPU cycle
         * decrement both the CHIP 8 delay timer and the sound timer

        Args:
            theEvent:

        """
        # clock          = Clock()
        # milliseconds   = clock.tick(1000)         # milliseconds passed since last frame; needs to agree witH Chip8UIShell value
        # self.logger.info(f"milliseconds: {milliseconds}")
        milliseconds: float = theEvent.dict['time']
        self.logger.debug(f"milliseconds: {milliseconds}")
        self.chip8.decrementDelayTimer()
        self.chip8.decrementSoundTimer()

        return True

    def key_down(self, theKeyEvent: Event):

        pressedKey: Chip8KeyPadKeys = Chip8KeyPadKeys.toEnum(theKeyEvent.key)
        self.logger.debug(f"key down: {pressedKey.value:X}")
        self.chip8.keypad.keyDown(pressedKey)
        self.logger.debug(f"keypad: {self.chip8.keypad}")

    def key_up(self, theKeyEvent: Event):

        releasedKey: Chip8KeyPadKeys = Chip8KeyPadKeys.toEnum(theKeyEvent.key)
        self.logger.debug(f"key up: {releasedKey.value:X}")
        self.chip8.keypad.keyUp(releasedKey)
        self.logger.debug(f"keypad: {self.chip8.keypad}")
