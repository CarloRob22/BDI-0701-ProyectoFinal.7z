# Imports ---------------

from guizero import App, Text, Waffle
from random import randint


# Variables -------------

GRID_SIZE = 5
score = 0

# Functions -------------

#PREGUNTA: Para que sirve este metodo?
def add_dot():
    #DEFINICION: randint -> Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
    #PREGUNTA: Porque el limite maximo es GRID_SIZE-1?
    x, y = randint(0,GRID_SIZE-1), randint(0,GRID_SIZE-1)

    #DEFINICION: Waffle.dotty(parameter) -> Whether the pixels display as dots/circles (True) or squares (False)
    #PREGUNTA: Que hace esta sentencia?
    while board[x, y].dotty == True:
       x, y = randint(0,GRID_SIZE-1), randint(0,GRID_SIZE-1)

    #PREGUNTA: Que ahce esta sentencia?
    board[x, y].dotty = True

    #DEFINICION: Waffle.set_pixel(method) ->  Sets the pixel at the specified coordinates to the specified colour.
    #                                         0,0 is the top left of the grid.
    board.set_pixel(x, y, "blue")

    speed = 1000

    #PREGUNTA: Que hace esta sentencia?
    if score > 30:
        speed = 200
    elif score > 20:
        speed = 400
    elif score > 10:
        speed = 500
    
    all_red = True

    #PREGUNTA: Que hace esta sentencia?
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if board[x,y].color != "red":
                all_red = False
    if all_red:
        score_display.value = "You lost! Score: " + str(score)
    else:
        board.after(speed, add_dot)

#PREGUNTA: Para que sirve este metodo?
def destroy_dot(x,y):
    global score
    if board[x,y].dotty == True:
        board[x,y].dotty = False
        board.set_pixel(x, y, "white")
        score += 1
        score_display.value = "Your score is " + str(score)


# App -------------------

app = App("Destroy the dots")

instructions = Text(app, text="Click the dots to destroy them")

#DEFINICION Waffle -> display an n*n grid of squares with custom dimensions and padding.
#DEFINICION command(parameter) -> The name of a function to call when the waffle is clicked. This function MUST take either
#                                 zero or two arguments, if the function takes two arguments the x and y co-ordinates of the
#                                 pixel which was clicked will be given.
board = Waffle(app, width=GRID_SIZE, height=GRID_SIZE, command=destroy_dot)

#DEFINICION: Waffle.after(method) -> Schedules a single call to command after time milliseconds. (To repeatedly call the same 
#                                    command, use repeat())
board.after(1000, add_dot)

#DEFINICION: Text -> displays non editable text in your app, useful for titles, labels and instructions.
score_display = Text(app, text="Your score is " + str(score))

app.display()
