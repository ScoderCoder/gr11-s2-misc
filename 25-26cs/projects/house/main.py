#!python

# Sougato Chakrobortty
# ---------------------
# Haunted House Project
# 03/03/2026
# ---------------------

import pygame # import main library
import sys # system library for mouse events
import random # random number generator

pygame.init() # initialize pygame

SIZE = (1000, 700) # screen size (taken from assignment)
screen = pygame.display.set_mode(SIZE) # setting mode to size variable
FPS = 60 # frame speed

# defining colours
GREY = (30, 33, 40) 
BLACK = (10, 10, 6)
BLUE = (55, 56, 73)
YELLOW = (234, 162, 65)
BGLIGHT = (120, 144, 152)
BGDARK = (62, 76, 87)
MOONLIGHT = (245, 227, 199)
MOONDARK = (228, 211, 180)

screen.fill(BGLIGHT) # background

# function to draw cloud, as we will draw multiple in different places
def drawCloud(x, y): # take x & y as parameters
    # draw circles to overlap & look like a cloud
    # using operatos to make other circles position themselves relatively

    # top layer
    pygame.draw.circle(screen, BGDARK, (x, y), 20)
    pygame.draw.circle(screen, BGDARK, (x + 25, y - 10), 20)
    pygame.draw.circle(screen, BGDARK, (x + 50, y - 15), 20)
    pygame.draw.circle(screen, BGDARK, (x + 75, y - 10), 20)
    pygame.draw.circle(screen, BGDARK, (x + 100, y), 20)

    # bottom layer
    pygame.draw.circle(screen, BGDARK, (x + 25, y + 10), 20)
    pygame.draw.circle(screen, BGDARK, (x + 50, y + 15), 20)
    pygame.draw.circle(screen, BGDARK, (x + 75, y + 10), 20)
    pygame.draw.circle(screen, BGDARK, (x + 100, y), 20)

# function to draw roof, as we will draw multiple in different places
def drawRoof(x, y): # same parameters
    pygame.draw.polygon(screen, GREY, ((x, y), (x + 80, y - 160), (x + 160, y))) # main window (triangle)
    pygame.draw.polygon(screen, BLACK, ((x, y), (x + 80, y - 160), (x + 160, y)), 7) # window outline

# function to draw window, as we will draw multiple in different places
def drawWindow(x, y):
    pygame.draw.polygon(screen, YELLOW, ((x, y), (x - 10, y + 70), (x + 30, y + 70), (x + 20, y))) # yellow base
    pygame.draw.polygon(screen, BLACK, ((x, y), (x - 10, y + 70), (x + 30, y + 70), (x + 20, y)), 7) # outline
    pygame.draw.line(screen, BLACK, (x + 10, y), (x + 10, y + 70), 7) # line down the middle
    pygame.draw.line(screen, BLACK, (x - 5, y + 35), (x + 25, y + 35), 7) # line across the middle

# function to draw house, function is easy to reproduce
def drawHouse(): # no parameters, we will run this once
    # base
    pygame.draw.rect(screen, BLUE, (350, 400, 350, 700)) # base of house
    pygame.draw.rect(screen, BLACK, (350, 400, 350, 700), 7) # base outline
    pygame.draw.rect(screen, BLACK, (400, 400, 300, 700), 7) # line through the base
    drawWindow(440, 475) # base window

    # door
    pygame.draw.rect(screen, GREY, (515, 500, 75, 150)) # door base
    pygame.draw.rect(screen, BLACK, (515, 500, 75, 150), 7) # door outline
    pygame.draw.circle(screen, BLACK, (530, 555), 5) # door handle

    # moon 
    pygame.draw.circle(screen, MOONLIGHT, (860, 100), 85) # moon base
    pygame.draw.circle(screen, BLACK, (860, 100), 85, 7) # moon outline

    for i in range (1, 7):
        pygame.draw.circle(screen, MOONDARK, (random.randint(820, 900), random.randint(60, 140)), random.randint(5, 15)) # moon dots

    # middle
    pygame.draw.rect(screen, BLUE, (460, 200, 100, 200)) # middle tower
    pygame.draw.rect(screen, BLACK, (460, 200, 100, 200), 7) # middle tower outline
    drawRoof(430, 210) # middle roof
    drawWindow(500, 220) # middle window

    # left
    pygame.draw.rect(screen, BLUE, (350, 335, 100, 100)) # left tower
    pygame.draw.line(screen, BLACK, (353, 335), (353, 435), 7) # left tower outline 
    drawRoof(320, 340) # left roof
    drawWindow(380, 360) # left window

    pygame.draw.polygon(screen, GREY, ((380, 450), (420, 300), (680, 300), (720, 450))) # big roof, will only be drawn once so no function
    pygame.draw.polygon(screen, BLACK, ((380, 450), (420, 300), (680, 300), (720, 450)), 7) # roof outline

    # right side
    pygame.draw.rect(screen, BLUE, (600, 400, 100, 100)) # right tower
    pygame.draw.line(screen, BLACK, (600, 400), (600, 500), 7) # right tower outline
    pygame.draw.line(screen, BLACK, (696, 400), (696, 500), 7) # right tower outline 2
    pygame.draw.rect(screen, BGLIGHT, (700, 400, 100, 100)) # covering up overflowing big roof
    drawRoof(570, 400) # right roof
    drawWindow(640, 420) # right window
    drawWindow(640, 510) # right window 2

