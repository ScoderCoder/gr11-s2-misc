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
FONT = "./assets/jbm.ttf" # choosing the font file
BLUE, RED, GREEN, YELLOW, WHITE, ORANGE, BLACK = (0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 255, 255), (255, 165, 0), (0, 0, 0) # all colours

# function variables
screen = p.display.set_mode(SIZE) # setting mode to size variable
clock = p.time.Clock() # enforce frame rate
levelstate = 0 # menu by default
diedb4 = False # used by the menu, which does not take the level resetting into acconut
gamebeaten = False # same as above

p.display.set_caption("Last Bastion TD") # window title

# asset loading, we want it done before a loop so we don't have it reloading so often
assets = { # make a dictionary
    # fonts
    "large": p.font.Font(FONT, 32), # large font
    "small": p.font.Font(FONT, 24), # small font

    # menu specific images
    "menubg": p.transform.scale(p.image.load("./assets/menu/menubg.jpg").convert(), (SIZE[0], SIZE[1])), # menu background
    "buymenubg": p.transform.scale(p.image.load("./assets/menu/buymenubg.png").convert(), (SIZE[0], SIZE[1])), # buy menu background
    "menubanner": p.image.load("./assets/menu/banner.png").convert_alpha(), # menu banner

    # towers
    "TWR1": p.image.load("./assets/towers/t1/t1l1.png").convert_alpha(),
    "TWR2": p.image.load("./assets/towers/t1/t1l2.png").convert_alpha(),
    "TWR3": p.image.load("./assets/towers/t1/t1l3.png").convert_alpha(),
}

# our towers are png images, and we rely on transparency so we need to make sure the invisible pixels don't count
assets["TWR1mask"] = p.mask.from_surface(assets["TWR1"])
assets["TWR2mask"] = p.mask.from_surface(assets["TWR2"])
assets["TWR3mask"] = p.mask.from_surface(assets["TWR3"])

