from guizero import *
from view import View
from random import randint

class ViewDestroyDots(View):   
    def __init__(self, title="Destroy de dots", width=840, height=620, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)

        self.GRID_SIZE = 5
        self.score = 0
        self.instructions = Text(self.app, text="Click the dots to destroy them")
        self.board = Waffle(self.app, width=self.GRID_SIZE, height=self.GRID_SIZE, command=self.destroy_dot, dim = 80)
        self.board.after(1000, self.add_dot)
        self.score_display = Text(self.app, text="Your score is " + str(self.score))
        
        self.app.display()

    def add_dot(self):
        x, y = randint(0,self.GRID_SIZE-1), randint(0,self.GRID_SIZE-1)

        while self.board[x, y].dotty == True:
            x, y = randint(0,self.GRID_SIZE-1), randint(0,self.GRID_SIZE-1)

        self.board[x, y].dotty = True
        self.board.set_pixel(x, y, "red")

        speed = 2000

        if self.score > 30:
            speed = 200
        elif self.score > 20:
            speed = 400
        elif self.score > 10:
            speed = 500
        
        all_red = True

        for x in range(self.GRID_SIZE):
            for y in range(self.GRID_SIZE):
                if self.board[x,y].color != "red":
                    all_red = False
        if all_red:
            self.score_display.value = "You lost! Score: " + str(self.score)
            self.board.disable()
        else:
            self.board.after(speed, self.add_dot)

#PREGUNTA: Para que sirve este metodo?
    def destroy_dot(self,x,y):
        global score
        if self.board[x,y].dotty == True:
            self.board[x,y].dotty = False
            self.board.set_pixel(x, y, "white")
            self.score += 1
            self.score_display.value = "Your score is " + str(self.score)

#instancia para hacer pruebas
#p = ViewDestroyDots()