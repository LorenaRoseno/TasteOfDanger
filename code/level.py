import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.background import Background
from code.const import TIMEOUT_LEVEL, MENU_OPTION, EVENT_FOOD, EVENT_TIMEOUT, TIMEOUT_STEP, WIN_WIDTH, C_WHITE, \
    WIN_HEIGHT, C_BLACK, C_YELLOW, SPAWN_TIME, C_LIGHT_GREEN, C_ORANGE
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.goodFood import GoodFood
from code.player import Player
from code.poisonFood import PoisonFood


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.background = Background(window, self.name)
        self.next_food_spawn_time = pygame.time.get_ticks()
        self.food_spawn_interval = 1000
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_FOOD, SPAWN_TIME[self.name])
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        self.show_level_start()
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            current_time = pygame.time.get_ticks()
            for ent in self.entity_list[:]:
                if isinstance(ent, (GoodFood, PoisonFood)):
                    if current_time - ent.spawn_time >= ent.duration:
                        self.entity_list.remove(ent)
            food_count = sum(1 for e in self.entity_list if isinstance(e, (GoodFood, PoisonFood)))

            if food_count < 3 and current_time >= self.next_food_spawn_time:
                entity_type = random.choice(["GoodFood", "PoisonFood"])
                new_entity = EntityFactory.get_entity(entity_type)
                self.entity_list.append(new_entity)
                self.next_food_spawn_time = current_time + self.food_spawn_interval

            self.window.fill((0, 0, 0))
            self.background.run()
            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.surf, ent.rect)
                if ent.name == 'Player1':
                    self.level_text(15, f'Player1 - Health {ent.health} | Score: {ent.score}', C_BLACK, (30, 25))
                    self.level_text(15, f'Player1 - Health {ent.health} | Score: {ent.score}', C_LIGHT_GREEN, (32, 26))

                if ent.name == 'Player2':
                    self.level_text(15, f'Player2 - Health {ent.health} | Score: {ent.score}', C_BLACK, (30, 50))
                    self.level_text(15, f'Player2 - Health {ent.health} | Score: {ent.score}', C_WHITE, (32, 51))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_FOOD:
                    food_count = sum(
                        1 for e in self.entity_list if isinstance(e, GoodFood) or isinstance(e, PoisonFood))
                    if food_count < 3:
                        if random.random() < 0.05:
                            self.entity_list.append(EntityFactory.get_entity("PoisonFood"))
                        else:
                            self.entity_list.append(EntityFactory.get_entity("GoodFood"))
                            food_count += 1
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            elif isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list[:]:
                    if isinstance(ent, Player):
                        if ent.health <= 0:
                            self.entity_list.remove(ent)
                        else:
                            found_player = True
                if not found_player:
                    result = self.game_over()
                    return result

             # Printed text
            self.level_text(25, f'Timeout: {self.timeout / 1000 :.1f}s',
                            C_BLACK, (650, 10))
            self.level_text(25, f'Timeout: {self.timeout / 1000 :.1f}s',
                            C_ORANGE, (652, 11))


            pygame.display.flip()

            #Collisions
            EntityMediator.verify_collision(self.entity_list)

    def show_level_start(self):
        if self.name == 'Level1':
            self.show_instruction()

        pygame.mixer_music.load('./asset/StartLevel.mp3')
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.play()

        countdown_seconds = 3

        for i in range(countdown_seconds, 0, -1):
            self.background.run()

            self.level_text(50, f"LEVEL {self.name.replace('Level', '')}", C_BLACK,
                            ((WIN_WIDTH / 2) - 150, WIN_HEIGHT / 2 - 150))
            self.level_text(50, f"LEVEL {self.name.replace('Level', '')}", C_WHITE,
                            ((WIN_WIDTH / 2) - 152, WIN_HEIGHT / 2 - 151))
            self.level_text(80, str(i), C_BLACK, ((WIN_WIDTH / 2) - 20, WIN_HEIGHT / 2 - 40))
            self.level_text(80,str(i),C_YELLOW,((WIN_WIDTH / 2) - 22, WIN_HEIGHT / 2 - 41))
            pygame.display.flip()
            pygame.time.delay(1000)

        self.background.run()

        self.level_text(50,f"LEVEL {self.name.replace('Level', '')}",C_BLACK,
                        ((WIN_WIDTH / 2) - 150, WIN_HEIGHT / 2 - 150) )
        self.level_text(50, f"LEVEL {self.name.replace('Level', '')}", C_WHITE,
                        ((WIN_WIDTH / 2) - 152, WIN_HEIGHT / 2 - 151))

        self.level_text(80,"GO!",C_BLACK,((WIN_WIDTH / 2) - 80, WIN_HEIGHT / 2 - 40))
        self.level_text(80, "GO!", C_ORANGE, ((WIN_WIDTH / 2) - 82, WIN_HEIGHT / 2 - 41))

        pygame.display.flip()
        pygame.time.delay(1000)

        self.background.run()
        pygame.display.flip()

    def show_instruction(self):
        self.background.run()

        text_lines = [
            "INSTRUCTIONS:",
            "- Player 1: use arrow keys to move.",
            "- Player 2 (in competitive mode):",
            "use A (left), D (right), W (up),",
            "and S (down) to move.",
            "- Collect fruits and vegetables to earn points.",
            "- Avoid poison roots or you'll lose health.",
            "- Survive until the timeout!",
        ]

        y = WIN_HEIGHT / 2 - 150
        for line in text_lines:
            self.level_text(20, line, C_BLACK, ((WIN_WIDTH / 2) - 480, y))
            self.level_text(20,line, C_WHITE,((WIN_WIDTH / 2) - 482, y))
            y += 40
        self.level_text(20, "Press any key to start!", C_BLACK, ((WIN_WIDTH / 2) - 250, WIN_HEIGHT / 2 + 180))
        self.level_text(20,"Press any key to start!",C_YELLOW,((WIN_WIDTH / 2) - 252, WIN_HEIGHT / 2 + 180))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def game_over(self):
        pygame.mixer_music.stop()

        pygame.mixer_music.load('./asset/PlayerDeath.mp3')
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.play()

        self.level_text(50, 'Game Over', C_BLACK, ((WIN_WIDTH / 2) - 250, 250))
        self.level_text(50, 'Game Over', C_YELLOW, ((WIN_WIDTH / 2) - 252, 251))
        pygame.display.flip()
        pygame.time.delay(3000)

        pygame.mixer_music.load('./asset/GameOverBG.mp3')
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.play(-1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer_music.stop()
                        return False  # avisa pro Level.run sair
            self.level_text(25, 'PRESS ESC TO RETURN MENU', C_BLACK, ((WIN_WIDTH / 2) - 280, 350))
            self.level_text(25, 'PRESS ESC TO RETURN MENU', C_WHITE, ((WIN_WIDTH / 2) - 282, 351))
            pygame.display.flip()




    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font("./asset/MenuBg.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