maps = { # maps dict
    1: { # level 1
        "bgimg": p.image.load("./assets/bg/bg1.png").convert_alpha(), # the background of the level
        "startmoney": 100, # the money the player starts with
        "enemystart": (200, 0), # starting position for the enemies
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
    def __init__(self, hp, speed, level, damage, colour = RED): # function to run at the start of the class
        self.xpos = maps[level]["enemystart"][0] # grabbing the info
        self.ypos = maps[level]["enemystart"][1] # second position is y
        self.exists = True # alive or not?
        self.hp = hp # given when the enemy is created
        self.speed = speed # given speed
        self.cornerindex = 0 # index for the enemy's position in the list of corners
        self.damage = damage # given damage
        self.size = 60 # the size to be drawn at
        self.colour = colour # use the default red or the specified

        enemysurface = p.Surface((self.size, self.size)) # make it an object
        enemysurface.fill(WHITE) # allow the surface to be hit
        self.mask = p.mask.from_surface(enemysurface) # put the mask into its own variable

    def getrect(self): # function to return a rectangle object to check collision
        return p.Rect(self.xpos - (self.size / 2), self.ypos - (self.size / 2), self.size, self.size) # dynamically pass coordinates

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
        self.orangetimer = 1 # orange for 1 frames

        if self.hp <= 0: # check if there's no HP, also checking for less than 0 in the case of a negative
            self.exists = False # the enemy no longer exists

            global money # access the global money variable

            money += self.speed # make the user some money if they managed to eliminate the enemy

def pyprint(text, x, y, size, colour = WHITE): # function to print quicker, with parameters
    screen.blit(assets[size].render(text, True, colour), (x, y)) # fixed colour, background is black to overwrite old text

def levelreset(): # function to reset the global variables if the user replays
    global levelsetup, enemies, levelhp, buying, towerheld, towers, money, affordable, diedb4, spawntimer, enemiesalive, wavestate, enemyconfigs, waveenemies, gamebeaten # allow global reset

    levelsetup = False # one timers
    enemies = [] # object list to store which enemies are alive
    levelhp = 100 # start the level's HP
    buying = True # start the user buying
    towers = [] # the towers placed
    towerheld = None # which tower is the user placing? None means they're not holding tower 1 or 2
    money = maps[levelstate]["startmoney"] # put the current level's starting amount into the balance
    affordable = True # prevent the error message first
    diedb4 = False # prevent another error message
    spawntimer = 0 # timer based spawning system for enemies
    enemiesalive = 10 # total enemies that will spawn
    wavestate = 1 # start at the first wave
    enemyconfigs = [] # list of dictionaries to remember what types of enemies are alive
    waveenemies = 0 # tracker for the amount of enemies in the current wave
    gamebeaten = False # if the user is playing, the game wasn't beaten

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

    if diedb4: # an error message from the last failed purchase
        pyprint("You died! Pick an option to continue.", (SIZE[0] / 2) - 235, 650, "small", RED) # bottom middle of the screen 
    elif gamebeaten: # winner's message
        pyprint("You won! Pick an option to continue.", (SIZE[0] / 2) - 235, 650, "small", GREEN) # green success

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
    pyprint(f"Level {levelstate} | Wave {wavestate}", (SIZE[0] // 2) - 100, scaly + 150, "small", BLACK) # smaller text
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
    global levelsetup, levelhp, buying, spawntimer, enemiesalive, wavestate, enemyconfigs, waveenemies, buying, levelstate, enemies, levelstate, gamebeaten, affordable # global variables that will be changed

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
        if not levelsetup: # one time run
            enemyconfigs = [] # empty the configurations

            if wavestate >= 1: # for the first wave, wave 2 and 3 will also use these enemies
                for i in range(10): # 10 base enemies
                    enemyconfigs.append({
                        "hp": 100,
                        "speed": 5, 
                        "damage": 10,
                        "colour": RED
                    })

            if wavestate >= 2: # for the second wave, wave 3 will also use these enemies
                for i in range(5): # 5 extra enemies
                    enemyconfigs.append({
                        "hp": 150,
                        "speed": 10, 
                        "damage": 15,
                        "colour": BLUE
                        })

            if wavestate == 3: # for the last wave, no other waves exist after so this can be hard capped
                for i in range(5): # last 5 enemies
                    enemyconfigs.append({
                        "hp": 200,
                        "speed": 15, 
                        "damage": 20,
                        "colour": BLACK
                    })

            waveenemies = len(enemyconfigs) # grab the amount of enemies to spawn
            levelsetup = True # leave this state
            spawntimer = 0 # allow the first enemy to be spawned

        if len(enemyconfigs) > 0: # if there's any enemies to spawn
            if spawntimer <= 0: # if the spawn timer runs out
                spawnenemy = enemyconfigs.pop(0) # grab the latest enemy's config to spawn
                enemies.append(enemy(spawnenemy["hp"], spawnenemy["speed"], map, spawnenemy["damage"], spawnenemy["colour"]))
                spawntimer = 45 # reset the spawn timer
            else:
                spawntimer -= 1 # otherwise keep counting

        enemiesarealive = any(i.exists for i in enemies) # check if anyone is alive

        if len(enemyconfigs) == 0 and not enemiesarealive: # if there's no more enemies to spawn and no enemies exist
            if wavestate < 3: # if the user isn't at the final wave
                wavestate += 1 # move up a wave
                towerheld = None # leave any buying state the user was in
                affordable = True # remove any error message
                buying = True # next buying phase
                levelsetup = False # require the level to be setup again
                enemies = [] # clear all the dead enemies
            else:
                if (levelstate + 1) in maps: # if the next level exists
                    levelstate += 1 # move to it
                    levelreset() # reset variables
                else:
                    gamebeaten = True # for the winning text on the next menu
                    levelstate = 0 # back to menu

        for i in enemies: # going through every enemy alive
            if i.exists: # check if the enemy object exists
                if i.cornerindex > len(maps[map]["corners"]) - 1: # check if the corner index is done
                    i.exists = False # the enemy doesn't exist anymore

                    levelhp -= i.damage # apply damage

                    if levelhp <= 0: # if the user dies
                        global diedb4 # globally modify the diedb4 variable

                        diedb4 = True # the user has died, so the error message will print when the user returns to the menu
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

                enemyrect = i.getrect() # grabbing the object
                workingondying = False # variable to check if the enemy is being hit by a tower

                for j in towers: # loop through towers
                    towermask = assets[f"TWR{j['type']}mask"] # dynamically grab the tower mask from the dictionary
                    towerimage = assets[f"TWR{j['type']}"] # dynamically grab the tower image from the dictionary
                    towerrect = towerimage.get_rect(center=j["rect"].center) # grab the tower image as a rectangle

                    # calculating the distance between the x and y points of the enemy and the tower
                    xoffset = enemyrect.x - towerrect.x
                    yoffset = enemyrect.y - towerrect.y

                    if towermask.overlap(i.mask, (xoffset, yoffset)): # check for the contact
                        i.die(0.75) # 0.75 hp gone per contact
                        workingondying = True # state that the user is being hit

                if workingondying: # if the user is taking damage
                    enemycolour = ORANGE # make the colour orange to indicate damage being taken
                else:
                    enemycolour = i.colour # take the default colour

                p.draw.rect(screen, enemycolour, ((i.xpos) - (i.size / 2), (i.ypos) - (i.size / 2), i.size, i.size), border_radius = 5) # draw the enemy

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
                    # levelstate -= 1 # go to a special -1 state for the information screen

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
                                affordable = True # just to remove the error, even if they still can't afford it
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
