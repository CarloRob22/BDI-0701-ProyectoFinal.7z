# ------------------------------
# Imports
# ------------------------------

from guizero import *
import random
from .viewDestroyDots import ViewDestroyDots
from .viewFloodIt import ViewFloodIt

class StartAdminView:    
    def __init__(self):        
        self.window = App("Interfaz de Administrador", height=300)
        self.Name_box = Box(self.window, width="fill", align="top", border=True, height=60)
        self.Name_box.bg = '#FFFFFF'
        self.userName = Text(self.Name_box, width="fill", height="fill", align="right", size=15, color='blue')

        self.Floodit_box = Box(self.window, width="fill", align="top", height=60)
        self.playFloodit = PushButton(self.Floodit_box, width="fill", height="fill", text='Jugar Flood It',command=self.startFloodit)
        self.playFloodit.bg = '#FBE3B8'

        self.Destroy_box = Box(self.window, width="fill", align="top", height=60)
        self.playDestroy = PushButton(self.Destroy_box, width="fill", height="fill", text='Jugar Destroy The Dots',command=self.startDestroy)
        self.playDestroy.bg = (79, 168, 187)

        self.Crud_box = Box(self.window, width="fill", align="top", height=60)
        self.crudUser = PushButton(self.Crud_box, width="fill", height="fill", text='Gestionar Usuarios',command=self.start)
        self.crudUser.bg = '#22778B'

        self.Bin_box = Box(self.window, width="fill", align="top", height=60)
        self.viewBinnacle = PushButton(self.Bin_box, width="fill", height="fill", text='Visualizar Bitácora')
        self.viewBinnacle.bg = '#104B59'



        #Mediante esta función se muestra la ventana principal de acciones del administrador.
    def start(self):
        pass

    def getName(self, name):
        #self.userName.clear()
        self.userName.append(str(name))
            
    #Mediante la siguiente función se inicia el juego Floodit cuando el usuario da click en el boton "Jugar Flood It".
    def startFloodit(self):
        self.window.destroy()
        flood = ViewFloodIt()
            
        #Mediante la siguiente función se inicia el juego Destroy The Dots cuando el usuario da click el el boton "Jugar Destroy The Dots".
    def startDestroy(self):
        self.window.destroy()
        destroyDots = ViewDestroyDots()
            
    #Mediante la siguiente función el usuario inicia el módulo de gestión de la información de los usuarios al dar click en el boton "Gestionar Usuarios".
    #crear, eliminar y editar los datos de autenticación de usuarios (jugadores).
    def startCrud(self):
        pass
        #agregar aquí código para iniciar módulo de gestión de usuarios.
            
    #Mediante la siguiente función el usuario inicia el módulo  de registro de bitácora al dar click en el boton "Visualizar Bitácora".
    def startBinnacle(self):
        pass
        #agregar aquí código para iniciar módulo de registro de bitácora.
        
