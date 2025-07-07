import random

from code.const import WIN_HEIGHT, WIN_WIDTH, FRUIT_POINT, VEGETABLE_POINT
from code.goodFood import GoodFood
from code.player import Player
from code.poisonFood import PoisonFood


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Player1':
                return Player('Player1', (WIN_WIDTH / 2 - 200, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (WIN_WIDTH / 2 + 200, WIN_HEIGHT / 2 - 30))

            case 'GoodFood':
                food_type = random.choice(['fruit', 'vegetable'])
                name = food_type
                if food_type == "fruit":
                    fruit = [f'GFFru{i}' for i in range(1, 10)]
                    name = random.choice(fruit)

                elif food_type == "vegetable":
                    vegetable = [f'GFVeg{i}' for i in range(1, 5)]
                    name = random.choice(vegetable)

                position = (
                    random.randint(0, WIN_WIDTH - 50),
                    random.randint(int(WIN_HEIGHT / 2), WIN_HEIGHT - 150)
                )
                return GoodFood(name, position)

            case 'PoisonFood':
                name = random.choice([f'PF{i}' for i in range(1, 5)])
                position = (
                    random.randint(0, WIN_WIDTH - 50),
                    random.randint(int(WIN_HEIGHT / 2), WIN_HEIGHT - 150)
                )
                return PoisonFood(name, position)

        return None
