# Last Bastion TD
# Sougato Chakrobortty
# 12/05/2026
# IDE LSP may signal errors that do not account for functions handling them.

import pygame as p # import and shorten the pygame library
import sys as s # import and shorten the system library

p.init() # initialize pygame

# global variables
SIZE = (1000, 700) # screen size (taken from assignment)
FPS = 60 # frame rate
FONT = "JetBrainsMono Nerd Font" # choosing the system font
BLUE, RED, GREEN, YELLOW, WHITE, ORANGE, BLACK = (0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 255, 255), (255, 165, 0), (0, 0, 0) # all colours

# function variables
screen = p.display.set_mode(SIZE) # setting mode to size variable
clock = p.time.Clock() # enforce frame rate
levelstate = 0 # menu by default

p.display.set_caption("Last Bastion TD") # window title

# asset loading, we want it done before a loop so we don't have it reloading so often
assets = { # make a dictionary
    # fonts
    "large": p.font.SysFont(FONT, 32), # large font
    "small": p.font.SysFont(FONT, 24), # small font

    # menu specific images
    "menubg": p.transform.scale(p.image.load("./assets/menu/menubg.jpg").convert(), (SIZE[0], SIZE[1])), # menu background
    "buymenubg": p.transform.scale(p.image.load("./assets/menu/buymenubg.png").convert(), (SIZE[0], SIZE[1])), # buy menu background
    "menubanner": p.image.load("./assets/menu/banner.png").convert_alpha(), # menu banner

    # towers
    "TWR1": p.image.load("./assets/towers/t1/t1l1.png").convert_alpha(),
    "TWR2": p.image.load("./assets/towers/t1/t1l2.png").convert_alpha(),
    "TWR3": p.image.load("./assets/towers/t1/t1l3.png").convert_alpha(),
}

