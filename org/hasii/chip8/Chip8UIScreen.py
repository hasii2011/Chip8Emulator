from os import getcwd

from typing import cast

from logging import Logger
from logging import getLogger

from pygame import Surface
from pygame.event import Event

from albow.core.ui.Screen import Screen

from albow.dialog.FileDialogUtilities import request_old_filename

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

from org.hasii.chip8.errors.InvalidIndexRegisterValue import InvalidIndexRegisterValue
from org.hasii.chip8.errors.UnknownInstructionError import UnknownInstructionError
from org.hasii.chip8.errors.UnKnownSpecialRegistersSubOpCode import UnKnownSpecialRegistersSubOpCode
from org.hasii.chip8.Chip8Beep import Chip8Beep


class Chip8UIScreen(Screen):

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
            theShell:  The shell that wraps this screen

            theSurface: The pygame surface to use to drawn on

        Returns:  An instance of itself

        """
        super().__init__(theShell)

        self.surface: Surface = theSurface
        self.logger:  Logger = getLogger(__name__)
        self.chip8:   Chip8 = Chip8()
        #
        # TEMP TEMP TEMP; until I get File->Load working
        #
        self.chip8.loadROM("Invaders")

        self.note: Chip8Beep = cast(Chip8Beep, None)

        menus = [
            Chip8UIScreen.fileMenu, Chip8UIScreen.helpMenu
        ]

        menuBar = MenuBar(menus=menus, width=self.shell.width)

        framedMenuBar: Frame       = Frame(client=menuBar, width=self.shell.width)
        chip8Screen:   Chip8Screen = Chip8Screen(self.chip8.virtualScreen)
        columnAttrs = {
            "align": "l",
            'expand': 0
        }
        contents = Column([framedMenuBar, chip8Screen], **columnAttrs)

        self.logger.debug(f"Menu bar size: {framedMenuBar.size}, shell width: {self.shell.width}")
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
        seconds:      float = milliseconds/1000
        self.logger.debug(f"seconds: {seconds:5.3f}")
        try:
            if self.chip8.romLoaded is True:
                self.chip8.emulateSingleCpuCycle()
                self.chip8.decrementDelayTimer()
                self.chip8.decrementSoundTimer()
        except (UnknownInstructionError, InvalidIndexRegisterValue, UnKnownSpecialRegistersSubOpCode) as e:
            self.logger.error(f"Chip 8 failure: {e}")
            self.logger.error(f"Chip Dump:\n {self.chip8}")
            self.chip8.debugPrintMemory = True
            self.logger.error(f'                        MEMORY DUMP')
            self.logger.error(f'____________________________________________________________________')
            self.chip8._debugPrintMemory(startByteNbr=0, nBytes=len(self.chip8.memory))

            self.shell.quit()

        return True

    def key_down(self, theKeyEvent: Event):
        """
        Seems like part of the Chip 8 emulator has to happen here:
        http://laurencescotford.co.uk/?p=347

        Args:
            theKeyEvent:  The PyGame key event
        """
        pressedKey: Chip8KeyPadKeys = Chip8KeyPadKeys.toEnum(theKeyEvent.key)
        self.logger.debug(f"key down: {pressedKey.value:X}")
        self.chip8.keypad.keyDown(pressedKey)
        self.logger.debug(f"keypad: {self.chip8.keypad}")
        self.note = Chip8Beep(440)
        self.note.play(-1)

    def key_up(self, theKeyEvent: Event):

        releasedKey: Chip8KeyPadKeys = Chip8KeyPadKeys.toEnum(theKeyEvent.key)
        self.logger.debug(f"key up: {releasedKey.value:X}")
        self.chip8.keypad.keyUp(releasedKey)
        self.logger.debug(f"keypad: {self.chip8.keypad}")
        self.note.stop()

    def processLoad_cmd(self):

        cwd: str = getcwd() + '/org/hasii/chip8/roms'
        path = request_old_filename(directory=cwd)
        self.logger.info(f'path: {path}')

    def processExit_cmd(self):
        self.logger.info("Executed exit item command")
        self.shell.quit()

    def processAbout_cmd(self):
        self.logger.info("Executed about item command")

    def processHelp_cmd(self):
        self.logger.info("Executed help item command")
