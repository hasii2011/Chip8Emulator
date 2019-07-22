
from logging import Logger
from logging import getLogger

from pygame.time import Clock
from pygame import Surface
from pygame.event import Event

from albow.core.ui.Screen import Screen
from albow.core.ui.Shell import Shell


class Chip8UIScreen(Screen):

    def __init__(self, theShell: Shell, theSurface: Surface):
        """

        Args:
            self:

            theShell:  The shell that wraps this screen

            theSurface: The pygame surface to use to drawn on

        Returns:  An instance of itself

        """
        super().__init__(theShell)

        self.logger: Logger = getLogger(__name__)
        #
        # Debug logger
        #
        # saveLogger = self.logger
        # while self.logger is not None:
        #     print(f"level: '{self.logger.level}'', name: '{self.logger.name}'', handlers: '{self.logger.handlers}"'')
        #     self.logger = self.logger.parent
        # self.logger = saveLogger
        #
        self.surface:  Surface = theSurface
        self.playTime: float   = 0.0

    def timer_event(self, theEvent: Event):
        """
        Called from the timer_event() method of the Shell when this screen is the current screen. The default
        implementation returns true so that a display update is performed.

        Args:
            theEvent:

        """
        clock          = Clock()
        milliseconds   = clock.tick(1000)         # milliseconds passed since last frame; needs to agree witH Chip8UIShell value
        self.logger.info(f"milliseconds: {milliseconds}")
        quarterSeconds = milliseconds / 250.0   # quarter-seconds passed since last frame (float)
        self.playTime  += quarterSeconds

        self.logger.info(f"playtime: {self.playTime}")
        return True
