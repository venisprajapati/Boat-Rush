import pygame


# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((764, 664))  # ( width, height )

# Title And Logo
pygame.display.set_caption("Boat Rush")  # display caption
icon = pygame.image.load('ferryboat.png')
pygame.display.set_icon(icon)

# waves
wave0 = pygame.image.load('wave0.png')
wave1 = pygame.image.load('wave1.png')


# Game Loop.
running = True
while running:  # running infinite while loop

    # Display screen (above everything)
    # Anything that is persistent into your window continuously
    screen.fill((100, 211, 219))  # (R,G,B) values (59, 179, 208) (0, 183, 229)

    for event in pygame.event.get():  # see all the events happening in game window
        if event.type == pygame.QUIT:  # must write event type to check type of events and it is QUIT /=not quit,() :
            running = False  # break loop
            
    screen.blit(wave0, (50, 50))
    screen.blit(wave1, (150, 150))

    pygame.display.update()  # update screen, if something new is added
