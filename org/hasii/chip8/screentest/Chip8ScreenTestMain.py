
from typing import Tuple
import json

import logging
import logging.config

import pygame

from pygame import Surface

from albow.themes.ThemeLoader import ThemeLoader
from albow.themes.Theme import Theme

from org.hasii.chip8.screentest.Chip8ScreenTestUIShell import Chip8ScreenTestUIShell

from org.hasii.chip8.Chip8Screen import Chip8Screen

JSON_LOGGING_CONFIG_FILENAME = "loggingConfiguration.json"
MADE_UP_PRETTY_MAIN_NAME     = "Chip8ScreenTestMain"

MENU_BAR_HEIGHT_ADJUSTMENT: int = 56
MENU_BAR_WIDTH_ADJUSTMENT:  int = 0


def main():

    with open(JSON_LOGGING_CONFIG_FILENAME, 'r') as loggingConfigurationFile:
        configurationDictionary = json.load(loggingConfigurationFile)

    logging.config.dictConfig(configurationDictionary)
    logging.logProcesses = False
    logging.logThreads = False

    logger = logging.getLogger(MADE_UP_PRETTY_MAIN_NAME)

    themeLoader: ThemeLoader = ThemeLoader()
    themeLoader.load()
    themeRoot: Theme = themeLoader.themeRoot
    Theme.setThemeRoot(themeRoot)

    pygame.init()
    pygame.display.set_caption("Python Chip 8 Emulator")

    windowWidthHeight: Tuple[int,int] = (720, 500)
    surface: Surface = pygame.display.set_mode(windowWidthHeight)
    shell:   Chip8ScreenTestUIShell = Chip8ScreenTestUIShell(theSurface=surface)

    logger.info(f"Starting {MADE_UP_PRETTY_MAIN_NAME}")

    shell.run()


if __name__ == "__main__":
    main()
