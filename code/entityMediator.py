import pygame

from code.entity import Entity
from code.goodFood import GoodFood
from code.player import Player
from code.poisonFood import PoisonFood


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        pass

    @staticmethod
    def __verify_collision_good_food(ent1, ent2, entity_list, to_remove):
        if isinstance(ent1, Player) and isinstance(ent2, GoodFood):
            if EntityMediator.__is_colliding(ent1, ent2):
                points = ent2.get_points()
                ent1.score += points
                pygame.mixer.Sound('./asset/EatGoodFood.mp3').play()
                to_remove.append(ent2)
        elif isinstance(ent1, GoodFood) and isinstance(ent2, Player):
            EntityMediator.__verify_collision_good_food(ent2, ent1, entity_list, to_remove)

    @staticmethod
    def __verify_collision_poison_food(ent1, ent2, entity_list, to_remove):
        if isinstance(ent1, Player) and isinstance(ent2, PoisonFood):
            if EntityMediator.__is_colliding(ent1, ent2):
                ent1.health -= ent2.damage
                pygame.mixer.Sound('./asset/EatPoisonFood.mp3').play()
                to_remove.append(ent2)
        elif isinstance(ent1, PoisonFood) and isinstance(ent2, Player):
            EntityMediator.__verify_collision_poison_food(ent2, ent1, entity_list, to_remove)

    @staticmethod
    def __is_colliding(ent1, ent2):
        return (
                ent1.rect.right >= ent2.rect.left and
                ent1.rect.left <= ent2.rect.right and
                ent1.rect.bottom >= ent2.rect.top and
                ent1.rect.top <= ent2.rect.bottom
        )

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        to_remove = []

        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_good_food(entity1, entity2, entity_list, to_remove)
                EntityMediator.__verify_collision_poison_food(entity1, entity2, entity_list, to_remove)


        for ent in to_remove:
            if ent in entity_list:
                entity_list.remove(ent)

