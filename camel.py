"""Camel: A dos game ported to a cross platform solution.
Was originally: Camel Source Code for the BrailleNote, written in Rapid Euphoria
Original author: Louis Bryant
Modified by Nathaniel Schmidt <schmidty2244@gmail.com>
Date modified: 09/09/2020; 23/01/2021

You have permission to modify and redistribute this code and software with or without changes.
Pulse Data International, Rapid Deployment Software, Programmers of other included files, and I take no responsibility for damages you cause by your modifying this software.

This code and software is provided 'as is' without any implied or express warranty."""

import random, time

# Game Starts Here.

# First, let's declare some global variables - bad practice but easier when translating from such a basic language such as euphoria:
you = 0, # Where you are.
Lions = 0, # The lions location.
drinks = 0, # How many drinks you have left.
gocommands = 0, # How many commands you have before you need another drink.
days = 0, # How many good days your camel has left.
n = 0 # Temporary random number usages.
mainInput = None # Stores the user presses here.

# Now, let's set up routines that initializes the variables:

def init() # The function is called init.
    you = 0 # You haven't gone anywhere.
    lions = 25 # The lions are 25 miles ahead of you.
    drinks = 6 # You have six drinks left in your canteen.
    gocommands = 4 # You have 4 commands without drinking.
    days = 7 # Your camel has 7 good days left.

# Now let's start the game.

