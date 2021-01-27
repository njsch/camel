"""Camel: A dos game ported to a cross platform solution.
Was originally: Camel Source Code for the BrailleNote, written in Rapid Euphoria
Original author: Louis Bryant
Modified by Nathaniel Schmidt <schmidty2244@gmail.com>
Date modified: 09/09/2020; 23/01/2021

You have permission to modify and redistribute this code and software with or without changes.
Pulse Data International, Rapid Deployment Software, Programmers of other included files, and I take no responsibility for damages you cause by your modifying this software.

This code and software is provided 'as is' without any implied or express warranty."""

from random import randint
from time import sleep

# First, let's declare some global variables - bad practice but easier when translating from such a basic language such as euphoria:
you = 0 # Where you are.
hyenas = 0 # The hyenas location.
drinks = 0 # How many drinks you have left.
gocommands = 0 # How many commands you have before you need another drink.
days = 0 # How many good days your camel has left.
n = 0 # Temporary random number usages.
mainInput = 0 # Stores the user presses here.
gameLost = False# Whether you have lost, mainly for the printLoss function.

def queryInstructions (prompt):
    """Ask the user whether they want instructions, then recursively query the user for instructions until the user declines.
    @param prompt: The output prompt containing the query for the user to answer.
    @type prompt: str"""
    global mainInput
    instructions = """Welcome to the game of Camel. 
The object of the game is to travel 200 miles across the Great Desert. 
A pack of nasty, ravenous hyenas will be chasing you. 
You will be asked for commands every so often. 

C O M M A N D S: 
1 -- drink from your canteen, 
2 -- move ahead moderate speed, 
3 -- move ahead fast speed, 
4 -- stop for a rest, 
5 -- status check, 
6 -- hope for help,
7 -- exit,
And 8 -- request help to list available commands.

You will get a quart of water which will last you six drinks. 
You must renew your water supply at an Oases completely. 
You get a half quart if found by help. 
If help does not find you after command '6', you lose."""
    
    mainInput = input(prompt)
    mainInput = mainInput.upper ()
    
    while mainInput != "Y" and mainInput != "N":
        print ("Please enter either 'y' or 'n'")
        mainInput = input("Would you like instructions? Type Y for yes or N for no. ")
        mainInput = mainInput.upper ()
    
    if mainInput == 'Y':
        print (instructions)
        queryInstructions ("Would you like to hear the instructions again? Type Y for yes or N for no.")
    else:
        print("Good luck and good cameling! ")

# Now, let's  initialize the variables:
def init():
    """Initialise global variable identifiers with required initial value assignments to allow the game to start."""
    global you
    global hyenas
    global drinks
    global gocommands
    global days

    you = 0 # You haven't gone anywhere.
    hyenas = 25 # The hyenas are 25 miles ahead of you.
    drinks = 6 # You have six drinks left in your canteen.
    gocommands = 4 # You have 4 commands without drinking.
    days = 7 # Your camel has 7 good days left.

def printLoss ():
    """Print a random loss message from a randomised selection."""
    global n
    n = randint(1, 4) # We have five loser statements.
    print("Your body and soul lay a rest in the sand. ")
    if n == 1: # This is the first loser statement.
        print("The National's Camel Union is not attending your funeral!!!!!! ")
    elif n == 2: # This is the second loser statement.
        print("Your body was eaten by voltures and hyenas!!!!!! ")
    elif n == 3: # This is the fourth loser statement.
        print("People with little inteligence should stay out of the desert. ")
    elif n == 4: # This is the last loser statement.
        print("Turkeys should fly, not ride camels. ") # No more loser statements.

def queryReplay ():
    """Ask whether to play the game again or exit."""
    global gameLost
    global mainInput
    if gameLost == True:
        printLoss ()
    mainInput = input ("Want another camel and a new game? (Pres Y for yes or N for no) ")
    mainInput = mainInput.upper ()
    
    while mainInput != 'Y' and mainInput != 'N':
        print ("Please enter either 'Y' or 'N'")
        mainInput = input ("Want another game? (Pres Y for yes or N for no) ")
        mainInput = mainInput.upper ()
    if mainInput == 'Y':
        gameLost = False
        main ()
    else:
        print ("Chicken!")
        exit ()

