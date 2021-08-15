# -*- coding: utf-8 -*-
"""
    @author  mruizq@unah.hn, roberto.duran@unah.com
    @version 0.1.0
    @date 2021/08/05
"""

# --------------Imports----------------
from re import T
from guizero import *
from guizero import Picture
from .View import View
from .LoginView import LoginView


class ScreenSplashView(View):   
    def __init__(self, gEngine, title="view", width=40, height=60, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)
        self.gEngine = gEngine        

        #El método after de self.app recibe como parametro 3000 milisegundos, que es el timepo que se mostrará el
        self.app.after(3000, self.openLogin, args="")
        #p=Picture(self.app,image="Código/Core/Splash.png")
        text=Text(self.app,text="Cargando...",size=28,height=5,font="Haettenschweiler",align="bottom")

    def openLogin(self):        
        self.app.destroy()
        viewLogin = LoginView(self.gEngine,"Login")
        
        
        
        
        

