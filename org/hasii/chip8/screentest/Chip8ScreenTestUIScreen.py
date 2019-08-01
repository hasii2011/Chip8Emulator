
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

from albow.input.TextField import TextField

from albow.layout.Column import Column
from albow.layout.Row import Row
from albow.layout.Frame import Frame

from albow.dialog.DialogUtilities import alert

from org.hasii.chip8.Chip8 import Chip8
from org.hasii.chip8.Chip8KeyPadKeys import Chip8KeyPadKeys
from org.hasii.chip8.Chip8Screen import Chip8Screen
from org.hasii.chip8.Chip8SpriteName import Chip8SpriteName


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
        self.logger:  Logger = getLogger(__name__)
        self.selectedSprite: Chip8SpriteName = cast(Chip8SpriteName, None)

        super().__init__(theShell)

        self.chip8:   Chip8 = Chip8()

        vXLabel: Label = Label("Vx: ")
        vYLabel: Label = Label("VY: ")

        vXField: TextField = TextField(width=100)
        vYField: TextField = TextField(width=100)

        spriteSelector: ListBox = ListBox(nrows=2,
                                          theClient=self, theItems=Chip8SpriteName.toStrList(), selectAction=self.selectAction)
        self.logger.info(f"list box width: {spriteSelector.width}")
        drawButton:    Button       = Button("Draw", action=self.drawAction)
        widgetList:    List[Widget] = [drawButton, vXLabel, vXField, vYLabel, vYField, spriteSelector]

        rowAttrs = {'margin': 3}
        inputRow:      Row          = Row(items=widgetList, **rowAttrs)
        framedInputRow: Frame       = Frame(client=inputRow)

        chip8Screen:   Chip8Screen = Chip8Screen(self.shell)

        columnAttrs = {
            "align": "l",
            'expand': 0,
            'margin': 3
        }
        contents = Column([framedInputRow, chip8Screen], **columnAttrs)

        self.logger.info(f"framedInputRow size: {framedInputRow.size}, shell width: {self.shell.width}")
        self.add(contents)

    def selectAction(self, theSelectedItem: str):
        self.logger.info(f"theSelectedItem: {theSelectedItem}")

    def drawAction(self):
        self.logger.info(f"Button pressed")
        if self.selectedSprite is None:
            alert("Please select a sprite type")

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
