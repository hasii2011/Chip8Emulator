import json

import logging
import logging.config

import pygame

from pygame import Surface

from albow.themes.ThemeLoader import ThemeLoader
from albow.themes.Theme import Theme

JSON_LOGGING_CONFIG_FILENAME = "loggingConfiguration.json"
MADE_UP_PRETTY_MAIN_NAME     = "Chip8Main"

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

    surface: Surface = pygame.display.set_mode((64, 32))

    logger.info(f"Starting {MADE_UP_PRETTY_MAIN_NAME}"  )


if __name__ == "__main__":
    main()
