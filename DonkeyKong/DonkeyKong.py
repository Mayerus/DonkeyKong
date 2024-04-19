import pygame
from Mario import Mario
from Barrel import Barrel
from DK_Objects import *
from HitEventListener import HitEventListener
from StartScreen import StartScreen
from File import LoadFile
_AUTHOR_ = "Omri Mayer"


# Constants
WINDOW_WIDTH = 935
WINDOW_HEIGHT = 715
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
# mouse buttons
LEFT = 1
SCROLL = 2
RIGHT = 3
# FPS
REFRESH_RATE = 60

BARRELS_RATE = 180
start = True
let_continue = True
game_over_state = False
dk_clock = 0
lives = 0
count = 0
won = False

# Init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Donkey Kong")
clock = pygame.time.Clock()

# moving objects
Mario = Mario(screen)

Barrel_1 = Barrel()
Barrel_2 = Barrel()
Barrel_3 = Barrel()
Barrel_4 = Barrel()
Barrel_5 = Barrel()
Barrel_6 = Barrel()
barrels_list = [Barrel_1, Barrel_2, Barrel_3, Barrel_4, Barrel_5, Barrel_6]

Start_screen = StartScreen(screen)

# hit of mario and barrels event listener
is_hit = HitEventListener(Mario, barrels_list)

L1_background1 = Background(screen, barrels_list, Mario)

# images
# mario images
# moving to the right mario
marioR = pygame.image.load('Mario.png').convert()
marioR = pygame.transform.scale(marioR, (24, 32))
# moving to the left mario
marioL = pygame.image.load('MarioL.png').convert()
marioL = pygame.transform.scale(marioL, (24, 32))
marioL.set_colorkey(WHITE)

peach = pygame.image.load('princess_peach.png').convert()
peach = pygame.transform.scale(peach, (39, 61))
peach.set_colorkey(BLACK)

# spinning barrel sprites
barrel = pygame.image.load('barrel.png').convert()
barrel = pygame.transform.scale(barrel, (24, 24))
barrel.set_colorkey(WHITE)

barrel_2 = pygame.image.load('barrel2.png').convert()
barrel_2 = pygame.transform.scale(barrel_2, (24, 24))
barrel_2.set_colorkey(WHITE)

barrel_3 = pygame.image.load('barrel3.png').convert()
barrel_3 = pygame.transform.scale(barrel_3, (24, 24))
barrel_3.set_colorkey(WHITE)

barrel_4 = pygame.image.load('barrel4.png').convert()
barrel_4 = pygame.transform.scale(barrel_4, (24, 24))
barrel_4.set_colorkey(WHITE)

dk_new_game_button = pygame.image.load('dk_new_game_button.PNG')
dk_continue_game_button = pygame.image.load('dk_continue_game_button.PNG')

game_over = pygame.image.load('gameover.PNG').convert()
game_over.set_colorkey(BLACK)

kong_L = pygame.image.load('Kongleft.PNG').convert()

kong_R = pygame.image.load('Kongright.PNG').convert()

heart = pygame.image.load('Heart.png').convert()
heart.set_colorkey(WHITE)

warning = pygame.image.load('warning.png').convert()
warning = pygame.transform.scale(warning, (30, 30))

kong_hold = pygame.image.load('kong_hold.png').convert()
kong_hold = pygame.transform.scale(kong_hold, (80, 64))
kong_hold.set_colorkey(WHITE)

kong_throw = pygame.image.load('kongthrow.png').convert()
kong_throw = pygame.transform.scale(kong_throw, (80, 64))
kong_throw.set_colorkey(WHITE)

you_won = pygame.image.load('dk_you won.png').convert()


