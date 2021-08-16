# -*- coding: utf-8 -*-
"""
    @author   roberto.duran@unah.com, mruizq@unah.hn
    @version 0.1.0
    @date 2021/08/13
"""
#from time import process_time_ns
from guizero import *
from .View import View
from .DestroyDotsView import DestroyDotsView
from .FloodItView import FloodItView
from .ScoreView import ScoreView
import json


class StartPlayerView(View):
    def __init__(self, gEngine, title="view", width=50, height=80, layout="auto", bg="gray92", visible=True):
        super().__init__(title, width, height, layout, bg, visible)
        self.gEngine = gEngine
        self.returning = 0

        allBox = Box(self.app, layout="auto", width=self.pixel_width, height=self.pixel_height, border=1)
        allBox.tk.pack()
        allBox.tk.pack_propagate(0)
        
        #INICIO SECCION DE BOTONES DE INTERACCION
        allBoxRow1 = Box(allBox, layout="auto")
        allBoxRow1.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*85)/100)
        allBoxRow1.tk.pack_propagate(0)

        allBoxRow1Row1 = Box(allBoxRow1, layout="auto")
        allBoxRow1Row1.resize(allBoxRow1.tk.winfo_reqwidth(), (allBoxRow1.tk.winfo_reqheight()*25)/100)
        allBoxRow1Row1.tk.pack_propagate(0)

        FloodItButton = PushButton(allBoxRow1Row1, text="Iniciar juego Flood It", width=50, height=5, command=self.newFloodIt)
        FloodItButton.tk.place(x=allBoxRow1Row1.tk.winfo_reqwidth()/2, y=allBoxRow1Row1.tk.winfo_reqheight()/2, anchor="center")
        FloodItButton.tk.pack_propagate(0)
        FloodItButton.bg = '#FBE3B8'

        allBoxRow1Row2 = Box(allBoxRow1, layout="auto")
        allBoxRow1Row2.resize(allBoxRow1.tk.winfo_reqwidth(), (allBoxRow1.tk.winfo_reqheight()*25)/100)
        allBoxRow1Row2.tk.pack_propagate(0)

        DestroyDotsButton = PushButton(allBoxRow1Row2, text="Iniciar juego Destroy the Dots", width=50, height=5, command=self.newDestroyDots)
        DestroyDotsButton.tk.place(x=allBoxRow1Row2.tk.winfo_reqwidth()/2, y=allBoxRow1Row2.tk.winfo_reqheight()/2, anchor="center")
        DestroyDotsButton.tk.pack_propagate(0)
        DestroyDotsButton.bg = (79, 168, 187)

        allBoxRow1Row3 = Box(allBoxRow1, layout="auto")
        allBoxRow1Row3.resize(allBoxRow1.tk.winfo_reqwidth(), (allBoxRow1.tk.winfo_reqheight()*25)/100)
        allBoxRow1Row3.tk.pack_propagate(0)

        ResumeGameButton = PushButton(allBoxRow1Row3, text="Reanudar Partida", width=50, height=5, command=self.restartGameMatchHold)
        ResumeGameButton.tk.place(x=allBoxRow1Row3.tk.winfo_reqwidth()/2, y=allBoxRow1Row3.tk.winfo_reqheight()/2, anchor="center")
        ResumeGameButton.tk.pack_propagate(0)
        ResumeGameButton.bg = "RoyalBlue2"

        allBoxRow1Row4 = Box(allBoxRow1, layout="auto")
        allBoxRow1Row4.resize(allBoxRow1.tk.winfo_reqwidth(), (allBoxRow1.tk.winfo_reqheight()*25)/100)
        allBoxRow1Row4.tk.pack_propagate(0)

        ScoreButton = PushButton(allBoxRow1Row4, text="Mostrar tabla de puntuaciones", width=50, height=5, command=self.openScoreTable)
        ScoreButton.tk.place(x=allBoxRow1Row4.tk.winfo_reqwidth()/2, y=allBoxRow1Row4.tk.winfo_reqheight()/2, anchor="center")
        ScoreButton.tk.pack_propagate(0)
        ScoreButton.bg = "plum"

        #INICIO SECCION DE BOTON DE REGRESO
        allBoxRow2 = Box(allBox, layout="auto")
        allBoxRow2.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*15)/100)
        allBoxRow2.tk.pack_propagate(0)

        returnButton = PushButton(allBoxRow2, text="Salir", width=30, height=3, command=self.ReturnLogin)
        returnButton.tk.place(x=allBoxRow2.tk.winfo_reqwidth()/2, y=allBoxRow2.tk.winfo_reqheight()/2, anchor="center")
        returnButton.tk.pack_propagate(0)
        returnButton.bg = "indian red"
        
    def newFloodIt(self):            
        check = self.gEngine.checkStateMatch()        
        if check != None:            
            if check["gameStateId"] != 2:                        
                self.gEngine.startMatch(1)               
                self.app.destroy()                 
                floodIt = FloodItView(self.gEngine, self.returning, None,"Flood It")                
            else:
                print("hay una partidada guardada")
                self.popUpHoldMacht = self.app.info("Partida en espera","Tienes una Partida en espera")      
        else:
            self.gEngine.startMatch(1)               
            self.app.destroy()                 
            floodIt = FloodItView(self.gEngine, self.returning, None,"Flood It")
            
        
    def newDestroyDots(self):
        check = self.gEngine.checkStateMatch()        
        if check != None:            
            if check["gameStateId"] != 2:                        
                self.gEngine.startMatch(2)
                self.app.destroy()            
                destroyDots = DestroyDotsView(self.gEngine, self.returning,"Destroy The Dots")               
            else:
                print("hay una partidada guardada")
                self.popUpHoldMacht = self.app.info("Partida en espera","Tienes una Partida en espera")      
        else:
            self.gEngine.startMatch(2)               
            self.app.destroy()                 
            destroyDots = DestroyDotsView(self.gEngine, self.returning, "Destroy The Dots")
        
       
           
    def openScoreTable(self):
        self.app.destroy()            
        destroyDots = ScoreView(self.gEngine,"Personal Score Table")
        
    def restartGameMatchHold(self):         
        check = self.gEngine.checkStateMatch()        
        if check != None: 
            if check["gameStateId"] == 2:      
                dataMatch = self.gEngine.restartGameMatchHold()                  
                lastTime = str(dataMatch[0])
                movesMatch = dataMatch[1]
                idGame = dataMatch[2]   
                self.app.destroy()  
                if idGame == 1:               
                    floodIt = FloodItView(self.gEngine, self.returning, None, True,lastTime,movesMatch,"Flood It")               
                elif idGame == 2:
                    destroyDots = DestroyDotsView(self.gEngine, self.returning, True,lastTime, movesMatch,  "Destroy The Dots")
        else:
            print("no hay una partidada guardada")
            self.popUpHoldMacht = self.app.info("No hay partida en espera","No tienes una Partida en espera")                
            self.popUpHoldMacht = True
            
    def ReturnLogin(self):
        from .LoginView import LoginView
        self.app.destroy()
        viewLogin = LoginView(self.gEngine, "Inicio de sesion")



    