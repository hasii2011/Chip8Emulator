import json

import logging
import logging.config

import pygame

from pygame import Surface

from albow.themes.ThemeLoader import ThemeLoader
from albow.themes.Theme import Theme

from org.hasii.chip8.ui.Chip8UIShell import Chip8UIShell

from org.hasii.chip8.ui.Chip8Screen import Chip8Screen

JSON_LOGGING_CONFIG_FILENAME = "loggingConfiguration.json"
MADE_UP_PRETTY_MAIN_NAME     = "Chip8Main"

MENU_BAR_HEIGHT_ADJUSTMENT:          int = 24
INTERNALS_DISPLAY_HEIGHT_ADJUSTMENT: int = 285


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

    surface: Surface = pygame.display.set_mode(
        (Chip8Screen.WIDTH * Chip8Screen.SCALE_FACTOR, (Chip8Screen.HEIGHT * Chip8Screen.SCALE_FACTOR) + MENU_BAR_HEIGHT_ADJUSTMENT + INTERNALS_DISPLAY_HEIGHT_ADJUSTMENT)
    )
    shell:   Chip8UIShell = Chip8UIShell(theSurface=surface)

    logger.info(f"Starting {MADE_UP_PRETTY_MAIN_NAME}")

    shell.run()


if __name__ == "__main__":
    main()
