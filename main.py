import pygame
from water import Water
from objects import objects

# Game heading and initializing section

# Initialize Pygame
pygame.init()

# Screen set mode
screen = pygame.display.set_mode((764, 732))  # ( width, height )

# Title And Logo
pygame.display.set_caption("Boat Rush")  # display caption
icon = pygame.image.load('boat_logo.png')
pygame.display.set_icon(icon)

# Boat section

# Boat
boat_img = pygame.image.load('cargo_ship_1.png')
boat_X = 355
boat_Y = 505
boat_X_change = 0
boat_Y_change = 0


def boat_move(boat_X):
    screen.blit(boat_img, (boat_X, boat_Y))


# defining water class
w1 = Water()


# Movement of water..
def moving_water():
    for i in range(w1.wave_len):
        for j in range(w1.wave_wid):
            screen.blit(w1.W_wave_img[i][j], (w1.W_wave_X[i][j], w1.W_wave_Y[i][j]))
            w1.wave_move()
    # pygame.display.update()


# Object Section

# Objects making
ob1 = objects()


# object moving function
def objects_move():
    for j in range(ob1.object_s):
        screen.blit(ob1.object_img[j], (ob1.object_X[0][j], ob1.object_Y[0][j]))
        ob1.object_movement()
        # print(ob1.object_Y)


FPS = 60  # frames per second setting
fpsClock = pygame.time.Clock()

# Game Loop.
running = True
while running:  # running infinite while loop

    # Display screen (above everything)
    screen.fill((100, 211, 219))  # (R,G,B) values (59, 179, 208) , (0, 183, 229)

    # break for close
    for event in pygame.event.get():  # see all the events happening in game window
        if event.type == pygame.QUIT:  # must write event type to check type of events and it is QUIT /=not quit,() :
            running = False  # break loop

    # Really water is moving
    moving_water()

    # Boat
    # Boat moving X
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            boat_X_change = -6.4
        elif event.key == pygame.K_RIGHT:
            boat_X_change = 6.4
    # Boat moving Y
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            boat_Y_change = -6.4
        elif event.key == pygame.K_DOWN:
            boat_Y_change = 6.4

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

    # ob1.object_movement()
    objects_move()

    boat_move(boat_X)

    pygame.display.update()  # update screen, if something new is added
    fpsClock.tick(FPS)  # Game frame updates as per rate of FPS
