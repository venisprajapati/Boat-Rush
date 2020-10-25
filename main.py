"""
The main Boat-Rush game
author:@venisprajapati
"""

import pygame
from water import Water
from objects import objects
from pygame import mixer

gamePlayerName = 'Venis Prajapati'

# Game heading and initializing section /*/*/*/

# Initialize Pygame
pygame.init()

# Screen set mode
screen = pygame.display.set_mode((764, 732))  # ( width, height )

# Title And Logo
pygame.display.set_caption("Boat Rush")  # display caption
icon = pygame.image.load('boat_logo.png')
pygame.display.set_icon(icon)

# Background Sound
mixer.music.load('Crisp_Ocean_Waves.wav')
mixer.music.play(-1)

# Boat section /*/*/*/

# Boat
boat_img = pygame.image.load('cargo_ship_1.png')
boat_X = 355
boat_Y = 505
boat_X_change = 0
boat_Y_change = 0


def boat_move(boat_X):
    screen.blit(boat_img, (boat_X, boat_Y))


# Water Section /*/*/*/

# defining water class
w1 = Water()


# Movement of water..
def moving_water():
    for i in range(w1.wave_len):
        for j in range(w1.wave_wid):
            screen.blit(w1.W_wave_img[i][j], (w1.W_wave_X[i][j], w1.W_wave_Y[i][j]))
            w1.wave_move()
    # pygame.display.update()


# Object Section /*/*/*/

# Objects making
ob1 = objects()

# Speed of object
speed_font = pygame.font.SysFont('consolas', 28)

# Level ..
levels_font = pygame.font.SysFont('impact', 38)


# object moving function
def objects_move():
    ticks = pygame.time.get_ticks()
    seconds = int(ticks / 1000 % 60)
    if seconds >= 50:
        status = 6
    elif seconds >= 40:
        status = 5
    elif seconds >= 30:
        status = 4
    elif seconds >= 20:
        status = 3
    elif seconds >= 10:
        status = 2
    else:
        status = 1

    # Sharks
    for i in range(ob1.shark_s):
        screen.blit(ob1.shark_img[i], (ob1.shark_X[0][i], ob1.shark_Y[0][i]))
        ob1.shark_movement()

    # Objects
    for j in range(ob1.object_s):
        screen.blit(ob1.object_img[j], (ob1.object_X[0][j], ob1.object_Y[0][j]))
        ob1.object_movement(status)
        speed_text = speed_font.render(str(int(ob1.object_Y_speed * 100)).format() + " knots", True, (0, 38, 0))
        screen.blit(speed_text, (612, 10))
        # print(ob1.object_Y)

    # Levels
    levels_text = levels_font.render("Level: " + str(status), True, (0, 0, 68))
    screen.blit(levels_text, (322, 10))


# Graphics View section /*/*/*/

# Timer Font view
clock = pygame.time.Clock()
time_font = pygame.font.SysFont('consolas', 28)

# timer_text = time_font.render(clock, True, (34, 139, 34))


# Timer function
global final_time
final_time = 'None'


def timer_fun(game_run):
    ticks = pygame.time.get_ticks()
    millis = int(ticks % 1000 / 10)
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 24)
    out = '{minutes:1d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
    # out = '{seconds:02d}:{millis:01d}'.format(millis=millis, seconds=seconds)
    if game_run:
        timer_text = time_font.render(out, True, (0, 38, 0))  # 0, 51, 102
        screen.blit(timer_text, (20, 10))
    else:
        if final_time == 'None':
            # print(out)
            return out


# Finish Game /*/*/*/

# Finishing game font
finish_game_font = pygame.font.SysFont('comicsansms', 32)

finish_flag = pygame.image.load('flag_2.png')


# Game finishing fun
def finish_game():
    finish_game_text_1 = finish_game_font.render('Game finished by the player ..', True, (255, 255, 255))
    finish_game_text_2 = finish_game_font.render(gamePlayerName, True, (255, 255, 255))
    finish_game_text_3 = finish_game_font.render("Let's have a party .. :) ", True, (255, 255, 255))
    screen.blit(finish_game_text_1, (100, 80))
    screen.blit(finish_game_text_2, (100, 180))
    screen.blit(finish_game_text_3, (100, 280))

    screen.blit(finish_flag, (125, 510))