def gameStatus ()
    # Check where you are before letting you proceed.
    # Did you win? Or did the lions capture you?
    # Or, maybe, you are still alive.
    if you > 199:# You made it!
        print("YOU WIN! A party is given in your honor! ")
        print("The lions have been tamed and are planning to attend. ")
    
    if you > lions: # You are ahead of the lions.
        # Let them move.
        lions += rand(20) # Move at a random speed.
    
    if lions >= you and you >30:
        print("THE lions HAVE CAPTURED YOU!
        print ("CAMEL AND PEOPLE SOUP IS THEIR FAVORITE DISH. ")
    if gocommands < 3: # You had better get a drink.
        print("W A R N I N G -- GET A DRINK ")
    if gocommands == 0: # Too many commands without drinking.
        print("YOU RAN OUT OF WATER... SORRY CHUM!!!!!! ")
    # What about your camel?
    if days < 1: # You ran your camel to death!
        print("YOU DIRTY LOUSY RAP SCALLION!!! ")
        print("YOU RAN YOUR INNOCENT CAMEL TO DEATH! ")
    
    # Well? Let's continue!
    if you = 0: # You are just starting.
        print("You are in the middle of the desert at an oases. ")
    
    if you > 25:
        lions += rand(10)
        print("The lions are " + you-lions + " miles behind you.")
    
    print("You have travelled " + you + " miles altogether, and have " + 200-you + " more miles to go.")

def main ()
    print("Welcome to The Game Of Camel. ")
    mainInput = input("Would you like instructions? Type Y for yes or N for no. ")
    mainInput = mainInput.upper ()
    
    while mainInput != "Y" and mainInput != "N":
        print ("Please enter either 'y' or 'n'")
        mainInput = input("Would you like instructions? Type Y for yes or N for no. ")
        mainInput = mainInput.upper ()
    
    if mainInput == 'Y'
        # Give the instructions now.
        print("Welcome to the game of Camel. ")
        print("The object of the game is to travel 200 miles across the Great Desert. ")
        print("A pride of nasty, ravenous lions will be chasing you. ")
        print("You will be asked for commands every so often. ")
        print("C O M M A N D S: ")
        print("1 -- drink from your canteen, ")
        print("2 -- move ahead moderate speed, ")
        print("3 -- move ahead fast speed, ")
        print("4 -- stop for a rest, ")
        print("5 -- status check, ")
        print("and 6 -- hope for help. ")
        print("You will get a quart of water which will last you six drinks. ")
        print("You must renew your water supply at an Oases completely. ")
        print("You get a half quart if found by help. ")
        print("If help does not find you after command '6', you lose. ")
    
    init() # Call the subroutine to initialize the variables.
    print("Good luck and good cameling! ")
    gameStatus ()
    
    mainInput = int(input("Your command?")) # Wait for the user to enter something
    if mainInput == 1: # Have a drink
        # Drink from your canteen.
        if drinks = 0:
            print("YOU RAN OUT OF WATER. SORRY CHUM!!!!!! ")
        else: # Get a drink?
            drinks -= 1
            print("BETTER WATCH FOR A OASIS. ")
            gocommands = 4 # Reset how many commands you can go before drinking.
        
    elif mainInput == 2:
        # Walk normally.
        you += rand(5) # Move randomly from 1 to 5 miles.
        days -= 1 # Subtract one day from the camel.
        print("Your camel likes this paste! ")
        gocommands -= 1 # Subtract commands you have before drinking.
    elif mainInput == 3:
        # So try to run!
        gocommands -= 1 # You wasted one more command.
        n = rand(4) # What happens here?
        # Let's see.
        if n = 1 then # The Note-taker chose the first action.
            # The first action is a sand-storm.
            print("YOU HAVE BEEN CAUGHT IN A SAND-STORM... ")
            print("GOOD LUCK! ")
            you += rand(5) # Slow down.
        elsif n = 2 then # The Note-taker chose to perform the second action. This action is to let your camel find an oases.
            print("You have stopped at an Oases. Your camel is ")
            print("filling your canteen and eating figs. ")
            drinks = 6 # Put six more drinks in the canteen.
            gocommands = 4 # Reset the commands.
            n = 4 # Force the Note-taker to do the last action.
        elif n == 3: # Oops! The Note-taker chose the third action. This action gets you caught by a hidden crazy kidnapper.
            print("YOU HAVE BEEN CAPTURED BY HIDDEN CRAZY KIDNAPPERS. ")
            print("Luckily the local council has agreed to their ransom-demands...")
            print("You have a new set of commands. ")
            print("#7 attempt an escape, or #8 wait for payment.")
            mainInput = int(input("Your sub-command? "))
            if mainInput == 7: # The number seven was pressed.
                # Attempt an escape.
                n = rand(2) # One of two things can happen.
                if n == 1: # You made it.
                    print("CONGRATULATIONS! YOU SUCCESSFULLY ESCAPED! ")
                else: # Well, you didn't make it.
                    print("You were mortally wounded by a gunshot wound while trying to escape. ")
            elsif mainInput == 8: # The number eight was pressed.
                print("Your ransom has been payed and you are free to go. The local council is collecting. ")
                print("Just Wait ")
                wait(10) # Stop for ten seconds.
                you += rand(3) # Move from one to three miles.
                # The kidnapper slowed you down.
        elif n = 4 then # Your camel is burning across the desert sands.
            you += rand(20) # Randomly move from one to twenty miles.
            print("Your camel is burning across the desert sands. ")
            days -= 3 # Subtract three days from your camel.
        
# You should never get here unless you press number 4.

    elif mainInput == 4: # let the camel rest.
        print("Your camel thanks you. ")
        days = 7 # You now have seven good days left.
        gocommands -= 1 # Lose one more command.
    elif mainInput == 5: # Status Check Please?
        print("Your camel has " + days + " good days left. You have " + drinks + " drinks left in the canteen. You can go " + gocommands + " commands without drinking. BETTER WATCH FOR AN OASES. ")
    elif mainInput == 6: # HELP!
        n = rand(2) # Chose whether to give out help or not.
        if n == 1: # Give Help.
            print("Help has found you in a state of unconsciousness. ")            # Let the camel rest for a while.
            days = 7 # Your camel is rejubinated.
            drinks = 3 # You get the half-quart of water.
            # You drink some water and get more commands.
            gocommands = 8 # You now have eight commands without drinking.
        else: # Help hasn't found you.
            # Do something!
    else: # Invalid option.
print("Invalid Option. ")
print("The commands you can choose from are: ")
print("1 -- drink from your canteen ")
print("2 -- move ahead moderate speed ")
print("3 -- move ahead fast speed ")
print("4 -- stop for a rest ")
print("5 -- status check ")
print("6 -- hope for help ")

if line = 3 then # This isn't a loop. It generates
# loser statements.
n = rand(4) # We have five loser statements.
print("Your body and soul lay a rest in the sand. ")
if n = 1 then # This is the first loser statement.
print("The National's Camel Union is not attending your funeral!!!!!! ")
elsif n = 2 then # This is the second loser statement.
print("Your body was eaten by voltures and hyenas!!!!!! ")
elsif n = 3 then # This is the fourth loser statement.
print("People with little inteligence should stay out of the desert. ")
elsif n = 4 then # This is the last loser statement.
print("Turkeys should fly, not ride camels. ")end if # No more loser statements.

print("Want another camel and a new game? ")
key = wait_key() # Wait for the user to enter something
print('\n')
if key = 'y' or key = 'Y' then # Yes was entered.
line = 1 # Jump to the first while-loop.
exit # Start all over.
elsif key = 'n' or key = 'N' then # No was entered.
# So abort after the last comment.
print("CHICKEN! ")
sleep(5) # Suspend execution for five seconds.
abort(0) # Shutdown the program.
end if # Y or N wasn't pressed, so re-ask the question.
end while
end while

if __name__ == "__main__":
    main ()
# End of program.
