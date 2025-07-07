import sys
from datetime import datetime

import pygame
from pygame import Surface, KEYDOWN, K_RETURN, K_BACKSPACE, Rect, K_ESCAPE
from pygame.font import Font

from code.const import C_YELLOW, MENU_OPTION, C_WHITE, SCORE_POS, MENU_STYLE, SCORE_TITLE, SCORE_WIN, C_BLACK
from code.dbProxy import DbProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/PlayerWin.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DbProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            for title in SCORE_WIN:
                width = title["initial_x"]
                height = title["initial_y"]
                for letra in title["text"]:
                    if letra != " ":
                        self.score_text(MENU_STYLE["text_font_big"], letra, MENU_STYLE["text_color_big"],
                                        (width, height))
                        self.score_text(MENU_STYLE["text_font_small"], letra, MENU_STYLE["text_color_small"],
                                        (width + MENU_STYLE["position_x"], height + MENU_STYLE["position_y"]))
                    width += title["spacing"]
            score = player_score[0]
            text = 'Enter Player 1 name (4 characters):'
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
            if game_mode == MENU_OPTION[1]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Enter Player 1 name (4 characters):'
                else:
                    score = player_score[1]
                    text = 'Enter Player 2 name (4 characters):'
            self.score_text(24, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 6:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode

            self.score_text(35, name, C_WHITE, SCORE_POS['Name'])

            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load('./asset/ScoreBg.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        for title in SCORE_TITLE:
            width = title["initial_x"]
            height = title["initial_y"]
            for letra in title["text"]:
                if letra != " ":
                    self.score_text(MENU_STYLE["text_font_big"], letra, MENU_STYLE["text_color_big"],
                                        (width, height))
                    self.score_text(MENU_STYLE["text_font_small"], letra, MENU_STYLE["text_color_small"],
                                        (width + MENU_STYLE["position_x"], height + MENU_STYLE["position_y"]))
                width += title["spacing"]
                self.score_text(24, "NAME SCORE  DATE", C_BLACK, SCORE_POS['Label0'])
                self.score_text(24, "NAME SCORE  DATE", C_YELLOW, SCORE_POS['Label1'])
        db_proxy = DbProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        while True:
            for player_score in list_score:
                id_, name, score, date = player_score
                self.score_text(24, f"{name} {score :05d} {date}", C_WHITE,
                                SCORE_POS[list_score.index(player_score)])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

            pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("./asset/MenuBg.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_date}"