def game_screen(count):
    # barrels instantaneous position
    Bx, By = barrels_list[0].get_pos()
    Bx2, By2 = barrels_list[1].get_pos()
    Bx3, By3 = barrels_list[2].get_pos()
    Bx4, By4 = barrels_list[3].get_pos()
    Bx5, By5 = barrels_list[4].get_pos()
    Bx6, By6 = barrels_list[5].get_pos()
    barrels_pos_list = [[Bx, By], [Bx2, By2], [Bx3, By3], [Bx4, By4], [Bx5, By5], [Bx6, By6]]
    # print barrels on screen and calculate barrels and mario movement
    for i in range(0, 6):
        if count > i*BARRELS_RATE:
            barrels_list[i].complete_orientation(screen, marioR, marioL, peach, barrel, L1_background1, count, lives, heart, kong_hold, kong_throw)
        L1_background1.level_1_background(marioR, marioL, peach, barrel, count, lives, heart, kong_hold, kong_throw)
    if event.type == pygame.KEYDOWN and event.key != pygame.K_SPACE:
        L1_background1.level_1_background(marioR, marioL, peach, barrel, count, lives, heart, kong_hold, kong_throw)
        Mario.move(event.key, 31 / 931, 31 / 834, 0, 0)
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        for i in range(0, 577):
            Mario.jump()
            for k in range(0, 6):
                if count > k*BARRELS_RATE:
                    if (not (not (barrels_pos_list[k][0] >= 833) or not
                    (611 > barrels_pos_list[k][1] > 560 or 394 > barrels_pos_list[k][1] > 382.451 or
                     220 > barrels_pos_list[k][1] > 203.04))) or (not (not (barrels_pos_list[k][0] < 75) or not
                            (298.6 < barrels_pos_list[k][1] < 296) and not (465 < barrels_pos_list[k][1] < 480))):
                        while screen.get_at(((int(barrels_pos_list[k][0]) + 24), int(By + 24))) != BLUE:
                            barrels_pos_list[k][0], barrels_pos_list[k][1] = barrels_list[k].get_pos()
                            barrels_list[k].freefall()
                    barrels_list[k].move(31 / 931, 31 / 834, screen.get_at(((int(barrels_pos_list[k][0]) + 12),
                            int(barrels_pos_list[k][1] + 24))), 0.08)
            L1_background1.level_1_background(marioR, marioL, peach, barrel, count, lives, heart, kong_hold, kong_throw)
    Mx, My, c = Mario.get_pos()
    if My < 96:
        screen.blit(you_won, [400, 360])
        return
    # mario falling from the edges of the ramps
    if (Mx >= 830 and (not ((not (611 > My > 560) and not (400 > My > 382.451)) and not (220 > My > 203.04)))) \
            or (not (not (Mx < 75) or not (297 > My < 311) and not (470 < My < 480))):
        while screen.get_at(((int(Mx) + 24), int(My + 32))) != BLUE:
            Mx, My, c = Mario.get_pos()
            Mario.freefall()
            L1_background1.level_1_background(marioR, marioL, peach, barrel, count, lives, heart, kong_hold, kong_throw)
    L1_background1.level_1_background(marioR, marioL, peach, barrel, count, lives, heart, kong_hold, kong_throw)


finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if not game_over_state and not start:
                L1_background1.ObjPos(count, lives)
            finish = True
        # editor tool - when clicking on the left mouse button it prints the mouse's pointer coordinates on canvas
        # and also mario's coordinates on canvas
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            print(pygame.mouse.get_pos())
            a, b, c = Mario.get_pos()
            print("mario({},{})".format(a, b))
    # start screen
    if start:
        start = True
        Start_screen.donkey_kong_animation(kong_L, kong_R)
        start, temp_count, lives = Start_screen.menu(event, dk_new_game_button, dk_continue_game_button, barrels_list, Mario)
        count = temp_count
    # if the user let the game begin
    if let_continue and not start:
        try:
            game_screen(count)
        except IndexError or range:
            screen.blit(warning, [300, 100])
            pygame.display.flip()
            L1_background1.ObjPos(count, lives)
            break
        # stopwatch variable
        count += 1
    pygame.display.flip()
    clock.tick(REFRESH_RATE)
    # hit/collide of mario and barrels event listener
    if is_hit.hit_listener() and lives < 2:
        renew_game = LoadFile("new_game")
        renew_game.load(barrels_list, Mario)
        lives += 1
        count = 0
    if is_hit.hit_listener() and lives == 2:
        screen.blit(game_over, [400, 360])
        pygame.display.flip()
        let_continue = False
        game_over_state = True
