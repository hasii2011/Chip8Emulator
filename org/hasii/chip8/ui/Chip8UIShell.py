
from logging import Logger
from logging import getLogger

from pygame import Surface

from albow.core.ui.Shell import Shell

from org.hasii.chip8.Chip8 import Chip8

from org.hasii.chip8.ui.Chip8UIScreen import Chip8UIScreen


class Chip8UIShell(Shell):

    """
    Shell
    """
    def __init__(self, theSurface: Surface, **kwds):
        """

        Args:
            display:
        """
        #
        # Python 3 update
        #
        super().__init__(theSurface, **kwds)

        self.logger: Logger = getLogger(__name__)

        self.chip8UiScreen = Chip8UIScreen(theShell=self, theSurface=theSurface)

        self.set_timer(Chip8.CPU_CYCLE)
        self.show_screen(self.chip8UiScreen)

    def show_main_screen(self):

        self.logger.info(f"Showing main screen")
        #  self.show_screen(self.menu_screen)

    def __repr__(self):
        return self.__class__.__name__
