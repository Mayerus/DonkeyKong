import pygame
from File import LoadFile
_AUTHOR_ = "Omri Mayer"
LEFT = 1


class StartScreen:

    def __init__(self, screen):
        self.screen = screen
        self.dk_clock = 0

    def menu(self, event, new_game_img, continue_img, barrels_list, Mario):
        start = True
        count = 0
        lives = 0
        self.screen.blit(new_game_img, [400, 400])
        self.screen.blit(continue_img, [400, 430])
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and 400 < x < 519 and 400 < y < 418:
            start = False
            Load_file = LoadFile("new_game")
            count, lives = Load_file.load(barrels_list, Mario)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and 400 < x < 519 and 430 < y < 450:
            start = False
            print("enter the game's name")
            filename = input()
            Load_file = LoadFile(filename)
            count, lives = Load_file.load(barrels_list, Mario)
        return start, count, lives

    def donkey_kong_animation(self, kongL, kongR):
        if self.dk_clock < 60:
            self.screen.blit(kongL, [300, 100])
            self.dk_clock += 1
        elif 59 < self.dk_clock < 120:
            self.screen.blit(kongR, [300, 100])
            self.dk_clock += 1
        if self.dk_clock == 120:
            self.dk_clock = 0
