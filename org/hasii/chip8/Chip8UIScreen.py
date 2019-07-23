
from logging import Logger
from logging import getLogger


from pygame import Surface
from pygame.event import Event

from albow.core.ui.Screen import Screen

from albow.core.ui.Shell import Shell
from albow.core.ui.AlbowEventLoop import AlbowEventLoop


class Chip8UIScreen(Screen):

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
        self.logger.info(f"milliseconds: {milliseconds}")
        return True
