import pygame

from code.entity import Entity


class PoisonFood(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.spawn_time = pygame.time.get_ticks()
        self.duration = 3000

    def move(self, ):
        pass
