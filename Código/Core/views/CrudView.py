# ------------------------------
# Imports
# ------------------------------

from guizero import *
import random
from .View import View
from .DestroyDotsView import DestroyDotsView
from .FloodItView import FloodItView

class CrudView(View):    
    def __init__(self, gEngine, title="view", width=1400, height=750, layout="grid", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)        
        self.gEngine = gEngine
        self.returning = 1 

        
        insertText = Text(self.app, text="Inserte un nuevo jugador", size=18, height=3, width=55, align="left", grid=[0,0])
        #insertText.bg = "blue"

        insertText = Text(self.app, text="Borrar Jugador", size=18, height=3, width=55, align="left", grid=[1,0])
        #insertText.bg = "blue"

        Listbox = ListBox(self.app, items=["Beef", "Chicken", "Fish", "Vegetarian"],height=400, width=500, align="center", grid=[1,1,1,10])

        DeleteBotton = PushButton(self.app, text="Eliminar", height=2, width=35,  grid=[1,11])
        DeleteBotton.bg = "firebrick"

        UpdateBotton = PushButton(self.app, text="Actualizar", height=2, width=35,  grid=[1,12])
        UpdateBotton.bg = "tan1"

        FirstNText = Text(self.app, text="Nombre", height=2, width=40, align="left", grid=[0,1])
        #FirstNText.bg = "yellow"

        FirstNInput = TextBox(self.app, height=3, width=55 ,multiline=True, grid=[0,2])
        #FirstNInput.bg = "green"

        LastNText = Text(self.app, text="Apellido", height=2, width=40, align="left", grid=[0,3])
        #LastNText.bg = "yellow"

        LastNInput = TextBox(self.app, height=3, width=55 ,multiline=True, grid=[0,4])
        #LastNInput.bg = "green"

        EmailText = Text(self.app, text="Correo", height=2, width=40, align="left", grid=[0,5])
        #EmailText.bg = "yellow"

        EmailInput = TextBox(self.app, height=3, width=55 ,multiline=True, grid=[0,6])
        #EmailInput.bg = "green"

        NicknameText = Text(self.app, text="Apodo", height=2, width=40, align="left", grid=[0,7])
        #NicknameText.bg = "yellow"

        NicknameInput = TextBox(self.app, height=3, width=55 ,multiline=True, grid=[0,8])
        #NicknameInput.bg = "green"

        PasswordText = Text(self.app, text="Contrasena", height=2, width=43, align="left", grid=[0,9])
        #PasswordText.bg = "yellow"

        PasswordInput = TextBox(self.app, height=3, width=55 ,multiline=True, grid=[0,10])
        #PasswordInput.bg = "green"

        #SubmitText = Text(self.app, height=1, width=25, align="left", grid=[0,11])
        #SubmitText.bg = "yellow"

        SubmitBotton = PushButton(self.app, text="Agregar", height=2, width=30, grid=[0,12])
        SubmitBotton.bg = "green"








        

        
 
