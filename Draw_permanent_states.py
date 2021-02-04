import pygame


class Draw_permanent_states:
    def __init__(self, screen, window_width, window_height, game_level):
        self.__window_width = window_width
        self.__window_height = window_height
        coin_surf = pygame.image.load('Coin.png')
        self.__coin_scale = pygame.transform.scale(coin_surf, (int(coin_surf.get_width() // 15), int(coin_surf.get_height() // 15)))
        self.__coin_rect = self.__coin_scale.get_rect()
        self.__draw_half_face_coin = False
        self.__screen = screen
        self.__game_level = game_level
        self.__fontobj = pygame.font.SysFont('Agency FB', 25)
        
    def draw_permanent_states(self, n_of_coins, FPS_counter):
        self.__draw_n_of_coin(n_of_coins, FPS_counter)
        self.__draw_game_level()

    def raise_game_level(self):
        self.__game_level += 1

    def __draw_n_of_coin(self, n_of_coins, FPS_counter):
        txt_image = self.__fontobj.render(str(n_of_coins), True, (129, 129, 129))
        txt_rect = txt_image.get_rect(topright=(self.__window_width - 7, 0))
        self.__screen.blit(txt_image, txt_rect)
        self.__coin_rect.topright = (txt_rect.topleft[0] - 2, txt_rect.topleft[1] + 4)
        self.__update_coin_image_pos(FPS_counter)
        if self.__draw_half_face_coin:
            coin_width = 4
            coin_height = self.__coin_rect.height
            pygame.draw.rect(self.__screen, (247, 205, 17), (self.__coin_rect.centerx - coin_width // 2,
                                                             self.__coin_rect.centery - coin_height / 2,
                                                             coin_width, coin_height))

        else:
            self.__screen.blit(self.__coin_scale, self.__coin_rect)

    def __draw_game_level(self):
        txt = 'game level: ' + str(self.__game_level)
        txt_image = self.__fontobj.render(txt, True, (129, 129, 129))
        txt_rect = txt_image.get_rect(topleft=(7, 0))
        self.__screen.blit(txt_image, txt_rect)

    def __update_coin_image_pos(self, FPS_counter):
        if FPS_counter % 25 == 0:
            self.__draw_half_face_coin = not self.__draw_half_face_coin
