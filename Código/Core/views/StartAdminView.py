# ------------------------------
# Imports
# ------------------------------

from guizero import *
import random
from .View import View
from .DestroyDotsView import DestroyDotsView
from .FloodItView import FloodItView
from .CrudView import CrudView
from .ScoreView import ScoreView
from .JournalView import JournalView

class StartAdminView(View):    
    def __init__(self, gEngine, title="view", width=40, height=70, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)        
        self.gEngine = gEngine
        self.returning = 1 
        
        allBox = Box(self.app, layout="auto", width=self.pixel_width, height=self.pixel_height, border=1)
        allBox.tk.pack()
        allBox.tk.pack_propagate(0)
        
        #INICIO SECCION DE BOTONES DE INTERACCION
        allBoxRow1 = Box(allBox, layout="auto")
        allBoxRow1.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*85)/100)
        allBoxRow1.tk.pack_propagate(0)

        allBoxRow1Row1 = Box(allBoxRow1, layout="auto")
        allBoxRow1Row1.resize(allBoxRow1.tk.winfo_reqwidth(), (allBoxRow1.tk.winfo_reqheight()*16.666666667)/100)
        allBoxRow1Row1.tk.pack_propagate(0)

        FloodItButton = PushButton(allBoxRow1Row1, text="Iniciar juego Flood It", width=60, height=3, command=self.startFloodit)
        FloodItButton.tk.place(x=allBoxRow1Row1.tk.winfo_reqwidth()/2, y=allBoxRow1Row1.tk.winfo_reqheight()/2, anchor="center")
        FloodItButton.tk.pack_propagate(0)
        FloodItButton.bg = "#FBE3B8"

        allBoxRow1Row2 = Box(allBoxRow1, layout="auto")
        allBoxRow1Row2.resize(allBoxRow1.tk.winfo_reqwidth(), (allBoxRow1.tk.winfo_reqheight()*16.666666667)/100)
        allBoxRow1Row2.tk.pack_propagate(0)

        DestroyDotsButton = PushButton(allBoxRow1Row2, text="Iniciar juego Destroy the Dots", width=60, height=3, command=self.startDestroy)
        DestroyDotsButton.tk.place(x=allBoxRow1Row2.tk.winfo_reqwidth()/2, y=allBoxRow1Row2.tk.winfo_reqheight()/2, anchor="center")
        DestroyDotsButton.tk.pack_propagate(0)
        DestroyDotsButton.bg = (79, 168, 187)

        allBoxRow1Row3 = Box(allBoxRow1, layout="auto")
        allBoxRow1Row3.resize(allBoxRow1.tk.winfo_reqwidth(), (allBoxRow1.tk.winfo_reqheight()*16.666666667)/100)
        allBoxRow1Row3.tk.pack_propagate(0)

        ResumeGameButton = PushButton(allBoxRow1Row3, text="Reanudar Partida", width=60, height=3, command=self.restartGameMatchHold)
        ResumeGameButton.tk.place(x=allBoxRow1Row3.tk.winfo_reqwidth()/2, y=allBoxRow1Row3.tk.winfo_reqheight()/2, anchor="center")
        ResumeGameButton.tk.pack_propagate(0)
        ResumeGameButton.bg = "RoyalBlue2"

        allBoxRow1Row4 = Box(allBoxRow1, layout="auto")
        allBoxRow1Row4.resize(allBoxRow1.tk.winfo_reqwidth(), (allBoxRow1.tk.winfo_reqheight()*16.666666667)/100)
        allBoxRow1Row4.tk.pack_propagate(0)

        ScoreButton = PushButton(allBoxRow1Row4, text="Mostrar tabla de puntuaciones", width=60, height=3, command=self.openScoreTable)
        ScoreButton.tk.place(x=allBoxRow1Row4.tk.winfo_reqwidth()/2, y=allBoxRow1Row4.tk.winfo_reqheight()/2, anchor="center")
        ScoreButton.tk.pack_propagate(0)
        ScoreButton.bg = "plum"

        allBoxRow1Row5 = Box(allBoxRow1, layout="auto")
        allBoxRow1Row5.resize(allBoxRow1.tk.winfo_reqwidth(), (allBoxRow1.tk.winfo_reqheight()*16.666666667)/100)
        allBoxRow1Row5.tk.pack_propagate(0)

        CrudButton = PushButton(allBoxRow1Row5, text="Gestionar Usuarios", width=60, height=3, command=self.openCrud)
        CrudButton.tk.place(x=allBoxRow1Row5.tk.winfo_reqwidth()/2, y=allBoxRow1Row5.tk.winfo_reqheight()/2, anchor="center")
        CrudButton.tk.pack_propagate(0)
        CrudButton.bg = '#22778B'

        allBoxRow1Row6 = Box(allBoxRow1, layout="auto")
        allBoxRow1Row6.resize(allBoxRow1.tk.winfo_reqwidth(), (allBoxRow1.tk.winfo_reqheight()*16.666666667)/100)
        allBoxRow1Row6.tk.pack_propagate(0)

        JournalButton = PushButton(allBoxRow1Row6, text="Mostrar bitacora", width=60, height=3, command=self.startJournal)
        JournalButton.tk.place(x=allBoxRow1Row6.tk.winfo_reqwidth()/2, y=allBoxRow1Row6.tk.winfo_reqheight()/2, anchor="center")
        JournalButton.tk.pack_propagate(0)
        JournalButton.bg = '#104B59'

        #INICIO SECCION DE BOTON DE REGRESO
        allBoxRow2 = Box(allBox, layout="auto")
        allBoxRow2.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*15)/100)
        allBoxRow2.tk.pack_propagate(0)

        returnButton = PushButton(allBoxRow2, text="Salir", width=30, height=3, command=self.ReturnLogin)
        returnButton.tk.place(x=allBoxRow2.tk.winfo_reqwidth()/2, y=allBoxRow2.tk.winfo_reqheight()/2, anchor="center")
        returnButton.tk.pack_propagate(0)
        returnButton.bg = "indian red"
#---------------------

#Mediante esta función se muestra la ventana principal de acciones del administrador.
    def addUsers(self):
        self.gEngine.getAllDataUser()

    def deleteUsers(self):
        pass

    def updateUsers(self):
        pass

    def getName(self, name):
        #self.userName.clear()
        self.userName.append(str(name))
            
    #Mediante la siguiente función se inicia el juego Floodit cuando el usuario da click en el boton "Jugar Flood It".
    def startFloodit(self): 
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
        
        
    #Mediante la siguiente función se inicia el juego Destroy The Dots cuando el usuario da click el el boton "Jugar Destroy The Dots".
    def startDestroy(self): 
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
        
            
    #Mediante la siguiente función el usuario inicia el módulo  de registro de bitácora al dar click en el boton "Visualizar Bitácora".
    def startJournal(self):
        self.app.destroy()            
        destroyDots = JournalView(self.gEngine,"Registro de bitacora")

    def openCrud(self):
        self.app.destroy() 
        crudView = CrudView(self.gEngine,"CRUD users")


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
            
    def openScoreTable(self):
        self.app.destroy()            
        destroyDots = ScoreView(self.gEngine,"Personal Score Table")

    def ReturnLogin(self):
        from .LoginView import LoginView
        self.app.destroy()
        viewLogin = LoginView(self.gEngine, "Inicio de sesion")