# Last Bastion TD
# Sougato Chakrobortty
# 12/05/2026

import pygame as p # import and shorten the pygame library
import sys as s # import and shorten the system library

p.init() # initialize pygame

SIZE = (1000, 700) # screen size (taken from assignment)
screen = p.display.set_mode(SIZE) # setting mode to size variable
FPS = 60 # frame rate
clock = p.time.Clock() # enforce frame rate
p.display.set_caption("Last Bastion TD") # window title
levelstate = 0 # menu by default

BLUE, RED, GREEN, YELLOW, WHITE, ORANGE, BLACK = (0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 255, 255), (255, 165, 0), (0, 0, 0) # all colours

# asset loading, we want it done before a loop so we don't have it reloading so often
assets = { # make a dictionary
    # fonts, relies on the Nerd Fonts version of JetBrains Mono
    "large": p.font.SysFont("JetBrainsMono Nerd Font", 32), # large font
    "small": p.font.SysFont("JetBrainsMono Nerd Font", 24), # small font

    # menu specific images
    "menubg": p.transform.scale(p.image.load("./assets/menu/menubg.jpg").convert(), (SIZE[0], SIZE[1])), # menu background
    "menubanner": p.image.load("./assets/menu/banner.png").convert_alpha(), # menu banner
}

maps = { # maps dict
    1: { # level 1
        "bgimg": p.image.load("./assets/bg/bg1.png").convert_alpha(), # the background of the level
        "startmoney": 100, # the money the player starts with
        "enemystart": (200, 0), # starting positon for the enemies
        "towerstart": (800, 700), # start position for the tower
        "corners": [(200, 145), (805, 145), (805, 350), (195, 350), (195, 555), (805, 555), (805, 800)] # the corners the enemies move toward
    },
}

class enemy: # make a class for enemies
    def __init__(self, hp, speed, level, damage): # function to run at the start of the class
        self.xpos = maps[level]["enemystart"][0] # grabbing the info
        self.ypos = maps[level]["enemystart"][1] # second position is y
        self.exists = True # alive or not?
        self.hp = hp # given when the enemy is created
        self.speed = speed # given speed
        self.cornerindex = 0 # index for the enemy's position in the list of corners
        self.orangetimer = 0 # track the amount of frames the enemy should be orange for
        self.damage = damage # given damage

    def right(self, left = False): # function to move left/right
        if left: # if the user wants to go left
            self.xpos -= self.speed # move left at that speed
        else: # otherwise the user is going right
            self.xpos += self.speed # move right at that speed

    def down(self, up = False): # function to move down/up
        if up: # if the user wants to go up
            self.ypos -= self.speed # move up at that speed
        else: # otherwise the user is going down
            self.ypos += self.speed # move down at that speed

    def die(self, damage): # function to take damage
        self.hp -= damage # reduce it from the hp
        self.orangetimer = 15 # orange for 15 frames

        if self.hp <= 0: # check if there's no HP, also checking for less than 0 in the case of a negative
            self.exists = False # the enemy no longer exists

def pyprint(text, x, y, size, colour = WHITE): # function to print quicker, with parameters
    screen.blit(assets[size].render(text, True, colour), (x, y)) # fixed colour, background is black to overwrite old text