# drawing ghosts
def drawGhost(x, y): # pass in cords again
    pygame.draw.rect(screen, MOONLIGHT, (x, y, 65, 55)) # base
    pygame.draw.circle(screen, MOONLIGHT, (x + 32.5, y), 32.5) # circle overlap
    pygame.draw.circle(screen, BLACK, (x + 21.67, y + 10), 5) # left eye
    pygame.draw.circle(screen, BLACK, (x + 43.33, y + 10), 5) # right eye
    pygame.draw.circle(screen, MOONLIGHT, (x + 10, y + 55), 10) # left groove
    pygame.draw.circle(screen, MOONLIGHT, (x + 32.5, y + 55), 10) # middle groove
    pygame.draw.circle(screen, MOONLIGHT, (x + 55, y + 55), 10) # right groove

# drawing clouds, passing in random functions to place the clouds at random coordinates each time
drawCloud(random.randint(50, 200), random.randint(50, 500)) # left cloud
drawCloud(random.randint(250, 650), random.randint(50, 60)) # middle cloud

# ghosts, same logic
drawGhost(random.randint(50, 200), random.randint(50, 500)) # left ghost
drawGhost(random.randint(250, 650), random.randint(50, 60)) # middle ghost

drawHouse() # will only be called once, no parameters

# placing this here to draw over covering inside drawHouse()
drawCloud(random.randint(750, 850), random.randint(200, 630)) # right cloud
drawGhost(random.randint(750, 850), random.randint(200, 630)) # right ghost

# base - short & ran one time, so no function
pygame.draw.ellipse(screen, GREY, (100, 600, 800, 200)) # oval shape for base
pygame.draw.ellipse(screen, BLACK, (100, 600, 800, 200), 10) # outline for oval
pygame.draw.rect(screen, BGLIGHT, (100, 665, 800, 265)) # covering the bottom half for semi-circle

# branches - these are 2 different types of trees only drawn once each, no function needed

# right branch
pygame.draw.line(screen, BLACK, (790, 635), (800, 500), 10) # stalk
pygame.draw.line(screen, BLACK, (840, 515), (800, 540), 10) # top right branch
pygame.draw.line(screen, BLACK, (760, 515), (800, 540), 10) # top left branch
pygame.draw.line(screen, BLACK, (840, 555), (800, 580), 10) # bottom right branch
pygame.draw.line(screen, BLACK, (755, 555), (800, 580), 10) # bottom left branch
pygame.draw.line(screen, BLACK, (820, 568), (840, 583), 10) # bottom left branch branch
pygame.draw.line(screen, BLACK, (775, 568), (755, 583), 10) # bottom right branch branch

# left branch
pygame.draw.line(screen, BLACK, (230, 635), (240, 450), 10) # stalk
pygame.draw.line(screen, BLACK, (238, 520), (190, 465), 10) # top right branch
pygame.draw.line(screen, BLACK, (238, 520), (276, 465), 10) # top left branch
pygame.draw.line(screen, BLACK, (238, 580), (190, 555), 10) # bottom right branch
pygame.draw.line(screen, BLACK, (238, 580), (276, 555), 10) # bottom left branch
pygame.draw.line(screen, BLACK, (210, 568), (190, 583), 10) # bottom left branch branch
pygame.draw.line(screen, BLACK, (255, 568), (275, 583), 10) # bottom right branch branch

# define pygame clock
clock = pygame.time.Clock()

# forever loop
while True:
    # sync clock with FPS
   clock.tick(FPS)

    # checking pygame events
   for event in pygame.event.get():
       if event.type == pygame.MOUSEBUTTONDOWN: # if mouse clicked
           mx,my = pygame.mouse.get_pos() # grab position
           print(mx,my) # print

       if event.type == pygame.QUIT: # check for quit
           pygame.quit() # exit pygame
           sys.exit() # exit program

   pygame.display.flip()