# Quit button /*/*/*/

# Quit game font
quit_button_font = pygame.font.SysFont('comicsansms', 32)
quit_button_text = quit_button_font.render('Quit', True, (0, 0, 0))


# Quit game function
def quit_game():
    if 330 <= mouse[0] <= 430 and 420 <= mouse[1] <= 470:
        pygame.draw.rect(screen, (170, 170, 170), [330, 420, 100, 50])
    else:
        pygame.draw.rect(screen, (100, 100, 100), [330, 420, 100, 50])
    screen.blit(quit_button_text, (340, 420))


# Game Over /*/*/*/

# Game over font
game_over_font = pygame.font.SysFont('comicsansms', 81)
final_time_font = pygame.font.SysFont('consolas', 38)
player_name_font = pygame.font.SysFont('dejavusans', 42)


# Game over Function
def game_over():
    player_name_text = player_name_font.render('Player name is: ' + gamePlayerName, True, (17, 180, 179))
    screen.blit(player_name_text, (164, 102))
    game_over_text = game_over_font.render('Game Over', True, (152, 79, 254))
    screen.blit(game_over_text, (178, 178))
    final_time_text = final_time_font.render(final_time, True, (232, 20, 21))
    screen.blit(final_time_text, (308, 340))
    mixer.music.stop()


FPS = 200  # frames per second setting
fpsClock = pygame.time.Clock()

# Game is running or not
game_run = True

# Main while loop section /*/*/*/

# Game Loop.
running = True
temp_time = 0
temp_color = 0

while running:  # running infinite while loop

    # Display screen (above everything)
    if temp_time > 100:
        temp_time = 0
        temp_color += 5
    if temp_color + 51 <= 250:
        screen.fill((51 + temp_color, 167, 220))  # (R,G,B) values (59, 179, 208) , (0, 183, 229) , (100, 211, 219)
    else:
        screen.fill((255, 167, 220))  # Stop changing of color.

    # Returns mouse position
    mouse = pygame.mouse.get_pos()

    # break for close
    for event in pygame.event.get():  # see all the events happening in game window
        if event.type == pygame.QUIT:  # must write event type to check type of events and it is QUIT /=not quit,() :
            running = False  # break loop

    ticks = pygame.time.get_ticks()
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 24)

    # Game completed
    if (minutes >= 1) or (seconds >= 59):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 330 <= mouse[0] <= 430 and 420 <= mouse[1] <= 470:
                running = False
                # pygame.quit()
        game_run = False
        mixer.music.stop()
        screen.fill((54, 67, 60))
        finish_game()
        quit_game()

    elif game_run:

        # Really water is moving
        moving_water()

        if ob1.is_collision(boat_X, boat_Y):
            game_run = False

        # Moving objects or shark
        objects_move()

        # Shows the time
        timer_fun(game_run)
        # print(timer_fun(game_run))

    else:

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 330 <= mouse[0] <= 430 and 420 <= mouse[1] <= 470:
                running = False
        screen.fill((54, 67, 60))
        quit_game()
        if final_time == 'None':
            final_time = str(timer_fun(game_run))
            collision_sound = mixer.Sound('Shotgun_Blast.wav')
            collision_sound.play()
            game_over_sound = mixer.Sound('Icy Game Over.wav')
            game_over_sound.play()
        game_over()
        # print(final_time)

    # Boat
    # Boat moving X
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            boat_X_change = -6.7
        elif event.key == pygame.K_RIGHT:
            boat_X_change = 6.7
    # Boat moving Y
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            boat_Y_change = -6.7
        elif event.key == pygame.K_DOWN:
            boat_Y_change = 6.7

    # update boat
    boat_X += boat_X_change
    boat_Y += boat_Y_change

    # boundaries X
    if boat_X <= 0:
        boat_X = 0
    elif boat_X >= 701:
        boat_X = 701
    # boundaries Y
    if boat_Y <= 300:
        boat_Y = 300
    elif boat_Y >= 532:
        boat_Y = 532

    # key is released
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            boat_X_change = 0
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            boat_Y_change = 0

    # Boat moving function
    boat_move(boat_X)

    # Screen fill method
    temp_time += 1

    pygame.display.update()  # update screen, if something new is added
    fpsClock.tick(FPS)  # Game frame updates as per rate of FPS
