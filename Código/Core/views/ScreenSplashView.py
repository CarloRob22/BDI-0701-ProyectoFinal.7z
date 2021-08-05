from guizero import *
from guizero import Picture
from .View import View
from .LoginView import LoginView


class ScreenSplashView(View):   
    def __init__(self, gEngine, title="view", width=840, height=620, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)
        self.gEngine = gEngine
        

        self.app.after(4000, self.openLogin, args="")
        #p=Picture(self.app,image="Código/Core/Splash.png")
        #text=Text(self.app,text="Cargando...",size=28,height=5,font="Haettenschweiler",align="bottom")

    def openLogin(self):
        
        self.app.destroy()
        viewLogin = LoginView(self.gEngine,"algo")
        
        
        

