from guizero import *
from .view import View
from .viewLogin import ViewLogin
import os

class ScreenSplash(View):   
    def __init__(self, gEngine, title="view", width=840, height=620, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)
        self.gEngine = gEngine
        
        path = os.getcwd()

        print(path)

        self.app.after(3000, self.openLogin, args="")

    def openLogin(self):
        
        self.app.destroy()
        viewLogin = ViewLogin(self.gEngine,"algo")
        
        
        

