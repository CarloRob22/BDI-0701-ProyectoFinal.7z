from guizero import *
from .View import View
from random import randint
import time
import json
import re

class DestroyDotsView(View):   
    def __init__(self, gEngine, returning, restart = None, lastTime="", lastMoves=[], title="Destroy de dots", width=45, height=85, layout="auto", bg="white", visible=True):
        super().__init__(title,  width, height, layout, bg, visible)
        self.gEngine = gEngine
        self.returning = returning
        self.restart = restart 
        self.GRID_SIZE = 5
        self.score = 0        
        self.second = 0
        self.minutes = 0
        self.hours = 0
        self.aux_hour =0 
        self.aux_min = 0
        self.aux_sec = 0
        self.stateTime = True
        self.varGameTime = lastTime
        self.listMoves = lastMoves
        self.stateMatch = 2 # se utiliza para llevar de manera globar el estado de la partida, su valor por defecto es necesario que sea 2.        
        
        allBox = Box(self.app, layout="auto", width=self.pixel_width, height=self.pixel_height, border=1)
        allBox.tk.pack()
        allBox.tk.pack_propagate(0)

        #INICIO SECCION DEL TITULO        
        allBoxRow1 = Box(allBox, layout="auto")
        allBoxRow1.tk.pack()
        allBoxRow1.tk.pack_propagate(0)
        allBoxRow1.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*10)/100)
        allBoxRow1.bg = "IndianRed4"
        title = Text(allBoxRow1, text="Destroy The Dots", size=18, color="white")
        title.tk.place(x=allBoxRow1.tk.winfo_reqwidth()/2, y=allBoxRow1.tk.winfo_reqheight()/2, anchor="center")
        #FINAL SECCION DEL TITULO

        allBoxRow2 = Box(allBox, layout="auto")
        allBoxRow2.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*20)/100)
        allBoxRow2.tk.pack_propagate(0)

        allBoxRow2Col1 = Box(allBoxRow2, layout="auto", align="left")
        allBoxRow2Col1.resize((allBoxRow2.tk.winfo_reqwidth()*33.333333333)/100, allBoxRow2.tk.winfo_reqheight())
        allBoxRow2Col1.tk.pack_propagate(0)

        self.pauseGame = PushButton(allBoxRow2Col1, text="Pausa", command=self.pause, width="fill", height="fill")

        allBoxRow2Col2 = Box(allBoxRow2, layout="auto", align="left")
        allBoxRow2Col2.resize((allBoxRow2.tk.winfo_reqwidth()*33.333333333)/100, allBoxRow2.tk.winfo_reqheight())
        allBoxRow2Col2.tk.pack_propagate(0)

        self.Defeat = PushButton(allBoxRow2Col2, text="Declarar derrota", command=self.declareDefeat, width="fill", height="fill")

        allBoxRow2Col3 = Box(allBoxRow2, layout="auto", align="left")
        allBoxRow2Col3.resize((allBoxRow2.tk.winfo_reqwidth()*33.333333333)/100, allBoxRow2.tk.winfo_reqheight())
        allBoxRow2Col3.tk.pack_propagate(0)
        allBoxRow2Col3.bg = "IndianRed4"

        self.timer = Text(allBoxRow2Col3, text="", size=14, color="white")
        self.timer.tk.place(x=allBoxRow2Col3.tk.winfo_reqwidth()/2, y=allBoxRow2Col3.tk.winfo_reqheight()/2, anchor="center")

        allBoxRow4 = Box(allBox, layout="auto")
        allBoxRow4.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*10)/100)
        allBoxRow4.tk.pack_propagate(0)

        self.instructions = Text(allBoxRow4, text="Presione los puntos para destruirlos", size=14)
        self.instructions.tk.place(x=allBoxRow4.tk.winfo_reqwidth()/2, y=allBoxRow4.tk.winfo_reqheight()/2, anchor="center")

        self.allBoxRow5 = Box(allBox, layout="auto")
        self.allBoxRow5.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*50)/100)
        self.allBoxRow5.tk.pack_propagate(0)

        self.board = Waffle(self.allBoxRow5, width=self.GRID_SIZE, height=self.GRID_SIZE, command=self.destroy_dot, dim = 80)              
        self.board.after(1000, self.add_dot)

        allBoxRow6 = Box(allBox, layout="auto")
        allBoxRow6.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*10)/100)
        allBoxRow6.tk.pack_propagate(0)

        self.score_display = Text(allBoxRow6, text="Has realizado {} movimientos".format(self.score))
        self.score_display.tk.place(x=allBoxRow6.tk.winfo_reqwidth()/2, y=allBoxRow6.tk.winfo_reqheight()/2, anchor="center")
        
        self.validateRestart()
        self.fillRestartboard()       
        self.gameTime()
        self.app.display()
        self.stateTime = True
        self.matchOnHold()
        
    """El siguiente método selecciona aleatoriamente un pixel del objeto waffle y aplica propiedad dotty a cada pixel,
    asigna color rojo a pixel y ademas valida cuando todos los pixeles del tablero(waffle) tiene estas asignaciones."""
    def add_dot(self):
        if self.stateTime == True:            
            x, y = randint(0,self.GRID_SIZE-1), randint(0,self.GRID_SIZE-1)

            while self.board[x, y].dotty == True:
                x, y = randint(0,self.GRID_SIZE-1), randint(0,self.GRID_SIZE-1)
            self.stateTime = True
            self.board[x, y].dotty = True
            self.board.set_pixel(x, y, "IndianRed4")

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
                    if self.board[x,y].color != "IndianRed4":
                        all_red = False
            if all_red:
                self.stateMatch=5
                self.gEngine.updateStateMatch(self.varGameTime, self.stateMatch)
                self.score_display.value = "Perdistes! Movimientos: " + str(self.score)
                self.stateTime = False 
                self.board.disable()
                self.gEngine.setScore(self.score,2, self.varGameTime)
                popUpLoser = self.app.info("Finalizado", "finalizaste el juego con una puntuación de {}".format(str(self.score)))
                popUpLoser = True
                if popUpLoser == True:
                    self.stateTime = False 
                    self.app.destroy()
                    self.ReturnBackScore()                    
            else:
                self.board.after(speed, self.add_dot)

    #Mediante el siguiente método se obtiene las coordenadas del pixel seleccionado para colorear en blanco y eliminar propiedad dotty.
    def destroy_dot(self,x,y):
        global score
        if self.board[x,y].dotty == True:
            self.board[x,y].dotty = False
            self.board.set_pixel(x, y, "white")
            self.score += 1
            self.score_display.value = "Has realizado {} movimientos".format(self.score)
        self.lastMove()
        self.addMoveMatch()
    
    
    """Mediante el siguiente método se inicia el tiempo del juego desde(00:00:00) y lo actualiza, 
       siempre y cuando la variable self.stateTime sea igual a True."""
    def gameTime(self): 
        if self.restart == True:                  
            self.aux_hour = int(re.split(':',self.varGameTime)[0])                
            self.aux_min = int(re.split(':',self.varGameTime)[1])                
            self.secondAux = re.split(':',self.varGameTime)[2]
            self.second = int(re.split('\.',self.secondAux)[0])               
            self.restart = False               
                
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
               
               
    """Mediante el siguiente método se pausa el tiempo del juego. La función es llamada desde el botón "pause.
       Este evento es controlado mediante la variable global de tipo boleana self.stateTime"""
    def pause(self):
        if self.stateTime:  
            self.board.hide()  
            self.gEngine.updateStateMatch(self.varGameTime,3)
            self.pauseGame.text = "Continue"    
            self.stateTime = False            
        else:
            self.board.show() 
            self.gEngine.updateStateMatch(self.varGameTime,1)
            self.stateTime = True                        
            self.pauseGame.text =  "Pause"
            self.gameTime()
            self.add_dot()
            
            
    """Mediante el siguiente método se regresa a la interfaz inicial de usuario cuando termina exitosamente o declara 
       como derrota un juego"""
    def ReturnBack(self):
        if self.returning==1:            
            from .StartAdminView import StartAdminView            
            viewLogin = StartAdminView(self.gEngine, "Admin Start Menu")
        else:            
            from .StartPlayerView import StartPlayerView            
            viewLogin = StartPlayerView(self.gEngine,"Player Start Menu")
    
    #Mediante el siguiente método se declara el juego en estado de derrota. La función es llamada desde el botón "Declare Defeat".
    def declareDefeat(self):          
        self.popUpDefeat = self.app.yesno("Defeat", "¿Desea abandonar la partida?") 
        self.stateTime = False                                                            
        if self.popUpDefeat == True:                                                                                                    
            self.stateMatch = 4 
            self.gEngine.updateStateMatch(self.varGameTime, self.stateMatch)                 
            self.app.destroy()                
            self.ReturnBack()
        else:
            self.stateTime = True
       
    #Mediante el siguiente método se obtiene el ultimo moviento realizado.
    def lastMove(self):        
        return self.board.get_all()

    #Mediante este método se actualiza el estado de la partida a estado "en espera".    
    def matchOnHold(self):           
            self.score += 1
            self.addMoveMatch()
            if self.stateMatch == 2:
                self.app.when_closed = self.gEngine.updateStateMatch(self.varGameTime,self.stateMatch)
    
    #Mediante este método se agrega un nuevo movimiento de la partida en base de datos.
    def addMoveMatch(self):
        move = {
            "no": int(self.score),
            "move": self.board.get_all()
        }     
        rmove=json.dumps(move)   
        self.gEngine.addMovementMatch(self.varGameTime ,rmove)  
        
    #El siguiente método valida si la partida actual es nueva ó es una partida reanudada.
    def validateRestart(self):       
        if self.restart == True:  
            self.score = len(self.listMoves)
            self.score_display.value = str(self.score)       
            self.Defeat.enabled = True
         
    """El siguiente método se utiliza en caso de reanudar, mediante el se dibuja el ultimo tablero
       mostrado en la partida antes de que fuese guardada."""
    def fillRestartboard(self):
        if self.restart == True: 
            lastmove = self.listMoves[len(self.listMoves)-1]
            for x in range(self.GRID_SIZE):
                for y in range(self.GRID_SIZE):
                    if lastmove[y][x] == "IndianRed4":
                        self.board.set_pixel(x, y, "IndianRed4")
                        self.board[x, y].dotty = True
                        
    #Metidante este método se envia al jugador a la interfaz de tablero personal de puntuaciones.
    def ReturnBackScore(self):
        from .ScoreView import ScoreView                              
        destroyDots = ScoreView(self.gEngine,"Tablero de puntajes personal")        
     