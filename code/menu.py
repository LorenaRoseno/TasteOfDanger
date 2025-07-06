import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import MENU_OPTION, WIN_WIDTH, C_WHITE, MENU_TITLES, MENU_STYLE, C_LIGHT_GREEN


class Menu:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/MenuBg.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # Draw images
            self.window.blit(source=self.surf, dest=self.rect)
            for title in MENU_TITLES:
                width = title["initial_x"]
                height = title["initial_y"]

                for letra in title["text"]:
                    if letra != " ":
                        self.menu_text(
                            MENU_STYLE["text_font_big"],
                            letra,
                            MENU_STYLE["text_color_big"],
                            (width, height)
                        )
                        self.menu_text(
                            MENU_STYLE["text_font_small"],
                            letra,
                            MENU_STYLE["text_color_small"],
                            (width + MENU_STYLE["position_x"], height + MENU_STYLE["position_y"])
                        )
                    width += title["spacing"]

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], C_LIGHT_GREEN, ((WIN_WIDTH / 2), 300 + 50 * i))
                else:
                    self.menu_text(25, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 300 + 50 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("./asset/MenuBg.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
