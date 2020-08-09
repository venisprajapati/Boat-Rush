import pygame

# Initialize Pygame
pygame.init()

# Create the screen(display) ( length, width ) -> tuple; so it is required to write inside another bracket
screen = pygame.display.set_mode((764, 564))  # ( width, height )

# Game Loop.
running = True
while running:  # running infinite while loop

    # Display screen (above everything)
    # Anything that is persistent into your window continuously
    screen.fill((59, 179, 208))  # (R,G,B) values

    for event in pygame.event.get():  # see all the events happening in game window
        if event.type == pygame.QUIT:  # must write event type to check type of events and it is QUIT /=not quit,() :
            running = False  # break loop

    pygame.display.update()  # update screen, if something new is added
