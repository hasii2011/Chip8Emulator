
from logging import Logger
from logging import getLogger

from pygame import Surface
from pygame.event import Event

from albow.core.ui.Screen import Screen

from albow.core.ui.Shell import Shell
from albow.core.ui.AlbowEventLoop import AlbowEventLoop

from albow.menu.Menu import Menu
from albow.menu.MenuBar import MenuBar
from albow.menu.MenuItem import MenuItem

from albow.layout.Column import Column
from albow.layout.Frame import Frame

from org.hasii.chip8.Chip8 import Chip8
from org.hasii.chip8.Chip8KeyPadKeys import Chip8KeyPadKeys
from org.hasii.chip8.Chip8Screen import Chip8Screen


class Chip8ScreenTestUIScreen(Screen):

    CPU_CYCLE_EVENT = AlbowEventLoop.MUSIC_END_EVENT + 1
    SIXTY_HERTZ       = 1000 // 60

    fileItems = [

        MenuItem(text="Load", command="processLoad"),
        MenuItem(text="Exit", command="processExit"),
    ]

    helpItems = [
        MenuItem(text="About", command="processAbout"),
        MenuItem(text="Help",  command="processHelp"),
    ]

    fileMenu: Menu = Menu(title="File", items=fileItems)
    helpMenu: Menu = Menu(title="Help", items=helpItems)

    def __init__(self, theShell: Shell, theSurface: Surface):
        """

        Args:
            self:

            theShell:  The shell that wraps this screen

            theSurface: The pygame surface to use to drawn on

        Returns:  An instance of itself

        """
        super().__init__(theShell)

        self.surface: Surface = theSurface
        self.logger:  Logger = getLogger(__name__)
        self.chip8:   Chip8 = Chip8()

        menus = [
            Chip8ScreenTestUIScreen.fileMenu, Chip8ScreenTestUIScreen.helpMenu
        ]

        menuBar = MenuBar(menus=menus, width=self.shell.width)

        framedMenuBar: Frame       = Frame(client=menuBar, width=self.shell.width)
        chip8Screen:   Chip8Screen = Chip8Screen(self.shell)
        columnAttrs = {
            "align": "l",
            'expand': 0
        }
        contents = Column([framedMenuBar, chip8Screen], **columnAttrs)

        self.logger.info(f"Menu bar size: {framedMenuBar.size}, shell width: {self.shell.width}")
        self.add(contents)

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

    def processLoad_cmd(self):
        self.logger.info("Executed load item command")

    def processExit_cmd(self):
        self.logger.info("Executed exit item command")
        self.shell.quit()

    def processAbout_cmd(self):
        self.logger.info("Executed about item command")

    def processHelp_cmd(self):
        self.logger.info("Executed help item command")
