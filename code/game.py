import sys

import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.entityFactory import EntityFactory
from code.level import Level
from code.menu import Menu
from code.score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                # NEW GAME 1 PLAYER
                player_score = [0, 0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        level = Level(self.window, 'Level3', menu_return, player_score)
                        level_return = level.run(player_score)
                        if level_return:
                            level = Level(self.window, 'Level4', menu_return, player_score)
                            level_return = level.run(player_score)
                            if level_return:
                                score.save(level.game_mode, player_score)
                if not level_return:
                    continue

            elif menu_return == MENU_OPTION[2]:
                score.show() # Show score
                continue

            if menu_return == MENU_OPTION[3]:  # EXIT
                pygame.quit()  # Close window
                quit()  # end pygame
            else:
                pygame.quit()
                sys.exit()
