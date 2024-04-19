import os
import pygame
import math
_AUTHOR_ = "Omri Mayer"
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
LIGHT_BLUE = (0, 198, 192)


class Ramp:
    pygame.init()

    def __init__(self, x0, x1, y0, y1, screen):
        self.__GAP = 15
        self.__x0 = x0
        self.__x1 = x1
        self.__y0 = y0
        self.__y1 = y1
        self.__length = math.sqrt(pow((self.__x1 - self.__x0),2) + pow((self.__y1 - self.__y0),2))
        self.__Dx = self.__x1 - self.__x0
        self.__Dy = self.__y1 - self.__y0
        self.screen = screen
        pygame.draw.line(self.screen, PINK, [x0, y0], [x1, y1], 3)
        pygame.draw.line(self.screen, BLUE, [x0, y0 - self.__GAP], [x1, y1 - self.__GAP], 3)


class Ladder:
    pygame.init()

    def __init__(self, x0, y0, length, screen):
        self.thickness = 15
        self.__LeftX = x0
        self.__RightX = self.__LeftX + self.thickness
        self.__BottomY = y0
        self.__length = length
        self.__TopY = self.__BottomY - length
        self.screen = screen
        pygame.draw.line(self.screen, LIGHT_BLUE, [self.__LeftX, self.__BottomY],
                         [self.__LeftX, self.__BottomY - self.__length], 3)
        pygame.draw.line(self.screen, LIGHT_BLUE, [self.__LeftX + self.thickness, self.__BottomY],
                         [self.__LeftX + self.thickness, self.__BottomY - self.__length], 3)
        y = self.__BottomY - 10
        while y > y0 - length:
            pygame.draw.line(screen, LIGHT_BLUE, [self.__LeftX, y], [self.__LeftX + self.thickness, y], 3)
            y -= 10


class Background:
    # fill screen and show
    def __init__(self, screen_1, barrels_list, mario):
        self.screen = screen_1
        self.Mario = mario
        self.Barrel_1 = barrels_list[0]
        self.Barrel_2 = barrels_list[1]
        self.Barrel_3 = barrels_list[2]
        self.Barrel_4 = barrels_list[3]
        self.Barrel_5 = barrels_list[4]
        self.Barrel_6 = barrels_list[5]
        self.barrels_list = [self.Barrel_1, self.Barrel_2, self.Barrel_3, self.Barrel_4, self.Barrel_5, self.Barrel_6]

    def level_1_background(self, marioR_img, marioL_img, peach_img, barrel_img, counter, lives, heart_img, kong_hold_img,
                           kong_throw_img):
        self.screen.fill(BLACK)
        do_throws = False
        # donkey kong movement animation
        for i in range(0, 6, 1):
            if self.barrels_list[i].kong_state > 0 and counter > i*120:
                self.screen.blit(kong_throw_img, [70, 145])
                do_throws = True
        if not do_throws:
            self.screen.blit(kong_hold_img, [60, 145])
        # hearts drawing
        j = 0
        for i in range(3, lives, -1):
            self.screen.blit(heart_img, [800 + j, 100])
            j += 15
        # level l ramps
        ramp1 = Ramp(0,   935, 700, 670, self.screen)
        ramp2 = Ramp(0,   835, 580, 610, self.screen)
        ramp3 = Ramp(100, 935, 520, 490, self.screen)
        ramp4 = Ramp(0,   835, 400, 430, self.screen)
        ramp5 = Ramp(100, 935, 340, 310, self.screen)
        ramp6 = Ramp(0,   835, 220, 250, self.screen)
        # Princess Peach's ramp
        ramp_peach = Ramp(360, 520, 140, 140, self.screen)
        # left and right ladders
        ladder_1 = Ladder(700, 660, 52, self.screen)
        ladder_2 = Ladder(170, 570, 52, self.screen)
        ladder_3 = Ladder(700, 480, 52, self.screen)
        ladder_4 = Ladder(170, 390, 52, self.screen)
        ladder_5 = Ladder(700, 300, 52, self.screen)
        # peach and DK ladders
        ladder_6 = Ladder(504, 222, 80, self.screen)
        ladder_7 = Ladder(340, 213, 215, self.screen)
        ladder_8 = Ladder(290, 212, 210, self.screen)
        # more ladders
        ladder_9 = Ladder(305,  395.3, 61, self.screen)
        ladder10 = Ladder(460, 490,   71, self.screen)
        ladder11 = Ladder(405, 580.7, 70, self.screen)
        m_x, m_y, direction = self.Mario.get_pos()
        if direction:
            self.screen.blit(marioR_img, [m_x, m_y])
        else:
            self.screen.blit(marioL_img, [m_x, m_y])
        b_x, b_y = self.Barrel_1.get_pos()
        self.screen.blit(barrel_img, [b_x, b_y])
        b_x2, b_y2 = self.Barrel_2.get_pos()
        if counter > 180:
            self.screen.blit(barrel_img, [b_x2, b_y2])
        b_x3, b_y3 = self.Barrel_3.get_pos()
        if counter > 360:
            self.screen.blit(barrel_img, [b_x3, b_y3])
        b_x4, b_y4 = self.Barrel_4.get_pos()
        if counter > 540:
            self.screen.blit(barrel_img, [b_x4, b_y4])
        b_x5, b_y5 = self.Barrel_5.get_pos()
        if counter > 720:
            self.screen.blit(barrel_img, [b_x5, b_y5])
        b_x6, b_y6 = self.Barrel_6.get_pos()
        if counter > 900:
            self.screen.blit(barrel_img, [b_x6, b_y6])
        self.screen.blit(peach_img, [368, 69])
        pygame.display.flip()

    def ObjPos(self, counter, lives):
        """returns all of the objects coordinates, conter and life status"""
        print("choose a name for your current game state")
        filename = input()
        while os.path.exists(filename + '.txt'):
            print("a game with such a name already exists, please choose another name")
            filename = input()
        state_file = open(filename + ".txt", 'w')
        m_x,  m_y, direction = self.Mario.get_pos()
        b_x,  b_y  = self.Barrel_1.get_pos()
        b_x2, b_y2 = self.Barrel_2.get_pos()
        b_x3, b_y3 = self.Barrel_3.get_pos()
        b_x4, b_y4 = self.Barrel_4.get_pos()
        b_x5, b_y5 = self.Barrel_5.get_pos()
        b_x6, b_y6 = self.Barrel_6.get_pos()
        state_file.write(str(m_x)  + "," + str(m_y)  + "\n" +
                         str(b_x)  + "," + str(b_y)  + ";" +
                         str(b_x2) + "," + str(b_y2) + ";" +
                         str(b_x3) + "," + str(b_y3) + ";" +
                         str(b_x4) + "," + str(b_y4) + ";" +
                         str(b_x5) + "," + str(b_y5) + ";" +
                         str(b_x6) + "," + str(b_y6) + ";" +
                         "\n" + str(counter) + "\n" + str(lives))
        state_file.close()
