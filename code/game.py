import sys

import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[3]:  # EXIT
                pygame.quit()  # Close window
                quit()  # end pygame
            else:
                pygame.quit()
                sys.exit()
