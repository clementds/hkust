# Done by SETIABUDHI, Clement Darmawan. SID: 20817485.

import random               # Import the 'random' library
import turtle               # Import the 'turtle' library

wanted_number = 0           # This stores the number to be guessed here
finished = False            # This is true if the game has finished
user_guess_text = ""        # This stores a text
user_guess = 0              # This stores a number
total_guess = 0             # This counts the total guesses
valid_number = False        # This is true if the number is valid
x_position = -200           # This is the initial x-axis position
y_position = 200            # This is the initial y-axis position

# Hide pen lines
turtle.up() 

# Generate a new integer random number
wanted_number = random.randint(1,100)
turtle.goto(x_position, y_position)
turtle.write("I am thinking of a number. What number am I thinking of?", font=("Arial", 10, "bold"))
y_position = y_position - 20

# Do the main game loop
while not finished:
    
    # Get the user's guess
    user_guess_text = turtle.textinput("Guessing Game",
                                       "Please enter a number between 1 and 100: ")

    # Check if the user's guess is a valid number
    try:
        user_guess = int(user_guess_text)
    except ValueError:
        turtle.goto(x_position, y_position)
        turtle.write("That is not a valid number!", font=("Arial", 10, "bold"))
        y_position = y_position - 20
        valid_number = False
    else:
        user_guess = int(user_guess_text)
        total_guess = total_guess + 1
        valid_number = True
            
    # Check the accuracy of the user's guess
    if valid_number == True:
        if user_guess < 1 or user_guess > 100:
            turtle.goto(x_position, y_position)
            turtle.write("Please enter a number between 1 and 100.", font=("Arial", 15, "bold"))
            y_position = y_position - 20
        elif user_guess > wanted_number:
            turtle.goto(x_position, y_position)
            turtle.write("Too high.", font=("Arial", 15, "bold"))
            y_position = y_position - 20
        elif user_guess < wanted_number:
            turtle.goto(x_position, y_position)
            turtle.write("Too low.", font=("Arial", 15, "bold"))
            y_position = y_position - 20
        else:
            finished = True
        
# At this point, the game has finished
turtle.goto(x_position, y_position)
turtle.write(("You got it! My number is " + str(wanted_number) + "."), font=("Arial", 10, "bold"))
y_position = y_position - 20
turtle.goto(x_position, y_position)
turtle.write(("It took you " + str(total_guess) + " guesses to get the number."), font=("Arial", 10, "bold"))
y_position = y_position - 20

# Finish the code
turtle.done
