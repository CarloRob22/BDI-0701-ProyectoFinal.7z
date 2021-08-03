from guizero import *
from .View import View
from .LoginView import LoginView


class ScreenSplashView(View):   
    def __init__(self, gEngine, title="view", width=840, height=620, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)
        self.gEngine = gEngine
        

        self.app.after(1000, self.openLogin, args="")
        #p=Picture(self.app,image="Código/wait.gif")
        text=Text(self.app,text="Cargando...",size=28,height=5,font="Haettenschweiler",align="bottom")

    def openLogin(self):
        
        self.app.destroy()
        viewLogin = LoginView(self.gEngine,"algo")
        
        
        