def gameStatus ():
    """Figure out what to do based on the current state of global vars."""
    global you
    global hyenas
    global drinks
    global gocommands
    global days
    global gameLost

    # Check where you are before letting you proceed.
    # Did you win? Or did the hyenas capture you?
    # Or, maybe, you are still alive.
    if you > 199: # You made it!
        print("YOU WIN! A party is given in your honor! ")
        print("The hyenas have been tamed and are planning to attend. ")
        queryReplay ()
    
    if you > hyenas: # You are ahead of the hyenas.
        # Let them move.
        hyenas += randint(1, 20) # Move at a random speed.
    
    if hyenas >= you and you >30:
        print("THE hyenas HAVE CAPTURED YOU!")
        print ("CAMEL AND PEOPLE SOUP IS THEIR FAVORITE DISH. ")
        gameLost = True
        queryReplay ()
    
    if gocommands < 3: # You had better get a drink.
        print("W A R N I N G -- GET A DRINK ")
    if gocommands == 0: # Too many commands without drinking.
        print("YOU RAN OUT OF WATER... SORRY CHUM!!!!!! ")
        gameLost = True
        queryReplay ()
    # What about your camel?
    if days < 1: # You ran your camel to death!
        print("YOU DIRTY LOUSY RAP SCALLION!!! ")
        print("YOU RAN YOUR INNOCENT CAMEL TO DEATH! ")
        gameLost = True
        queryReplay ()
    
    # Well? Let's continue!
    if you == 0: # You are just starting.
        print("You are in the middle of the desert at an oases. ")
    
    if you > 25:
        hyenas += randint(1, 10)
        print("The hyenas are " + you-hyenas + " miles behind you.")
    
    print("You have travelled {0} miles altogether, and have {1} more miles to go.".format (you, 200-you))

