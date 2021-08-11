from genericpath import getatime
from tkinter.constants import TOP
from guizero import *
from .View import View
import random
import time
import json

class FloodItView(View):   
    def __init__(self, gEngine,returning, title="Flood it!", width=900, height=700, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)
        self.gEngine = gEngine        
        self.returning = returning        
        self.colours = ["red", "blue", "green", "yellow", "magenta", "purple"]
        self.board_size = 14
        self.moves_limit = 25
        self.moves_taken = 0
        self.initialBoard = None
        self.startTim = {}
        self.second = 0
        self.minutes = 0
        self.hours = 0
        self.aux_hour =0 
        self.aux_min = 0
        self.aux_sec = 0
        self.stateTime = True  
        self.listMoves = []    
        self.varGameTime = "" 
        self.suc = None   
        self.holDef = 'h' 
        self.stateMatch = 2 # se utiliza para llevar de manera globar el estado de la partida, su valor por defecto es necesario que sea 2.
    
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
        self.matchOnHold()
        
         
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
    
    #mediante la siguiente función el juego detecta cuando el usuario gano el juego y nos manda al score personal.    
    def win_check(self):
        global moves_taken
        self.moves_taken += 1  
           
        move = {
            "no":self.moves_taken,
            "move": self.board.get_all()
        }     
        rmove=json.dumps(move)   
        self.gEngine.addMovementMatch(self.varGameTime ,rmove)      
             
        if self.moves_taken == self.moves_limit:
            self.suc = True
        self.moves.value = 'Movimientos realizados: ' + str(self.moves_taken)         
        if self.moves_taken < self.moves_limit:            
            if self.all_squares_are_the_same():
                self.win_text.value = "You win!" 
                self.stateTime = False
                self.gEngine.successfulMatch(self.varGameTime, 5)
                self.palette.enabled = False              
        else:            
            self.win_text.value = "You lost :(" 
            self.stateTime = False
            self.gEngine.successfulMatch(self.varGameTime, 5)           
            self.palette.enabled = False            
            popUpLoser = self.app.info("Perdiste", "Haz perdido esta partida, suerte a la próxima")
            popUpLoser = True
            if popUpLoser == True:    
                pass
                #self.app.destroy()
                #playerInt = StartPlayerView()
                
    
    #mediante la siguiente función se obtinene el tablero inicial de la partida.
    def get_start_board(self,b_init):
        self.initialBoard = b_init
        self.listMoves.append(b_init)
        
           

    def fill_board(self):
        for x in range(self.board_size):
            for y in range(self.board_size):
                self.board.set_pixel(x, y, random.choice(self.colours))
        self.get_start_board(self.board.get_all())   
        
        move = {
            "no":0,
            "move": self.board.get_all()
        }     
        
        rmove=json.dumps(move)   
        self.gEngine.addMovementMatch(self.varGameTime ,rmove)
         

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
        if (self.stateTime):
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
            
            self.varGameTime = "{}:{}:{}".format(str(self.aux_hour).zfill(2),str(self.aux_min).zfill(2),str(self.aux_sec).zfill(2))            
            self.timer.tk.config(text="{}:{}:{}".format(str(self.aux_hour).zfill(2),str(self.aux_min).zfill(2),str(self.aux_sec).zfill(2)))                                                        
            self.timer.tk.after(1000, self.gameTime)
            
    #Mediante la siguiente función se pausa el tiempo del juego. La función es llamada desde el botón "pause"
    def pause(self):        
        if self.stateTime:       
            self.gEngine.updateStateMatch(3)
            self.pauseGame.text = "Continue"    
            self.stateTime = False
            self.palette.enabled = False
        else:
            self.gEngine.updateStateMatch(1)
            self.stateTime = True
            self.palette.enabled = True
            self.pauseGame.text =  "Pause"
            self.gameTime()
    
    #Mediante la siguiente fución se elimina el ultimo movimiento que hubo en el juego. La función es llamada desde el botón "Rewind".
    def stepRewind(self):
        if len(self.listMoves)>1:            
            self.fillRewind()  
            self.gEngine.delMovement()                  
            self.moves_taken -= 1
            self.moves.value = 'Movimientos realizados: ' + str(self.moves_taken)
        print(self.listMoves)        
     
    def ReturnBack(self):        
        if self.returning==1:            
            from .StartAdminView import StartAdminView
            self.gEngine.successfulMatch(self.varGameTime, self.stateMatch)
            viewLogin = StartAdminView(self.gEngine, "Admin Start Menu")   
        else:            
            from .StartPlayerView import StartPlayerView
            self.gEngine.successfulMatch(self.varGameTime, self.stateMatch)
            viewLogin = StartPlayerView(self.gEngine,"Player Start Menu")  

    #Mediante la siguiente función se declara el juego en estado de derrota. La función es llamada desde el botón "Declare Defeat" 
    def declareDefeat(self):      
        self.popUpDefeat = self.app.yesno("Defeat", "¿Desea abandonar la partida?")                
        self.stateTime = False 
        if self.popUpDefeat == True:                                                 
            self.popUpNewBoard = self.app.yesno("Nuevo Juego", "¿Deseas iniciar un nuevo juego con el mismo tablero inicial de esta partida?")
            if self.popUpNewBoard == True:
                self.stateMatch = 4                
                self.restartGame()                        
            else: 
                self.stateMatch = 4                
                self.app.destroy()                
                self.ReturnBack()
        else:
            self.stateTime = True
    
    #mediante la siguiente función se obtiene el ultimo moviento realizado.
    def lastMove(self, board):
        self.listMoves.append(self.board.get_all())
        return self.board.get_all()
        #print(self.listMoves) 
        
    #mediante la siguiente función se dibuja el tablero del paso anterior, esta es llamada desde el metodo stepRewind.        
    def fillRewind(self):
        self.listMoves.pop()
        for x in range(self.board_size):
            for y in range(self.board_size):                                
                self.board.set_pixel(x, y, self.listMoves[len(self.listMoves)-1][y][x])
    
    def fillInitBoard(self):
        for x in range(self.board_size):
            for y in range(self.board_size):                                
                self.board.set_pixel(x, y, self.listMoves[len(self.listMoves)-1][y][x])            
    
    #mediante la siguiente fución se reinicia el tablero al tablero inicial de la partida
    def restartGame(self): 
         
        self.gEngine.successfulMatch(self.varGameTime, self.stateMatch)
        self.app.destroy()
        self.gEngine.startMatch(1) 
        floodIt = FloodItView(self.gEngine, "Flood It") 
        firstMove = self.gEngine.getFirstMove() 
        for x in range(self.board_size):
            for y in range(self.board_size):                                
                self.board.set_pixel(x, y, firstMove[y][x])                                            
                           
          
          
        """self.listMoves.append(self.initialBoard)              
            self.listMoves = []
            self.moves_taken = 0
            self.moves.value = "" 
            self.stateTime = True     
            self.varGameTime = ""        
            self.second = 0
            self.minutes = 0
            self.hours = 0
            self.aux_hour =0 
            self.aux_min = 0
            self.aux_sec = 0"""
        
         
        
        
                  
    #mediante esta función se actualiza el estado de la partida a estado "en espera".    
    def matchOnHold(self):                          
        if self.stateMatch != 2:            
            self.app.when_closed = self.gEngine.updateStateMatch(self.stateMatch)                
        else: 
            #self.ReturnBack()                                                         
            self.app.when_closed = self.gEngine.updateStateMatch(self.stateMatch)            
                               
             

            
