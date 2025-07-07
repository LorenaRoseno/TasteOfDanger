# C
import pygame

C_WHITE = (255, 255, 255)
C_YELLOW = (218, 165, 32)
C_LIGHT_GREEN = (144, 238, 144)
C_BLACK = (0, 0, 0)
C_GREY = (128,128,128)
C_ORANGE = (255, 140, 0)
# E
ENTITY_DAMAGE = {
    'Player1': 1,
    'Player2': 1,
    'GFFru1': 0,
    'GFFru2': 0,
    'GFFru3': 0,
    'GFFru4': 0,
    'GFFru5': 0,
    'GFFru6': 0,
    'GFFru7': 0,
    'GFFru8': 0,
    'GFFru9': 0,
    'GFVeg1': 0,
    'GFVeg2': 0,
    'GFVeg3': 0,
    'GFVeg4': 0,
    'GFVeg5': 0,
    'PF1': 25,
    'PF2': 25,
    'PF3': 25,
    'PF4': 25,
    'PF5': 25
}
ENTITY_HEALTH = {
    'Player1': 150,
    'Player2': 150,
    'GFFru1': 1,
    'GFFru2': 1,
    'GFFru3': 1,
    'GFFru4': 1,
    'GFFru5': 1,
    'GFFru6': 1,
    'GFFru7': 1,
    'GFFru8': 1,
    'GFFru9': 1,
    'GFVeg1': 1,
    'GFVeg2': 1,
    'GFVeg3': 1,
    'GFVeg4': 1,
    'GFVeg5': 1,
    'PF1': 1,
    'PF2': 1,
    'PF3': 1,
    'PF4': 1,
    'PF5': 1
}

ENTITY_SCORE = {
    'Player1': 0,
    'Player2': 0,
}

ENTITY_SPEED = {
    'Player1': 4,
    'Player2': 4,
}

EVENT_FOOD = pygame.USEREVENT + 1

EVENT_TIMEOUT = pygame.USEREVENT + 2

# F
FRUIT_POINT = 50

# M
MENU_OPTION = ('--NEW GAME-- (1 PLAYER)',
               '-NEW GAME- (2 PLAYERS - COMPETITIVE)',
               'SCORE',
               'EXIT')

WIN_WIDTH = 1067
MENU_TITLE = [
    {
        "text": "Taste",
        "initial_x": (WIN_WIDTH / 2) - 200,
        "initial_y": 80,
        "spacing": 50
    },
    {
        "text": "Of",
        "initial_x": (WIN_WIDTH / 2) + 100,
        "initial_y": 90,
        "spacing": 50
    },
    {
        "text": "Danger",
        "initial_x": (WIN_WIDTH / 2) - 130,
        "initial_y": 170,
        "spacing": 50
    }
]

MENU_STYLE = {
    "text_font_big": 62,
    "text_font_small": 58,
    "text_color_big": C_BLACK,
    "text_color_small": C_YELLOW,
    "position_x": 2,
    "position_y": 0
}

#  P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
# S
WIN_WIDTH = 576
SCORE_WIN = [
    {
        "text": "You Win!",
        "initial_x": (WIN_WIDTH / 2) + 100,
        "initial_y": 200,
        "spacing": 50
    }
]
SCORE_TITLE = [
    {
        "text": "TOP 10 SCORE",
        "initial_x": (WIN_WIDTH / 2) - 25,
        "initial_y": 50,
        "spacing": 50
    }
]

SCORE_POS = {'Title': ((WIN_WIDTH / 2)  , 70),
             'EnterName': ((WIN_WIDTH / 2)+ 280, 300),
             'Label0': ((WIN_WIDTH / 2) + 258, 140),
             'Label1': ((WIN_WIDTH / 2) + 260, 141),
             'Name': ((WIN_WIDTH / 2) + 200 , 350),
             0: ((WIN_WIDTH / 2) + 270, 190),
             1: ((WIN_WIDTH / 2) + 270, 220),
             2: ((WIN_WIDTH / 2) + 270, 250),
             3: ((WIN_WIDTH / 2) + 270, 280),
             4: ((WIN_WIDTH / 2) + 270, 310),
             5: ((WIN_WIDTH / 2) + 270, 340),
             6: ((WIN_WIDTH / 2) + 270 , 370),
             7: ((WIN_WIDTH / 2) + 270, 400),
             8: ((WIN_WIDTH / 2) + 270, 430),
             9: ((WIN_WIDTH / 2) + 270, 460)
             }

SPAWN_TIME = {'Level1': 4000,
              'Level2': 3500,
              'Level3': 3000,
              'Level4': 2000,
              }

# T
TIMEOUT_LEVEL = 20000

TIMEOUT_STEP = 100

# V
VEGETABLE_POINT = 70

# W

WIN_WIDTH = 1067
WIN_HEIGHT = 600
