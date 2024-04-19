import pygame
import random
from DK_Objects import *
from StartScreen import StartScreen
_AUTHOR_ = "Omri Mayer"
BLUE = (0, 0, 255)


class Barrel:

    def __init__(self):
        self.jump_state = 0
        self.__B_pos_x = 121
        self.__B_pos_y = 183
        self.irregular_movement = False
        self.state = 0
        self.kong_state = 1

    def freefall(self):
        self.__B_pos_y += 1

    def move(self, a_gradient, d_gradient, color, prop):
        rand = random.randint(0, 7)
        # climb down (ladders)
        if ((697 <= self.__B_pos_x <= 705 and
             (558.69 < self.__B_pos_y + 1.3 <= 640.95 or 376.76 < self.__B_pos_y + 1.3 <= 462.75 or
              204.76 < self.__B_pos_y + 1.3 <= 281.77)) or (170 <= self.__B_pos_x <= 185 and
            (468.357 <= self.__B_pos_y + 1.3 < 550.357 or 298.35 <= self.__B_pos_y + 1.3 < 369)) or
            (302 < self.__B_pos_x < 305 and 284.2 < self.__B_pos_y + 1.3 <= 373) or
             455 < self.__B_pos_x < 460 and 369 < self.__B_pos_y + 1.3 <= 470 or
                (395 < self.__B_pos_x < 405 and 460 < self.__B_pos_y + 1 <= 560)) and\
                (self.irregular_movement == True or rand == 4):
            self.irregular_movement = True
            self.__B_pos_y += 1.3*prop
            if color == BLUE and self.state == 33:
                self.state = 1
        # move right,
        # descending ramp
        elif 172.662 <= self.__B_pos_y+2*d_gradient < 209.6 or 351.7 <= self.__B_pos_y+2*d_gradient < 396 or \
                533.529 <= self.__B_pos_y+2*d_gradient < 578.8:
            self.irregular_movement = False
            self.__B_pos_x += 2.6*prop
            self.__B_pos_y += 2.6*d_gradient*prop
        # move left
        # ascending ramp
        elif 264.3 < self.__B_pos_y+2*a_gradient <= 303 or 444 < self.__B_pos_y+2*a_gradient <= 485 or \
                623.76 < self.__B_pos_y+2*a_gradient <= 660:
            self.irregular_movement = False
            self.__B_pos_x -= 2.6*prop
            self.__B_pos_y += 2.6*a_gradient*prop

    def set_pos(self, b_x, b_y):
        self.__B_pos_x = b_x
        self.__B_pos_y = b_y
        self.kong_state = 1

    def get_pos(self):
        return self.__B_pos_x, self.__B_pos_y

    def complete_orientation(self, screen, marioR, marioL, peach, barrel, L1_background, count, lives, heart, kong_hold, kong_throw_img):
        if not (not (self.__B_pos_x <= 135) or not ((self.__B_pos_y + 2 * 31 / 931) >= 658)):
            Barrel.__init__(self)
        if self.kong_state > 0:
            self.kong_state += 1
        if self.kong_state == 31:
            self.kong_state = 0
        if not (not (not (not (self.__B_pos_x >= 833) or not (
                not (not (611 > self.__B_pos_y > 560) and not (
                        400 > self.__B_pos_y > 382.451)) or 220 > self.__B_pos_y > 203.04))) and not (
                not (not (self.__B_pos_x < 75) or not (298.6 < self.__B_pos_y < 304) and not (
                        470 < self.__B_pos_y < 485)))):
            while screen.get_at(((int(self.__B_pos_x + 24)), int(self.__B_pos_y + 24))) != BLUE:
                Barrel.freefall(self)
            L1_background.level_1_background(marioR, marioL, peach, barrel, count, lives, heart, kong_hold, kong_throw_img)
        Barrel.move(self, 31 / 931, 31 / 834, screen.get_at(((int(self.__B_pos_x) + 12), int(self.__B_pos_y + 24))), 1)
