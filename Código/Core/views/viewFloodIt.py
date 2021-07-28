from guizero import *
from .view import View
import random

class ViewFloodIt(View):   
    def __init__(self, title="Flood it!", width=840, height=620, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)

        self.colours = ["red", "blue", "green", "yellow", "magenta", "purple"]
        self.board_size = 14
        self.moves_limit = 25
        self.moves_taken = 0

        self.board = Waffle(self.app, width=self.board_size, height=self.board_size, pad=0)
        self.palette = Waffle(self.app, width=6, height=1, dotty=True, command=self.start_flood)

        self.win_text = Text(self.app)

        self.fill_board()
        self.init_palette()

    # Recursively floods adjacent squares
    def flood(self, x, y, target, replacement):
        # Algorithm from https://en.wikipedia.org/wiki/Flood_fill
        if target == replacement:
            return False
        if self.board.get_pixel(x, y) != target:
            return False
        self.board.set_pixel(x, y, replacement)
        if y+1 <= self.board_size-1:   # South
            self.flood(x, y+1, target, replacement)
        if y-1 >= 0:            # North
            self.flood(x, y-1, target, replacement)
        if x+1 <= self.board_size-1:    # East
            self.flood(x+1, y, target, replacement)
        if x-1 >= 0:            # West
            self.flood(x-1, y, target, replacement)

    # Check whether all squares are the same
    def all_squares_are_the_same(self):
        squares = self.board.get_all()
        if all(colour == squares[0] for colour in squares):
            return True
        else:
            return False

    def win_check(self):
        global moves_taken
        self.moves_taken += 1
        if self.moves_taken <= self.moves_limit:
            if self.all_squares_are_the_same():
                self.win_text.value = "You win!"
        else:
            self.win_text.value = "You lost :("


    def fill_board(self):
        for x in range(self.board_size):
            for y in range(self.board_size):
                self.board.set_pixel(x, y, random.choice(self.colours))

    def init_palette(self):
        for colour in self.colours:
            self.palette.set_pixel(self.colours.index(colour), 0, colour)

    def start_flood(self,x, y):
        flood_colour = self.palette.get_pixel(x,y)
        target = self.board.get_pixel(0,0)
        self.flood(0, 0, target, flood_colour)
        self.win_check()
