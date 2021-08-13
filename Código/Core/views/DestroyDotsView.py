from guizero import *
from .View import View
from random import randint
import time
import json

class DestroyDotsView(View):   
    def __init__(self, gEngine, returning, title="Destroy de dots", width=740, height=620, layout="auto", bg="white", visible=True):
        super().__init__(title,  width, height, layout, bg, visible)
        self.gEngine = gEngine
        self.returning = returning
        self.GRID_SIZE = 5
        self.score = 0
        self.startTim = {}
        self.second = 0
        self.minutes = 0
        self.hours = 0
        self.aux_hour =0 
        self.aux_min = 0
        self.aux_sec = 0
        self.stateTime = True
        self.varGameTime = ""
        self.stateMatch = 2 # se utiliza para llevar de manera globar el estado de la partida, su valor por defecto es necesario que sea 2.
        
        
        self.BoxWaff = Box(self.app, layout="auto", align="left")
        self.instructions = Text(self.BoxWaff, text="Click the dots to destroy them")
        self.board = Waffle(self.BoxWaff, width=self.GRID_SIZE, height=self.GRID_SIZE, command=self.destroy_dot, dim = 80)                
        self.board.after(1000, self.add_dot)
        self.score_display = Text(self.BoxWaff, text="Your score is " + str(self.score))
        
        self.BoxBotton = Box(self.app, layout="auto", align="left", border=True, width="fill", height="fill")
        self.BoxBottonL =Box(self.BoxBotton, align="left", width="fill", height="fill")
        self.pauseGame = PushButton(self.BoxBottonL, text="Pause", command=self.pause, width="fill", height="fill")                       
        self.Defeat = PushButton(self.BoxBottonL, text="Declare Defeat", command=self.declareDefeat, width="fill", height="fill")
        self.BoxBottonR =Box(self.BoxBotton, align="left", width="fill", height="fill")    
        self.timer = Text(self.BoxBottonR, text="")
        
        self.startTime()
        self.gameTime()
        self.app.display()
        self.matchOnHold()

    def add_dot(self):
        if self.stateTime == True:            
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
                self.stateMatch=5
                self.gEngine.successfulMatch(self.varGameTime, self.stateMatch)
                self.score_display.value = "You lost! Score: " + str(self.score)
                self.stateTime = False 
                self.board.disable()
                self.gEngine.setScore(self.score,2, self.varGameTime)
                popUpLoser = self.app.info("Finalizado", "finalizaste el juego con una puntuación de {}".format(str(self.score)))
                popUpLoser = True
                if popUpLoser == True:
                    self.stateTime = False 
                    self.app.destroy()
                    self.ReturnBack()
                    self.gEngine.successfulMatch(self.varGameTime, self.stateMatch)
            else:
                self.board.after(speed, self.add_dot)


    def destroy_dot(self,x,y):
        global score
        if self.board[x,y].dotty == True:
            self.board[x,y].dotty = False
            self.board.set_pixel(x, y, "white")
            self.score += 1
            self.score_display.value = "Your score is " + str(self.score)
        self.lastMove()
    
            
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
    def gameTime(self,): 
        if(self.stateTime):       
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
            self.board.visible = False   
            self.gEngine.updateStateMatch(3) 
            self.pauseGame.text = "Continue"    
            self.stateTime = False            
        else:
            self.board.visible = True
            self.gEngine.updateStateMatch(1)
            self.stateTime = True            
            self.pauseGame.text =  "Pause"
            self.gameTime()
            self.add_dot()

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
            self.stateMatch = 4                
            self.app.destroy()                
            self.ReturnBack()
        else:
            self.stateTime = True
            
                  
   
       
    #mediante la siguiente función se obtiene el ultimo moviento realizado.
    def lastMove(self):
        #print(self.board.get_all())
        return self.board.get_all()

    #mediante esta función se actualiza el estado de la partida a estado "en espera".    
    def matchOnHold(self):        
        if self.stateMatch != 2:            
            self.app.when_closed = self.gEngine.updateStateMatch(self.stateMatch)                
        else:
            #self.ReturnBack()                                                         
            self.app.when_closed = self.gEngine.updateStateMatch(self.stateMatch) 
          