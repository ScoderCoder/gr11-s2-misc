# Python Mastermind Recreation
# Sougato Chakrobortty
# 01/04/2026 - 15/04/2026

import pygame as p # Import and shorten the pygame library
import random as r # Import and shorten the random library

p.init() # Initialize pygame

SIZE = (1000, 700) # Screen size (taken from assignment)
screen = p.display.set_mode(SIZE) # Setting mode to size variable
FPS = 60 # Frame rate
p.display.set_caption("Sougato's Mastermind") # Window title
FONT = p.font.Font('AgavePNF.ttf', 32) # Pass in my custom font file

colours = ["B", "R", "G", "Y", "W", "O"] # Define initial list of colours
pycolours = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 255, 255), (255, 165, 0)] # Matching pygame colours
background = (29, 31, 33) # Background colour
accent = (40, 42, 46) # Accent colour

def again(wrong = False): # Create a function asking the user, so it can be ran again; it assumes you're right until someone passes wrong
    screen.fill(background) # Clear screen

    # Check if the user got the answer
    if not wrong: # If the answer is not wrong
        pyprint("You are correct, well done!\nWould you like to play again?", 300, 300) # Ask user if they want to play again
    elif wrong: # If the user reached max guesses
        pyprint("Sorry, guess limit reached!\nWould you like to play again?", 300, 300) # Ask user if they want to play again

    pyprint("Yes!", 450, 400, pycolours[colours.index("R")]) # Yes option 
    pyprint("No!", 550, 400, pycolours[colours.index("R")]) # No option 

    cleared = False # Make a variable to end the loop later

    while not cleared: # Until the signal to clear has been given
        for event in p.event.get(): # Check every event
            if event.type == p.MOUSEBUTTONDOWN: # Check if clicked
                xpos, ypos = p.mouse.get_pos() # Get the coordinates (tuple)

                if 450 < xpos < 515 and 410 < ypos < 430: # Check if the yes button is pressed
                    cleared = True; # Permission to not run the loop again
                    main() # Run the game function to start it all over again
                if 550 < xpos < 615 and 410 < ypos < 430: # Check if the no button is pressed
                    quit() # End the program

def pyprint(text, x, y, bgcolour = background, clear = False): # Function to print quicker, with parameters
    if clear: # If clear is requested (unused for this program)
        screen.blit(FONT.render(text, True, bgcolour, bgcolour), (x, y)) # Fixed colour, text is black to hide old text
    else: # Otherwise, run normally
        screen.blit(FONT.render(text, True, pycolours[4], bgcolour), (x, y)) # Fixed colour, background is black to overwrite old text

    p.display.flip() # Update screen

