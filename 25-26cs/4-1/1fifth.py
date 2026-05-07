import pygame
import sys

pygame.init() # initialize pygame

SIZE = (1000, 700) # screen size (taken from assignment)
screen = pygame.display.set_mode(SIZE) # setting mode to size variable

BLUE = (55, 56, 73) # colour
BLACK = (0, 0, 0)

# loop now
for i in range(1, 1000, 50):
    pygame.draw.circle(screen, BLUE, (i, 50), 25)
    pygame.time.wait(100)
    pygame.display.flip()
    screen.fill(BLACK)