# Now let's start the game.
def main ():
    """Main procedure for the game."""
    global you
    global hyenas
    global drinks
    global gocommands
    global days
    global n
    global gameLost
    global mainInput
    
    print("Welcome to The Game Of Camel. ")
    queryInstructions ("Would you like to hear game instructions? Type Y for yes or N for no.")
    
    init() # Call the function to initialize the variables.
    gameStatus ()
    
    while gameLost != True:
        while True:
            try:
                mainInput = int(input("Your command?"))
                break
            except ValueError:
                print ("Make sure you only enter a number.")
                continue
        if mainInput == 1: # Have a drink
            # Drink from your canteen.
            if drinks == 0:
                print("YOU RAN OUT OF WATER. SORRY CHUM!!!!!! ")
                gameLost = True
                queryReplay ()
            else: # Get a drink?
                drinks -= 1
                print("BETTER WATCH FOR A OASIS. ")
                gocommands = 4 # Reset how many commands you can go before drinking.
                gameStatus ()
            
        elif mainInput == 2:
            # Walk normally.
            you += randint(1, 5) # Move randomly from 1 to 5 miles.
            days -= 1 # Subtract one day from the camel.
            print("Your camel likes this pace! ")
            gocommands -= 1 # Subtract commands you have before drinking.
            gameStatus ()
        elif mainInput == 3:
            # So try to run!
            gocommands -= 1 # You wasted one more command.
            gameStatus ()
            n = randint(1, 4) # What happens here?
            # Let's see.
            if n == 1: # The computer chose the first action.
                # The first action is a sand-storm.
                print("YOU HAVE BEEN CAUGHT IN A SAND-STORM... ")
                print("GOOD LUCK! ")
                you += randint(1, 5) # Slow down.
                gameStatus ()
            elif n == 2: # The Note-taker chose to perform the second action. This action is to let your camel find an oases.
                print("You have stopped at an Oases. Your camel is filling your canteen and eating figs. ")
                drinks = 6 # Put six more drinks in the canteen.
                gocommands = 4 # Reset the commands.
                gameStatus ()
                n = 4 # Force the Note-taker to do the last action.
            elif n == 3: # Oops! The Note-taker chose the third action. This action gets you caught by a hidden crazy kidnapper.
                print("YOU HAVE BEEN CAPTURED BY some HIDDEN CRAZY KIDNAPPERS. ")
                print("Luckily the local council has agreed to their ransom-demands...")
                print("You have a new set of commands. ")
                print("#7 attempt an escape, or #8 wait for payment.")
                subInput = int(input("Your sub-command? "))
                if subInput == 7: # The number seven was pressed.
                    # Attempt an escape.
                    n = randint(1, 2) # One of two things can happen.
                    if n == 1: # You made it.
                        print("CONGRATULATIONS! YOU SUCCESSFULLY ESCAPED! ")
                    else: # Well, you didn't make it.
                        print("You were mortally wounded by a gunshot wound while trying to escape. ")
                        gameLost = True
                        queryReplay ()
                elif subInput == 8: # The number eight was pressed.
                    print("Your ransom has been payed and you are free to go. The local council is collecting. ")
                    print("Just Wait ")
                    sleep(10) # Stop for ten seconds.
                    you += randint(1, 3) # Move from one to three miles.
                    # The kidnapper slowed you down.
            elif n == 4: # Your camel is burning across the desert sands.
                you += randint(6, 20) # Randomly move from one to twenty miles.
                print("Your camel is burning across the desert sands. ")
                days -= 3 # Subtract three days from your camel.
                gameStatus ()
            
    # You should never get here unless you press number 4.
        elif mainInput == 4: # let the camel rest.
            print("Your camel thanks you. ")
            days = 7 # You now have seven good days left.
            gocommands -= 1 # Lose one more command.
            gameStatus ()
        elif mainInput == 5: # Status Check Please?
            print("Your camel has {0} good days left. You have {1} drinks left in the canteen. You can go {2} commands without drinking.".format(days, drinks, gocommands))
        elif mainInput == 6: # HELP!
            n = randint(1, 2) # Chose whether to give out help or not.
            if n == 1: # Give Help.
                print("Help has found you in a state of unconsciousness. ")                # Let the camel rest for a while.
                days = 7 # Your camel is rejubinated.
                drinks = 3 # You get the half-quart of water.
                # You drink some water and get more commands.
                gocommands = 8 # You now have eight commands without drinking.
                gameStatus ()
            else: # Help hasn't found you.
                print ("You waited, and waited... and waited... but no help arrived.")
                gameLost = True
                queryReplay ()
        elif mainInput == 7: # Exit
            exitQuery = input ("Are you sure you want to exit? Press Y or N.")
            exitQuery = exitQuery.upper ()
            while exitQuery != "Y" and exitQuery != "N":
                print ("Please enter either Y or N.")
                exitQuery = input ("Are you sure you want to exit? Press Y or N.")
                exitQuery = exitQuery.upper ()
            if exitQuery == "Y": 
                exit ()
            else:
                print ("Okay.")
        if mainInput == 8: # request program help
            print("The commands you can choose from are: ")
            print("1 -- drink from your canteen ")
            print("2 -- move ahead moderate speed ")
            print("3 -- move ahead fast ]speed ")
            print("4 -- stop for a rest ")
            print("5 -- status check ")
            print("6 -- hope for help ")
            print ("7 - exit")
            print ("8 - get program help and list commands.")

        else: # Invalid option.
            print("Invalid Option. ")
            print("The commands you can choose from are: ")
            print("1 -- drink from your canteen ")
            print("2 -- move ahead moderate speed ")
            print("3 -- move ahead fast ]speed ")
            print("4 -- stop for a rest ")
            print("5 -- status check ")
            print("6 -- hope for help ")
            print ("7 - exit")
            print ("8 - get program help and list commands.")

if __name__ == "__main__":
    main ()
# End of program.
