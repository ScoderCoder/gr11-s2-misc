# Pong Recreation
# Sougato Chakrobortty
# 23/04/2026

import pygame as p # import and shorten the pygame library

p.init() # initialize pygame

SIZE = (1000, 700) # Screen size (taken from assignment)
screen = p.display.set_mode(SIZE) # Setting mode to size variable
FPS = 60 # Frame rate
p.display.set_caption("Sougato's Pong") # Window title
FONT = p.font.SysFont('JetBrainsMono Nerd Font', 32) # Pass in my system font

BLACK, WHITE = (0, 0, 0), (255, 255, 255) # frequently used colours

def pyprint(text, x, y, bgcolour = BLACK): # Function to print quicker, with parameters
    screen.blit(FONT.render(text, True, WHITE, bgcolour), (x, y)) # Fixed colour, background is black to overwrite old text

def init(): # function to reset info
    global leftscore, rightscore, paddlecentre, paddleheight # allow everyone to access these variables
    leftscore, rightscore = 0, 0 # default them to 0

    paddleheight = 150 # the height of the paddle

def main():
    pyprint(f"{leftscore}    {rightscore}", 445, 50) # print the score for each side

    for i in range(1, 700, 60): # keeping x cords in mind until the end of the screen
        p.draw.line(screen, WHITE, (500, i), (500, i + 50)) # printing 50px long lines
    
    p.draw.line(screen, WHITE, (30, (SIZE[1] / 2) - (paddleheight / 2)), (30, ((SIZE[1]) / 2) + (paddleheight / 2)), 15) # left paddle
    p.draw.line(screen, WHITE, (SIZE[0] - 30, (SIZE[1] / 2) - (paddleheight / 2)), (SIZE[0] - 30, ((SIZE[1]) / 2) + (paddleheight / 2)), 15) # right paddle

    p.display.flip() # update screen

while True:
    init() # reset
    main() # start the game