def main(): # Make a main function, with the core game code so we can run it again if the user wants to play again
    screen.fill(background) # Clear screen

    pickcolours = colours[:] # Copy list, as I will remove from it
    gen = [] # Create a list with the generated values
    histlist = [] # Initialize history of guesses
    rightlist = [] # Initialize history of right & wrong positions
    pos = 0 # Initialize position of cursor

    for i in range(4): # Random 4 colours
        pickpos = r.randint(0, len(pickcolours) - 1) # Indexing
        pick = pickcolours[pickpos] # Random pick
        gen += pick # Add random colour to the list
        pickcolours.remove(pick) # Remove from list, so it can't appear again

    print(f"For debug purposes, the pattern is: {gen}") # Debugging message | Comment out when playing

    guesses = 1 # Count user guesses
    guess = [] # Clear guesses

    def pypattern(use, x, y): # Create a specific function to put colours on a screen
        if use[0] != "C": # Check that we aren't clearing
            for i in range(0, len(use)): # Loop as long as the given list
                if use[i] != "": # Only draw if the part of the list is not empty, so the partial guesses can be shown
                    p.draw.circle(screen, pycolours[colours.index(use[i])], (x + i * 75, y), 30) # Draw the colours
                p.display.flip() # Update screen
        else: # If we are clearing
            for i in range(0, 4): # Set amount since we know there's only 4 colours, and the empty list wouldn't have a len() of 4
                p.draw.circle(screen, accent, (x + i * 75, y), 30) # Paint over

    def updatehistory(usehist, useright, use, rightuse): # Create a function to update the history, allowing the lists to append to & list of colours to be passed in
        usehist.append(use) # Add the colours to the history list
        useright.append(rightuse) # Add the right & wrong colurs to the history list

        starty = 650 # First y position

        p.draw.rect(screen, accent, (0, 0, 325, 700)) # Draw a rectangle over the last guess text
        p.display.flip() # Update the screen

        for i in usehist: # Loop through history
            printright = str(useright[usehist.index(i)][0]) # The right amonut
            printwrong = str(useright[usehist.index(i)][1]) # The wrong amonut

            pypattern(i, 50, starty)  # Print the colour
            pyprint(f"R: {printright}, W: {printwrong}", 85, starty) # Print the right and wrong amonut

            starty -= 100 # Move the list up 1

        pyprint("History", 100, starty) # Print the history header

    pypattern(["C"], 600, 150) # Create a cleared prompt
    pypattern(colours, 525, 500) # Draw the colours, I'm not passing pycolours here since I already have the function programmed to convert the letters
    pyprint("Your guess: ", 370, 135) # Prompt
    pyprint("Colours: ", 340, 485) # Prompt

    def updateguess(): # Make a function to speed this up later
        pypattern(guess, 600, 150) # Call function and pass arguments to display guess

    while True: # Keep asking until right
        submitted = False # Originally not finished guessing (submit button will change this)

        if guesses == 9: # Check if max guesses reached
            # The following lines of code can be uncommented to debug the checking logic
            # print(histlist)
            # print(rightlist)

            again(True) # Send play again signal with the wrong bool

        if len(guess) < 4: # If it's position 4, the submit button will show, so this shouldn't conflict
            pyprint("Make Guess", 630, 400) # Placeholder for where the button was

        right = 0 # Initialize variable counting how many chars are right
        wrong = 0 # Initialize variable counting how many chars are wrong
        pyprint(f"Guess: #{guesses}", 630, 50) # Print guesses 

        # Pygame event loop
        for event in p.event.get(): # Check every event
            if event.type == p.MOUSEBUTTONDOWN: # Check if clicked
                xpos, ypos = p.mouse.get_pos() # Get the coordinates (tuple)

                startx = 525 # Centre of first circle
                starty = 500 # Base of the circle, always the same since we're in a line

                # Doing a square hitbox
                for i in range(len(colours)): # Going through the colour list
                    centrx = startx + (i * 75) # i * 75 is the gap between each circle, so this gets all the centres

                    if pos < 4 and (centrx - 30) < xpos < (centrx + 30) and (starty - 30) < ypos < (starty + 30): # Check if a colour is pressed
                        try: # In case the user wants to change his guess
                            guess[pos] = colours[i] # Replace that position
                        except: # If the user is not changing their guess, the position used above won't exist, so we just add the item
                            guess.append(colours[i]) # Append

                        pos += 1 # Update the position
                        updateguess() # Call since we have the guess

                    # Logic for when the submit button is drawn
                    if len(guess) == 4 and 630 < xpos < 790 and 400 < ypos < 430: # Check if the button is pressed
                        submitted = True # Allow submission

                startx = 600 # Set the new x level for the guesses
                starty = 150 # Set the new y level for the guesses

                # Square hitboxes again
                for i in range(len(guess)): # Going through the generated list
                    centrx = startx + (i * 75) # i * 75 is the gap between each circle, so this gets all the centres

                    if (centrx - 30) < xpos < (centrx + 30) and (starty - 30) < ypos < (starty + 30): # Check if a colour is pressed
                        pos = i # Change the position to the clicked button

        # Checking position and placing indicator
        if pos == 0: # We'll use lines as the indicators
            p.draw.line(screen, accent, (570, 200), (855, 200), 5) # Clear any indicators
            p.draw.line(screen, pycolours[colours.index("W")], (570, 200), (630, 200), 5) # Show indicator
        elif pos == 1:
            p.draw.line(screen, accent, (570, 200), (855, 200), 5) # Clear the last indicator
            p.draw.line(screen, pycolours[colours.index("W")], (645, 200), (705, 200), 5) # Show indicator
        elif pos == 2:
            p.draw.line(screen, accent, (570, 200), (855, 200), 5) # clear the last indicator
            p.draw.line(screen, pycolours[colours.index("W")], (720, 200), (780, 200), 5) # Show indicator
        elif pos == 3:
            p.draw.line(screen, accent, (570, 200), (855, 200), 5) # clear the last indicator
            p.draw.line(screen, pycolours[colours.index("W")], (795, 200), (855, 200), 5) # show indicator
        
        if len(guess) == 4: # what to do when the user has finished the guess
            pyprint("  Submit  ", 630, 400, pycolours[1]) # Draw submit button
            # The logic for the button being pressed is in the event loop above to prevent 2 event loops taking turns existing
            
        if submitted: # This means the button was pressed
            if len(guess) != len(set(guess)): # Check for duplicates, set() removes duplicates from the list
                pyprint(f"Duplicates found, edit answer", 480, 300) # Inform the user
                pos = 3 # Move to last position to try again
            elif guess != gen: # What to do if the user is wrong
                getright = [] # Keeping track of the characters the user got right

                for i in range(0, len(guess)): # Loop through the guesses
                    if guess[i] == gen[i]: # Check if the letter is matching the generated letter
                        right += 1 # Increase the amount of right chars
                        getright += guess[i] # Add it to the list of right characters

                for i in range(0, len(guess)): # Loop again, since the getright variable is finished
                    if guess[i] not in getright and guess[i] in gen: # Check if the character isn't one the player already got right, and if it's in the right answer
                        wrong += 1 # Add to characters in the wrong spot

                pyprint(f"Correct Spot: {right} Wrong Spot: {wrong}", 480, 300) # Fail message
                pyprint("Next Guess", 630, 400, pycolours[1]) # Next guess
                
                guesses += 1 # Count guesses
                cleared = False # Make a variable to end the loop later
                pos = 0 # Reset position

                while not cleared: # Wait for the event
                    for event in p.event.get(): # Check every event
                        if event.type == p.MOUSEBUTTONDOWN: # Check if clicked
                            xpos, ypos = p.mouse.get_pos() # Get the coordinates (tuple)

                            if 630 < xpos < 790 and 400 < ypos < 430: # Check if the button is pressed
                                updatehistory(histlist, rightlist, guess, [right, wrong]) # Update the history
                                guess = [] # Reset the guess
                                pypattern(["C"], 600, 150) # Send clear signal
                                cleared = True # Ask the loop to stop

            elif guess == gen: # If the user is correct
                again() # Play again 

main() # run the game for the first time
