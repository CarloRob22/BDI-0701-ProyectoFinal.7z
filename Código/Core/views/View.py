# -*- coding: utf-8 -*-
"""
    @author   roberto.duran@unah.com, mruizq@unah.hn
    @version 0.1.0
    @date 2021/08/13
"""
from guizero import *

class View:
    def __init__(self, title="view", width=50, height=50, layout="auto", bg="light grey", visible=False):
        self.title = title
        self.width = width
        self.height = height
        self.layout = layout
        self.bg = bg
        self.visible = visible
        self.app = App(title=self.title, width=self.width, height=self.height, layout=self.layout, bg=self.bg, visible=self.visible)
        self.app.hide()
        self.screen_width = self.app.tk.winfo_screenwidth()
        self.screen_height = self.app.tk.winfo_screenheight()
        self.pixel_width = (self.screen_width*self.width)/100
        self.pixel_height = (self.screen_height*self.height)/100
        self.show_center() 
        

    def show_center(self):
        x = (self.screen_width/2) - (self.pixel_width/2)
        y = (self.screen_height/2) - (self.pixel_height/2)
        self.app.tk.geometry('%dx%d+%d+%d' % (self.pixel_width, self.pixel_height, x, y))
        self.app.show()
    
