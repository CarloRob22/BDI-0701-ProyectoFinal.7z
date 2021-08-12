# ------------------------------
# Imports
# ------------------------------

from guizero import *
import random
from .View import View
from .DestroyDotsView import DestroyDotsView
from .FloodItView import FloodItView
from .CrudView import CrudView

class StartAdminView(View):    
    def __init__(self, gEngine, title="view", width=700, height=700, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)        
        self.gEngine = gEngine
        self.returning = 1 
        
        #self.app = App("Interfaz de Administrador", height=300)
        self.Name_box = Box(self.app, width="fill", align="top", border=True, height=60)
        self.Name_box.bg = '#FFFFFF'
        self.userName = Text(self.Name_box, width="fill", height="fill", align="right", size=15, color='blue')

        self.Floodit_box = Box(self.app, width="fill", align="top", height=60)
        self.playFloodit = PushButton(self.Floodit_box, width="fill", height="fill", text='Jugar Flood It',command=self.startFloodit)
        self.playFloodit.bg = '#FBE3B8'

        self.Destroy_box = Box(self.app, width="fill", align="top", height=60)
        self.playDestroy = PushButton(self.Destroy_box, width="fill", height="fill", text='Jugar Destroy The Dots',command=self.startDestroy)
        self.playDestroy.bg = (79, 168, 187)

#----Ventana para emergente de la Gestion----

        self.Crud_box = Box(self.app, width="fill", align="top", height=60)
        self.crudUser = PushButton(self.Crud_box, width="fill", height="fill", text='Gestionar Usuarios',command=self.openCrud)
        self.crudUser.bg = '#22778B'

        self.Bin_box = Box(self.app, width="fill", align="top", height=60)
        self.viewBinnacle = PushButton(self.Bin_box, width="fill", height="fill", text='Visualizar Bitácora')
        self.viewBinnacle.bg = '#104B59'

        window_crud = Window(self.app,"Interfaz de Administrador",width=400, height=250, layout="grid")
        window_crud.hide() 

        boxW = Box(window_crud,layout="grid",grid=[0,0])
        lFirstName = Text(boxW, text="FirstName:", grid=[0,0],align="left")
        self.nickname = TextBox(boxW,width="fill", grid=[1,0],align="left")
        lLastName = Text(boxW, text="LastName:", grid=[0,1],align="left")
        self.nickname = TextBox(boxW,width="fill", grid=[1,1],align="left")
        lEmail = Text(boxW, text="Email:", grid=[0,2],align="left")
        self.nickname = TextBox(boxW,width="fill", grid=[1,2],align="left")
        lNickname = Text(boxW, text="NickName:", grid=[0,3],align="left")
        self.nickname = TextBox(boxW,width="fill", grid=[1,3],align="left")
        lPassword = Text(boxW, text="Password", grid=[0,4],align="left")
        self.nickname = TextBox(boxW,width="fill", grid=[1,4],align="left")
        lRole = Text(boxW, text="Role", grid=[0,5],align="left")
        self.nickname = TextBox(boxW,width="fill", grid=[1,5],align="left")
        
        boxIt = Box(window_crud, layout="grid",grid=[1,0])
        addButton = PushButton(boxIt,text="Add User",width=15,height=1,grid=[0,0],align="left", command= self.addUsers)
        addButton.bg="lime green"
        deleteButton = PushButton(boxIt,text="Delete User",width=15,height=1, grid=[0,1],align="left", command= self.deleteUsers)
        deleteButton.bg = "red"
        updateButton = PushButton(boxIt,text="Update User",width=15,height=1, grid=[0,2],align="left", command= self.updateUsers)
        updateButton.bg ="yellow"
        closeButton = PushButton(boxIt,text="Close",width=15,height=1, grid=[0,3],align="left")
        closeButton.bg ="DodgerBlue2"
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
        check = str(self.gEngine.checkStateMatch())        
        if check == "[(None,)]":
            self.gEngine.startMatch(1)               
            self.app.destroy()                 
            floodIt = FloodItView(self.gEngine,self.returning, None ,"Flood It")
        else:
            print("hay una partidada guardada")
            self.popUpHoldMacht = self.app.info("Partida en espera","Tienes una Partida en espera")
        
        
    #Mediante la siguiente función se inicia el juego Destroy The Dots cuando el usuario da click el el boton "Jugar Destroy The Dots".
    def startDestroy(self): 
        check = str(self.gEngine.checkStateMatch())        
        if check == "[(None,)]":
            self.gEngine.startMatch(2)
            self.app.destroy()            
            destroyDots = DestroyDotsView(self.gEngine,self.returning, None,"Destroy The Dots")
        else:
            self.popUpHoldMacht = self.app.info("Partida en espera","Tienes una Partida en espera")
        
            
    #Mediante la siguiente función el usuario inicia el módulo  de registro de bitácora al dar click en el boton "Visualizar Bitácora".
    def startBinnacle(self):
        pass
        #agregar aquí código para iniciar módulo de registro de bitácora.

    def openCrud(self):
        self.app.destroy() 
        crudView = CrudView(self.gEngine,"CRUD users")

