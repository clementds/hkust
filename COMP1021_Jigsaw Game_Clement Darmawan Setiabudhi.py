import turtle
import random
    
### This part of Python code will create the jigsaw pieces when starting up
### by setting up random positions and loading the corresponding image
def createJigsaw():
    global allTurtles

    # Initialize the variables of total number of rows and columns
    totalRows = 3
    totalColumns = 3
    # Now we go through the jigsaw piece row-column structure
    # Go through each row
    for row in range(totalRows):
        # Go through each column in this row
        for col in range(totalColumns):
            # Generate a random position
            x = random.randint( -int(turtle.window_width()/2) , int(turtle.window_width()/2))
            y = random.randint( -int(turtle.window_height()/2) , int(turtle.window_height()/2))
            # Make a new turtle
            newTurtle = turtle.Turtle()
            newTurtle.up()
            newTurtle.speed(0)
            # Move it to the random position
            newTurtle.goto(x, y)
            # Build the image file name
            theFilename = "image-"+str(row)+"-"+str(col)+".gif"
            # Add the image to the turtle system
            turtle.addshape(theFilename)
            # Apply the new image to this turtle
            newTurtle.shape(theFilename)

            
            # Now fix it so that when this turtle is dragged, it goes to the place where it is dragged
            newTurtle.ondrag(newTurtle.goto)
            # Add the new turtle to the new list of turtles
            allTurtles.append(newTurtle)
            
        
### This part of Python code will only run when the user presses "c" to check the jigsaw
def checkJigsaw():
    checkResult=True # At the start, we assume everything is OK

    for thisTurtle in allTurtles: # Go through every single turtle that we made
        thisX = thisTurtle.xcor() # Get the x coordinate of this turtle
        thisY = thisTurtle.ycor() # Get the y coordinate of this turtle
        
        # An example filename is "image-2-1.gif"
        theFilename = thisTurtle.shape() # Take the image filename of this turtle
        
        lengthOfFilenameWithoutExtension= len(theFilename)-4 # How long the filename is without the ".gif"
        theFilenameWithoutExtension=theFilename[ : lengthOfFilenameWithoutExtension ] # Remove the ".gif"
        FilenameWithoutExtension=theFilenameWithoutExtension.split("-") # Divide the filename into 3 pieces

        thisRow=FilenameWithoutExtension[1] # Take the Row number from the filename (the second piece of text)
        thisCol=FilenameWithoutExtension[2] # Take the Col number from the filename (the third piece of text)
        
        thisRow=int(thisRow) # Have to convert the text to an integer before comparing it with a number
        thisCol=int(thisCol) # Have to convert the text to an integer before comparing it with a number

        # We need to check this turtle with all other turtles for position violations
        for compareTurtle in allTurtles: # Go through every other turtle
            compareX = compareTurtle.xcor() # Get the x coordinate of the turtle
            compareY = compareTurtle.ycor() # Get the y coordinate of the turtle
            
            # An example filename is "image-2-1.gif"
            compareFilename = compareTurtle.shape() # Take the image filename of this turtle
            
            lengthOfCompareFilenameWithoutExtension= len(compareFilename)-4 # How long the filename is without the ".gif"
            compareFilenameWithoutExtension=compareFilename[ : lengthOfCompareFilenameWithoutExtension ] # Remove the ".gif"
            FilenameWithoutExtension=compareFilenameWithoutExtension.split("-") # Divide the filename into 3 pieces

            compareRow=FilenameWithoutExtension[1] # Take the Row number from the filename (the second piece of text)
            compareCol=FilenameWithoutExtension[2] # Take the Col number from the filename (the third piece of text)
            
            compareRow=int(compareRow) # Have to convert the text to an integer before comparing it with a number
            compareCol=int(compareCol) # Have to convert the text to an integer before comparing it with a number

            # Here, the four position violations will be checked
            # The jigsaw is wrong if any of them fails
            
            # The piece has a smaller column value but is on the right
            if thisCol < compareCol and thisX >= compareX:
                checkResult = False
                break

            # The piece has a larger column value but is on the left
            if thisCol > compareCol and thisX <= compareX:
                checkResult = False
                break
            # The piece has a smaller row value but is on the bottom
            if thisRow < compareRow and thisY <= compareY:
                checkResult = False
                break
            # The piece has a larger row value but is on the top
            if thisRow > compareRow and thisY >= compareY:
                checkResult = False
                break
            
    # Let's check the final result and show an appropriate message
    turtle.up()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.clear()
    turtle.color("red")
    turtle.goto(-40,-turtle.window_height()/2+40)
    if checkResult:
        print("Congratulations! Your jigsaw is correct!")
    else:
        print("Oh no! Your jigsaw is WRONG!!")

### Here is the main part of the program

allTurtles=[] # We will store all the turtles in this list

createJigsaw() # Create the jigsaw pieces
    
turtle.onkeypress(checkJigsaw, "c") # Press 'c' whenever you want to check the jigsaw

turtle.listen() # Listen for key presses

### Note: turtle.mainloop() is exactly the same as turtle.done()
turtle.mainloop() # Keep checking if anything is happening, if so do something appropriate