maps = { # maps dict
    1: { # level 1
        "bgimg": p.image.load("./assets/bg/bg1.png").convert_alpha(), # the background of the level
        "startmoney": 100, # the money the player starts with
        "enemystart": (200, 0), # starting positon for the enemies
        "towerstart": (800, 700), # start position for the tower
        "corners": [(200, 145), (805, 145), (805, 350), (195, 350), (195, 555), (805, 555), (805, 800)], # the corners the enemies move toward
        "plots": [ # rectangles where the user can press to place towers
            # top row
            p.Rect(265, 15, 130, 60),
            p.Rect(410, 15, 130, 60),
            p.Rect(555, 15, 130, 60),
            p.Rect(700, 15, 130, 60),

            # second row
            p.Rect(160, 220, 130, 60),
            p.Rect(305, 220, 130, 60),
            p.Rect(450, 220, 130, 60),
            p.Rect(600, 220, 130, 60),

            # third row
            p.Rect(275, 425, 130, 60),
            p.Rect(420, 425, 130, 60),
            p.Rect(565, 425, 130, 60),
            p.Rect(710, 425, 130, 60),

            # last row
            p.Rect(160, 625, 130, 60),
            p.Rect(310, 625, 130, 60),
            p.Rect(450, 625, 130, 60),
            p.Rect(600, 625, 130, 60),
        ]
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

def levelreset(): # function to reset the global variables if the user replays
    global levelsetup, enemies, levelhp, buying, towerheld, towers, money, affordable

    levelsetup = False # one timers
    enemies = [] # object list to store which enemies are alive
    levelhp = 100 # start the level's HP
    buying = True # start the user buying
    towers = [] # the towers placed
    towerheld = None # which tower is the user placing? None means they're not holding tower 1 or 2
    money = maps[levelstate]["startmoney"] # put the current level's starting amount into the balance
    affordable = True # prevent the error message first

# buttons
def menubutton(text, yplus, yscale): # make a function to modularize the process
    if len(text) < 5: # the box won't fit if the string is longer than 4 characters
        buttonobj = p.Rect((SIZE[0] // 2) - 30, yscale + yplus, 100, 50) # using the rectangle object

        p.draw.rect(screen, WHITE, buttonobj, 2) # place a border around it

    else:
        buttonobj = p.Rect((SIZE[0] // 2) - 30, yscale + yplus, 120, 50) # using the rectangle object

        p.draw.rect(screen, WHITE, buttonobj, 2) # place a border around it

    pyprint(text, (SIZE[0] // 2) - 20, yscale + yplus, "large") # draw the button    

    return buttonobj # give the object back to check for clicks

def menu(): # menu function
    scaly = 100 # base y

    # background & title banner
    screen.blit(assets["menubg"], (0, 0)) # load the jpg background 
    screen.blit(assets["menubanner"], ((SIZE[0] // 2) - 290, scaly - 75)) # load the png banner

    # title
    pyprint("Last Bastion", (SIZE[0] // 2) - 100, scaly + 100, "large", BLACK) # bigger text
    pyprint("Tower Defense", (SIZE[0] // 2) - 80, scaly + 150, "small", BLACK) # smaller text

    playbutton = menubutton("Play", 250, scaly) # play button
    infobutton = menubutton("Info", 310, scaly) # info button
    quitbutton = menubutton("Quit", 370, scaly) # quit button

    return playbutton, infobutton, quitbutton # have them be returned to be accessed by the event loop

def buymenu(): # buy menu function
    scaly = 100 # base y

    # background & title banner
    screen.blit(assets["buymenubg"], (0, 0)) # load the png background 
    screen.blit(assets["menubanner"], ((SIZE[0] // 2) - 290, scaly - 75)) # load the png banner

    # title
    pyprint("Buy Menu", (SIZE[0] // 2) - 50, scaly + 100, "large", BLACK) # bigger text
    pyprint(f"Level {levelstate}", (SIZE[0] // 2) - 30, scaly + 150, "small", BLACK) # smaller text
    pyprint("Press space to start level. | Press S to sell tower.\nPrices are not charged until tower is placed.", 15, 20, "small", WHITE) # useful info for the user 
    pyprint(f"${str(money)}", (SIZE[0] / 2), 440 + scaly, "small", YELLOW) # current balance

    if not affordable: # an error message from the last failed purchase
        pyprint("Insufficient funds for the purchase!", (SIZE[0] / 2) - 225, 650, "small", RED) # 2 line breaks to be placed below the above text

    # the 3 levels of towers
    tower1button = menubutton("TWR 1", 250, scaly) # first tower
    pyprint("$10", 600, 255 + scaly, "small", GREEN) # price 1
    tower2button = menubutton("TWR 2", 310, scaly) # second tower
    pyprint("$20", 600, 315 + scaly, "small", GREEN) # price 2
    tower3button = menubutton("TWR 3", 370, scaly) # third tower
    pyprint("$30", 600, 375 + scaly, "small", GREEN) # price 3

    return tower1button, tower2button, tower3button # have them be returned to be accessed by the event loop


def level(map): # function for the actual level to be played
    global levelsetup, levelhp, buying # allow the variable changes to leave the function

    currentlevel = maps[map] # place the info for only this level into a variable

    # grabbing info from the variable above
    corners = currentlevel["corners"] # the corners the enemy will go toward

    screen.blit(maps[map]["bgimg"], (0, 0)) # load the png background 

    for i in towers:
        towerimg = assets[f"TWR{i['type']}"] # Looking for "TWR1," "TWR2," etc.
        towerrect = towerimg.get_rect(center = i["rect"].center) # finding the rectangle object and grabbing its centre

        screen.blit(towerimg, towerrect) # image, coordinates

    pyprint(f"HP: {str(levelhp)}", 15, 20, "small", WHITE) # convert the hp integer into a displayable string
    pyprint(f"${str(money)}", 15, 50, "small", YELLOW) # convert the money integer into a displayable string

    # DEBUG -----
    #for i in pyevents: 
    #    if i.type == p.MOUSEBUTTONDOWN and i.button == 1: 
    #        pos = i.pos 
    #
    #        print(pos)
    # ----- DEBUG

    if buying: # check if the user is in the buy phase
        global towerheld # allow use everywhere

        if towerheld is None: # check if a tower is not at hand
            buymenu() # show the menu for the user to pick

        elif towerheld == -1: # if the user is selling
            pyprint(f"Selling tower", 400, 315, "small", RED) # selling info
            pyprint(f"Press escape to cancel.", 360, 355, "small", RED) # instructions

        else: # otherwise the user is working with a tower
            pyprint(f"Placing Tower {towerheld}", 400, 315, "small", RED) # display the tower held
            pyprint(f"Press escape to cancel.", 360, 355, "small", RED) # instructions

            # making the cursor have a tower be following it, so the user can visually see the tower coming
            xpos, ypos = p.mouse.get_pos() # get the mouse position into 2 variables
            followimg = assets[f"TWR{towerheld}"] # grab the image itself
            followrect = followimg.get_rect(center = (xpos, ypos)) # make the object with its centre being the mouse position

            screen.blit(followimg, followrect) # image, position

        key = p.key.get_pressed() # keypresses

        if key[p.K_SPACE]: # if the user presses space
            buying = False # leave the buy menu

        if key[p.K_ESCAPE]: # if the user presses escape
            towerheld = None # go back to the buy menu

    else: # otherwise play the game
        if not levelsetup: # if everything isn't set already
            enemies.append(enemy(100, 5, map, 25)) # make an enemy and add it to the list
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
        global money # need access to globally change money to give refunds
        level(levelstate) # start the level

        for i in pyevents: # open a new event loop
            if i.type == p.KEYDOWN and i.key == p.K_s: # check if the user is pressing the sell key (S)
                towerheld = -1 # set the tower being held to a special position to sell

            if i.type == p.MOUSEBUTTONDOWN and i.button == 1: # check if left mouse clicked
                pos = i.pos # get mouse position

                if buying: # in the buy menu
                    if towerheld is None: # if isn't already placing a tower
                        global price # allow global price usage

                        scaly = 100 # bring back this variable from before

                        # redefine the hitboxes generated by the button function
                        tower1rect = p.Rect((SIZE[0] // 2) - 30, scaly + 250, 120, 50)
                        tower2rect = p.Rect((SIZE[0] // 2) - 30, scaly + 310, 120, 50)
                        tower3rect = p.Rect((SIZE[0] // 2) - 30, scaly + 370, 120, 50)

                        # check the buttons, then assign it to my state variable
                        if tower1rect.collidepoint(pos):
                            towerheld = 1 

                        elif tower2rect.collidepoint(pos):
                            towerheld = 2

                        elif tower3rect.collidepoint(pos):
                            towerheld = 3

                    elif towerheld == -1: # check if the user just wants to sell something
                        levelplots = maps[levelstate]["plots"] # grab plots for the current level
                        sold = False # create a value to leave the loop later when the plot is sold

                        for j in levelplots: # loop through plots
                            if j.collidepoint(pos): # check if it was clicked on
                                for k in towers: # loop through active towers
                                    if k["rect"] == j: # check if there's a rectangle object there
                                        money += ((k["type"] * 10) // 4) * 3 # refund 75%
                                        towers.remove(k) # remove the tower
                                        sold = True # will allow the other loop to be left
                                        break # leave the loop

                            if sold:
                                towerheld = None # leave this state
                                break # break the loop

                    else: # otherwise, the user is buying and holding
                        levelplots = maps[levelstate]["plots"] # grab plots for the current level

                        for j in levelplots: # loop through plots
                            if j.collidepoint(pos): # if any of the plots are clicked on
                                taken = any(k["rect"] == j for k in towers) # if anything is present in the current plot, put it into this variable

                                if not taken: # check if the above variable is not what we're clicking on
                                    price = towerheld * 10 # dynamically make the price of the tower being placed
                                    affordable = money >= price # set a boolean so i can use it later

                                    if affordable: # check if the user can afford the tower
                                        towers.append({ # add a dictionary
                                            "type": towerheld, # type
                                            "rect": j # the rectangle object
                                        }) 

                                        money -= price # subtract the price

                                    towerheld = None # leave this state
                                    break # leave the loop

    pyprint("Sougato", 15, 650, "small") # my name :)

    p.display.flip() # update
    clock.tick(FPS) # framerate
