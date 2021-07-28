from guizero import *
from .view import View
from .viewLogin import ViewLogin

class ScreenSplash(View):   
    def __init__(self, title="view", width=840, height=620, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)

        self.app.after(3000, self.openLogin, args="")

    def openLogin(self):
        self.app.destroy()
        viewLogin = ViewLogin("algo")
        