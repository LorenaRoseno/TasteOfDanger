import pygame
from pygame import Surface


class Background:
    def __init__(self, window: Surface, level_name: str):
        self.window = window
        self.level_name = level_name
        self.surf = pygame.image.load(f'./asset/{self.level_name}.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        self.window.blit(self.surf, self.rect)

    def show_food(self, ):
        pass
