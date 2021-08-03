from genericpath import getatime
from tkinter.constants import TOP
from guizero import *
from .view import View
import random
import time
import json

class ViewFloodIt(View):   
    def __init__(self, title="Flood it!", width=900, height=700, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)

        self.colours = ["red", "blue", "green", "yellow", "magenta", "purple"]
        self.board_size = 14
        self.moves_limit = 25
        self.moves_taken = 0
        self.startTim = {}
        self.second = 0
        self.minutes = 0
        self.hours = 0
        self.aux_hour =0 
        self.aux_min = 0
        self.aux_sec = 0
        self.state = True  
        self.listMoves = []          
    
        self.BoxWaff = Box(self.app, layout="auto", align="left")
        #cuadricula de colores, su tamaño se modifico mediante la propiedad dim        
        self.board = Waffle(self.BoxWaff, width=self.board_size, height=self.board_size, pad=0, dim=35)        
        self.palette = Waffle(self.BoxWaff, width=6, height=1, dotty=True, command=self.start_flood)
        self.win_text = Text(self.BoxWaff)
        self.moves=Text(self.BoxWaff)
        
        self.BoxBotton =Box(self.app, layout="auto", align="left", border=True, width="fill", height="fill")
         
        self.BoxBottonL =Box(self.BoxBotton, align="left", width="fill", height="fill")
        self.pauseGame = PushButton(self.BoxBottonL, text="Pause", command=self.pause, width="fill", height="fill")               
        self.Rewind = PushButton(self.BoxBottonL, text="Rewind", command=self.stepRewind, width="fill", height="fill")
        self.Defeat = PushButton(self.BoxBottonL, text="Declare Defeat", command=self.declareDefeat, width="fill", height="fill")
        self.BoxBottonR =Box(self.BoxBotton, align="left", width="fill", height="fill")    
        self.timer = Text(self.BoxBottonR, text="")
        
        self.fill_board()
        self.init_palette()
        self.startTime()
        self.gameTime()      
        self.app.display()
         
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
        self.moves.value = 'Movimientos realizados: ' + str(self.moves_taken)
        if self.moves_taken <= self.moves_limit:
            if self.all_squares_are_the_same():
                self.win_text.value = "You win!"
        else:
            self.win_text.value = "You lost :("
    
    #mediante la siguiente función se obtinene el tablero inicial de la partida.
    def get_start_board(self,b_init):
                        
            self.listMoves.append(self.board.get_all())

    def fill_board(self):
        for x in range(self.board_size):
            for y in range(self.board_size):
                self.board.set_pixel(x, y, random.choice(self.colours))
        self.get_start_board(self.board)
        self.listMoves.append(self.board.get_all())
        

    def init_palette(self):
        for colour in self.colours:
            self.palette.set_pixel(self.colours.index(colour), 0, colour)

    def start_flood(self,x, y):
        flood_colour = self.palette.get_pixel(x,y)
        target = self.board.get_pixel(0,0)
        self.flood(0, 0, target, flood_colour)
        self.win_check()
        self.lastMove(self.board)
      
    #mediante la siguiente función se obtiene la hora de inicio del juego en formato HH:MM:SS.  
    def startTime(self):
        hour = time.strftime("%H")
        min = time.strftime("%M")
        sec = time.strftime("%S")
        
        self.startTim = {
            "hour":hour,
            "min":min,
            "sec":sec
        }  
        print(self.startTim["sec"])  
    
    
    #Mediante la siguiente función se inicia el tiempo del juego desde (00:00:00).               
    
    def gameTime(self):              
        if (self.state):
            sec = time.strftime("%S")
            self.second = self.second + (int(sec)-(int(sec))) +1    
            self.aux_sec = self.second
            
            if self.aux_sec == 60:
                self.aux_sec = "0"
                self.aux_min = self.aux_min + 1
                self.second = 0
                
            if self.aux_min == 60:
                self.aux_min = "0"
                self.aux_hour= self.aux_hour + 1
                self.min = 0
            
            self.timer.tk.config(text="{}:{}:{}".format(str(self.aux_hour).zfill(2),str(self.aux_min).zfill(2),str(self.aux_sec).zfill(2)))                                            
            
            self.timer.tk.after(1000, self.gameTime)
            
    #Mediante la siguiente función se pausa el tiempo del juego. La función es llamada desde el botón "pause"
    def pause(self):
        if self.state:       
            self.pauseGame.text = "Continue"    
            self.state = False
            self.palette.enabled = False
        else:
            self.state = True
            self.palette.enabled = True
            self.pauseGame.text =  "Pause"
            self.gameTime()
    
    #Mediante la siguiente fución se elimina el ultimo movimiento que hubo en el juego. La función es llamada desde el botón "Rewind".
    def stepRewind(self):
        self.board.pixel(2,2).color = "red"

    #Mediante la siguiente función se declara el juego en estado de derrota. La función es llamada desde el botón "Declare Defeat" 
    def declareDefeat(self):
        pass
    
    #mediante la siguiente función se obtiene el ultimo moviento realizado.
    def lastMove(self, board):
        self.listMoves.append(board)
        print(self.board.get_all())
        return self.board.get_all()
        
    
    
        
#instancia para pruebas :