from guizero import *
from .view import View
from .viewLogin import ViewLogin


class ScreenSplash(View):   
    def __init__(self, gEngine, title="view", width=840, height=620, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)
        self.gEngine = gEngine
        

        self.app.after(6000, self.openLogin, args="")
        p=Picture(self.app,image="Código/wait.gif")
        text=Text(self.app,text="Cargando...",size=28,height=5,font="Haettenschweiler",align="bottom")

    def openLogin(self):
        
        self.app.destroy()
        viewLogin = ViewLogin(self.gEngine,"algo")
        
        
        

