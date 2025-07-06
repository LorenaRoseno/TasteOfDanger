# C
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 128)
C_LIGHT_GREEN = (144, 238, 144)
C_BLACK = (0, 0, 0)


# M
MENU_OPTION = ('--NEW GAME-- (1 PLAYER)',
               '-NEW GAME- (2 PLAYERS - COMPETITIVE)',
               'SCORE',
               'EXIT')

WIN_WIDTH = 1067
MENU_TITLES = [
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


# W

WIN_WIDTH = 1067
WIN_HEIGHT = 600