def menu(): # menu function
    scaly = 100 # base y

    # background & title banner
    screen.blit(assets["menubg"], (0, 0)) # load the jpg background 
    screen.blit(assets["menubanner"], ((SIZE[0] // 2) - 290, scaly - 75)) # load the png banner

    # title
    pyprint("Last Bastion", (SIZE[0] // 2) - 100, scaly + 100, "large", BLACK) # bigger text
    pyprint("Tower Defense", (SIZE[0] // 2) - 80, scaly + 150, "small", BLACK) # smaller text

    # buttons
    def menubutton(text, yplus): # make a function to modularize the process
        buttonobj = p.Rect((SIZE[0] // 2) - 30, scaly + yplus, 100, 50) # using the rectangle object
        
        if len(text) < 5: # the box won't fit if the string is longer than 4 characters
            p.draw.rect(screen, WHITE, buttonobj, 2) # place a border around it
        
        pyprint(text, (SIZE[0] // 2) - 20, scaly + yplus, "large") # draw the button    
        return buttonobj # give the object back to check for clicks

    playbutton = menubutton("Play", 250) # play button
    infobutton = menubutton("Info", 310) # info button
    quitbutton = menubutton("Quit", 370) # quit button

    return playbutton, infobutton, quitbutton # have them be returned to be accessed by the event loop

# some variables before the enemy is created, so it doesn't run 60 times per second

def levelreset(): # function to reset the global variables if the user replays
    global levelsetup, enemies, levelhp

    levelsetup = False # one timers
    enemies = [] # object list to store which enemies are alive
    levelhp = 100 # start the level's HP

def level(map): # function for the actual level to be played
    global levelsetup, levelhp # allow the variable changes to leave the function
    currentlevel = maps[map] # place the info for only this level into a variable
    buying = True # make a variable to check whether the user is in the buy phase

    # grabbing info from the variable above
    money = currentlevel["startmoney"] # money will be copied from the starting amount
    corners = currentlevel["corners"] # the corners the enemy will go toward
    
    screen.blit(maps[map]["bgimg"], (0, 0)) # load the png background 
    pyprint(f"HP: {str(levelhp)}", 15, 20, "small", WHITE) # convert the hp integer into a displayable string

    if buying:
        pass # --------------------------------------------------------------------------- DEBUG, PUT BUY MENU CODE HERE

    if not levelsetup: # if everything isn't set already
        enemies.append(enemy(100, 5, map, 100)) # make an enemy and add it to the list
        levelsetup = True # there's no need to run again
        enemycolour = RED # set the colour of the enemy

    for i in enemies: # going through every enemy alive
        if i.exists: # check if the enemy object exists
            if i.cornerindex > len(maps[map]["corners"]) - 1: # check if the corner index is done
                i.exists = False # the enemy doesn't exist anymore
                levelhp -= i.damage # apply damage
                
                if levelhp <= 0: # if the user dies
                    global levelstate # globally modify the level state variable
                    levelstate = 0 # put the level back to the menu

                continue # no need to keep going in the loop on this enemy

            cornerx, cornery = corners[i.cornerindex] # save time by putting the values into a variable
            
            if i.xpos != cornerx: # check if the x position is not at the corner
                if abs(i.xpos - cornerx) < i.speed: # check if the left over space is less than the speed, since overshooting would otherwise happen
                    i.xpos = cornerx # snap to that position

                elif i.xpos < cornerx: # if less
                    i.right() # move right
                
                elif i.xpos > cornerx: # if more
                    i.right(True) # move left
                
            elif i.ypos != cornery: # check if the y position is not at the corner 
                if abs(i.ypos - cornery) < i.speed: # avoid overshooting again 
                    i.ypos = cornery # snap to that position

                elif i.ypos < cornery: # if less 
                    i.down() # move down
                
                elif i.ypos > cornery: # if more
                    i.down(True) # move up

            else: # otherwise move to the next corner
                i.cornerindex += 1; # move to the next

            enemycolour = RED # red by default

            if i.orangetimer > 0: # the die function will make the orangetimer 15, so this will become true
                enemycolour = ORANGE # if the die function has been called, make the enemy orange
                i.orangetimer -= 1 # count down on the timer, this conditonal statement won't be true in 15 frames

            enemysize = 60 # size of the enemy
            p.draw.rect(screen, enemycolour, ((i.xpos) - (enemysize / 2), (i.ypos) - (enemysize / 2), enemysize, enemysize), border_radius = 5) # draw the enemy

while True: # forever
    pyevents = p.event.get() # easier name for game events

    for i in pyevents: # for every event in my game
        if i.type == p.QUIT: # if the user wants to quit
            p.quit() # leave pygame
            s.exit() # leave the program

    if levelstate == 0: # only if the user is supposed to be here
        playrect, inforect, quitrect = menu() # grab the variables returned above

        for i in pyevents: # open a new event loop
            if i.type == p.MOUSEBUTTONDOWN and i.button == 1: # check if left mouse clicked
                pos = i.pos # get mouse position

                if playrect.collidepoint(pos): # if the play button is pressed
                    levelstate += 1 # add one to the level
                    levelreset() # fresh variables
                elif inforect.collidepoint(pos): # if the info button is pressed
                    print("Info button clicked!") # debug info
                elif quitrect.collidepoint(pos): # if the quit button is pressed
                    p.quit() # quit pygame
                    s.exit() # exit the program

    else: # otherwise (if the user didn't press play the levelstate will remain 0)
        level(levelstate) # start the level

    pyprint("Sougato", 15, 650, "small") # my name :)

    p.display.flip() # update
    clock.tick(FPS) # framerate
