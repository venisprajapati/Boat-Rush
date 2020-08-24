import pygame
from water import Water

# Initialize Pygame
pygame.init()

# Screen set mode
screen = pygame.display.set_mode((764, 732))  # ( width, height )

# Title And Logo
pygame.display.set_caption("Boat Rush")  # display caption
icon = pygame.image.load('boat_logo.png')
pygame.display.set_icon(icon)

# Boat
boat_img = pygame.image.load('cargo_ship_1.png')
boat_X = 355
boat_X_change = 0


def boat_move(boat_X):
    screen.blit(boat_img, (boat_X, 505))


# defining water class
w1 = Water()


# Movement of water..
def moving_water():
    for i in range(w1.wave_len):
        for j in range(w1.wave_wid):
            screen.blit(w1.W_wave_img[i][j], (w1.W_wave_X[i][j], w1.W_wave_Y[i][j]))
            w1.wave_move()
    # pygame.display.update()


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
    # Boat moving
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            boat_X_change = -5.5
        elif event.key == pygame.K_RIGHT:
            boat_X_change = 5.5

    # update boat
    boat_X += boat_X_change

    # boundaries
    if boat_X <= 0:
        boat_X = 0
    elif boat_X >= 701:
        boat_X = 701

    # key is released
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            boat_X_change = 0

    boat_move(boat_X)

    pygame.display.update()  # update screen, if something new is added
    fpsClock.tick(FPS)  # Game frame updates as per rate of FPS
