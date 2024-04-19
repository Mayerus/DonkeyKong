import pygame
_AUTHOR_ = "Omri Mayer"


class Mario:

    def __init__(self, screen):
        self.jump_state = 0
        self.__pos_x = 117
        self.__pos_y = 650
        self.jump_finished = True
        self.direction = True
        self.screen = screen

    def set_pos(self, m_x, m_y):
        self.__pos_x = m_x
        self.__pos_y = m_y

    def freefall(self):
        self.__pos_y += 1

    def move(self, key, a_gradient, d_gradient, Vx=0, Vy=0):
        # move right
        if key == pygame.K_RIGHT:
            self.direction = True
            # move right on an ascending ramp
            if not (not (264.3 <= self.__pos_y - 2 * a_gradient < 298.7) and not (
                    444.4 <= self.__pos_y - 2 * a_gradient < 473.2)) or (
                    623.76 <= self.__pos_y - 2 * a_gradient < 652.7):
                self.__pos_x += 2
                self.__pos_y -= 2*a_gradient
            # move right on a descending ramp
            if not (not (172.662 <= self.__pos_y + 2 * d_gradient < 203.09) and not (
                    351.7 <= self.__pos_y + 2 * d_gradient < 382.53)) or \
                    533.529 <= self.__pos_y+2*d_gradient < 564.8:
                self.__pos_x += 2
                self.__pos_y += 2*d_gradient
            return "Right"
        # move left
        if key == pygame.K_LEFT:
            self.direction = False
            # move left on an ascending ramp
            if not (not (264.3 < self.__pos_y + 2 * a_gradient <= 292.2) and not (
                    444 < self.__pos_y + 2 * a_gradient <= 473.2)) or \
                    623.76 < self.__pos_y+2*a_gradient <= 652.7:
                self.__pos_x -= 2
                self.__pos_y += 2*a_gradient
            # move left on a descending ramp
            if not (not (172.662 < self.__pos_y - 2 * d_gradient <= 202.09) and not (
                    351.7 < self.__pos_y - 2 * d_gradient <= 382.53)) or \
                    533.529 < self.__pos_y-2*d_gradient <= 564.8:
                self.__pos_x -= 2
                self.__pos_y -= 2*d_gradient
                return "Left"
        # climb up (ladders)
        if key == pygame.K_UP and\
                ((not (not (687 <= self.__pos_x <= 705) or not (
                558.69 <= self.__pos_y - 1 < 630.95 or 376.76 <= self.__pos_y - 1 < 452.75 or
                196.76 <= self.__pos_y - 1 < 272.77))) or (not (not (160 <= self.__pos_x <= 175) or not (
                        468.357 < self.__pos_y - 1 <= 540.357 or 288.35 < self.__pos_y - 1 <= 360.357))) or
                 (299<self.__pos_x<310 and 284.2<=self.__pos_y-1<365) or (450<self.__pos_x<463 and 369<=self.__pos_y-1<460)
                 or (395 < self.__pos_x < 415 and 460 <= self.__pos_y-1 < 550) or (500<=self.__pos_x<507 and
                 95<self.__pos_y<=191)):
            self.__pos_y -= 1
        # climb down (ladders)
        if (key == pygame.K_DOWN and ((not(not (687 <= self.__pos_x <= 705)or not(
                not (not (558.69 < self.__pos_y + 1 <= 630.95) and not (376.76 < self.__pos_y + 1 <= 452.75)) or
                196.76 < self.__pos_y + 1 <= 272.77))) or (160 <= self.__pos_x <= 175 and
                (468.357 <= self.__pos_y+1 < 540.357 or 288.35 <= self.__pos_y+1 < 360.357)) or
                (299<self.__pos_x<310 and 284.2<self.__pos_y+1<=365) or (450<self.__pos_x<463 and 369<self.__pos_y+1<=460)
                or (395 < self.__pos_x < 415 and 460 < self.__pos_y + 1 <= 550) or (500<self.__pos_x<=507 and
                 98<=self.__pos_y<191))):
            self.__pos_y += 1

    def jump(self):
        # velocity > 0
        if self.jump_state < 288:
            self.__pos_y -= 1/6
            self.jump_state += 1
        # velocity < 0
        elif 287 < self.jump_state < 576:
            self.__pos_y += 1/6
            self.jump_state += 1
        # declares the jump have finished
        elif self.jump_state == 576:
            self.jump_finished = True
            self.jump_state = 0

    def get_pos(self):
        return self.__pos_x, self.__pos_y, self.direction
