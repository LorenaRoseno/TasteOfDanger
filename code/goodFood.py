import pygame

from code.const import FRUIT_POINT, VEGETABLE_POINT
from code.entity import Entity


class GoodFood(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.spawn_time = pygame.time.get_ticks()
        self.duration = 3000


    def move(self):
        pass

    def get_points(self):
        if "GFFru" in self.name:
            return FRUIT_POINT
        elif "GFVeg" in self.name:
            return VEGETABLE_POINT
        else:
            return 0