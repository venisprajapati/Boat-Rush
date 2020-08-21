import pygame
from water import Water

# Initialize Pygame
pygame.init()

# Screen set mode
screen = pygame.display.set_mode((764, 732))  # ( width, height )

# Title And Logo
pygame.display.set_caption("Boat Rush")  # display caption
icon = pygame.image.load('ferryboat.png')
pygame.display.set_icon(icon)

# Boat
boat_img = pygame.image.load('cargo_ship_1.png')

# defining water class
w1 = Water()


# Movement of water..
def moving_water():
    for i in range(w1.wave_len):
        for j in range(w1.wave_wid):
            screen.blit(w1.W_wave_img[i][j], (w1.W_wave_X[i][j], w1.W_wave_Y[i][j]))
            w1.wave_move()


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
    screen.blit(boat_img, (355, 475))

    pygame.display.update()  # update screen, if something new is added
