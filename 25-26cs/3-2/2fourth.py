import pygame

pygame.init()

SIZE = (500, 500)
screen = pygame.display.set_mode(SIZE)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen.fill(RED)

def drawDesign(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, 100, 100))
    pygame.draw.rect(screen, BLACK, (x + 20, y + 20, 60, 60))
    pygame.draw.circle(screen, BLUE, (x + 50, y + 50), 30)


drawDesign(50, 50)
drawDesign(350, 350)
drawDesign(50, 350)
drawDesign(350, 50)

pygame.display.flip()
pygame.time.wait(5000)
pygame.quit()
