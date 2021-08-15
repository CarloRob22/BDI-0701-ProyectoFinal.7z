# -*- coding: utf-8 -*-
"""
    @author  fernando.murillo@unah.hn, mruizq@unah.hn, roberto.duran@unah.com
    @version 0.1.0
    @date 2021/08/10
"""

# --------------Imports----------------
from guizero import *
from .View import View
from .StartPlayerView import StartPlayerView
from .StartAdminView import StartAdminView
import json, re

class LoginView(View):   
    def __init__(self, gEngine, title="view", width=60, height=80, layout="auto", bg="gray92", visible=True):
        super().__init__(title, width, height, layout, bg, visible)
        self.gEngine = gEngine
        
        allBox = Box(self.app, layout="auto", width=self.pixel_width, height=self.pixel_height, border=1)
        allBox.tk.pack()
        allBox.tk.pack_propagate(0)

        #INICIO SECCION DEL TITULO        
        allBoxRow1 = Box(allBox, layout="auto")
        allBoxRow1.tk.pack()
        allBoxRow1.tk.pack_propagate(0)
        allBoxRow1.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*10)/100)
        allBoxRow1.bg = "dark slate blue"
        title = Text(allBoxRow1, text="Ingrese sus credenciales", size=18, color="white")
        title.tk.place(x=allBoxRow1.tk.winfo_reqwidth()/2, y=allBoxRow1.tk.winfo_reqheight()/2, anchor="center")
        #FINAL SECCION DEL TITULO

        #INICIO SECCION DEL FORMULARIO
        allBoxRow2 = Box(allBox, layout="auto")
        allBoxRow2.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*80)/100)
        allBoxRow2.tk.pack_propagate(0)

            #INICIO DEL FORMULARIO
        formBox = Box(allBoxRow2, layout="layout")
        formBox.resize((allBoxRow2.tk.winfo_reqwidth()*85)/100, (allBoxRow2.tk.winfo_reqheight()*70)/100)
        formBox.tk.place(x=allBoxRow2.tk.winfo_reqwidth()/2, y=allBoxRow2.tk.winfo_reqheight()/2, anchor="center")
        formBox.tk.pack_propagate(0)
        formBox.bg = "white"

                #INICIO SECCION DE INPUTS DEL FORMULARIO
        formBoxInputs = Box(formBox, layout="layout")
        formBoxInputs.resize(formBox.tk.winfo_reqwidth(), (formBox.tk.winfo_reqheight()*60)/100)
        formBoxInputs.tk.pack_propagate(0)

                    #INICIO SECCION DEL INPUT DE CORREO O NICKNAME
        formBoxInput1 = Box(formBoxInputs, layout="layout")
        formBoxInput1.resize(formBoxInputs.tk.winfo_reqwidth(), (formBoxInputs.tk.winfo_reqheight()*50)/100)
        formBoxInput1.tk.pack_propagate(0)

        formBoxInput1Col1 = Box(formBoxInput1, layout="layout", align="left")
        formBoxInput1Col1.resize((formBoxInput1.tk.winfo_reqwidth()*35)/100, formBoxInput1.tk.winfo_reqheight())
        formBoxInput1Col1.tk.pack_propagate(0)

        formLabelInput1 = Text(formBoxInput1Col1, text="Ingrese correo o nickname:", size=12, color="black")
        formLabelInput1.tk.place(x=formBoxInput1Col1.tk.winfo_reqwidth()/2, y=formBoxInput1Col1.tk.winfo_reqheight()/2, anchor="center")

        formBoxInput1Col2 = Box(formBoxInput1, layout="layout", align="left")
        formBoxInput1Col2.resize((formBoxInput1.tk.winfo_reqwidth()*65)/100, formBoxInput1.tk.winfo_reqheight())
        formBoxInput1Col2.tk.pack_propagate(0)

        self.formInput1 = TextBox(formBoxInput1Col2, width=47, height=2,  multiline=True)
        self.formInput1.tk.place(x=formBoxInput1Col2.tk.winfo_reqwidth()/2, y=formBoxInput1Col2.tk.winfo_reqheight()/2, anchor="center")

                    #FINAL SECCION DEL INPUT DE CORREO O NICKNAME

                    #INICIO SECCION DEL INPUT DE CONTRASENA
        formBoxInput2 = Box(formBoxInputs, layout="layout")
        formBoxInput2.resize(formBoxInputs.tk.winfo_reqwidth(), (formBoxInputs.tk.winfo_reqheight()*50)/100)
        formBoxInput2.tk.pack_propagate(0)

        formBoxInput2Col1 = Box(formBoxInput2, layout="layout", align="left")
        formBoxInput2Col1.resize((formBoxInput2.tk.winfo_reqwidth()*35)/100, formBoxInput2.tk.winfo_reqheight())
        formBoxInput2Col1.tk.pack_propagate(0)

        formLabelInput2 = Text(formBoxInput2Col1, text="Ingrese su clave de acceso:", size=12, color="black")
        formLabelInput2.tk.place(x=formBoxInput2Col1.tk.winfo_reqwidth()/2, y=formBoxInput2Col1.tk.winfo_reqheight()/2, anchor="center")

        formBoxInput2Col2 = Box(formBoxInput2, layout="layout", align="left")
        formBoxInput2Col2.resize((formBoxInput2.tk.winfo_reqwidth()*65)/100, formBoxInput2.tk.winfo_reqheight())
        formBoxInput2Col2.tk.pack_propagate(0)

        self.formInput2 = TextBox(formBoxInput2Col2, width=47, height=2,  multiline=True)
        self.formInput2.tk.place(x=formBoxInput2Col2.tk.winfo_reqwidth()/2, y=formBoxInput2Col2.tk.winfo_reqheight()/2, anchor="center")

                    #FINAL SECCION DEL INPUT DE CONTRASENA
                #FINAL SECCION DE INPUTS DEL FORMULARIO

                #INICIO SECCION DEL BOTON DEL FORMULARIO
        formBoxButton = Box(formBox, layout="layout")
        formBoxButton.resize(formBox.tk.winfo_reqwidth(), (formBox.tk.winfo_reqheight()*40)/100)
        formBoxButton.tk.pack_propagate(0)

        submitButton = PushButton(formBoxButton, text="Ingresar", width=30, height=4, command=self.openUser)
        submitButton.tk.place(x=formBoxButton.tk.winfo_reqwidth()/2, y=formBoxButton.tk.winfo_reqheight()/2, anchor="center")
        submitButton.tk.pack_propagate(0)
        submitButton.bg = "dark slate blue"
        submitButton.text_color = "white"

                #FINAL SECCION DEL BOTON DEL FORMULARIO
            #FINAL DEL FORMULARIO
        #FINAL SECCION DEL FORMULARIO
        
        #INICIO SECCION DE AUTORES
        allBoxRow3 = Box(allBox, layout="auto")
        allBoxRow3.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*10)/100)
        allBoxRow3.tk.pack_propagate(0)

        AutorsButton = PushButton(allBoxRow3, text="Creditos", width=20, height=1, command=self.open_window)
        AutorsButton.tk.place(x=allBoxRow3.tk.winfo_reqwidth()/2, y=allBoxRow3.tk.winfo_reqheight()/2, anchor="center")
        AutorsButton.tk.pack_propagate(0)
        AutorsButton.bg = "dark slate blue"
        AutorsButton.text_color = "white"
        #FINAL SECCION DE AUTORES             
        
        self.window = Window(self.app, title = "Autores", height=150, width=840)
        self.window.hide()
    
    #Mediante el siguiente método se muestra el formulario de autores del juego.
    def open_window(self):
        self.window.show()
        Text(self.window, text="")
        windowtext = Text(self.window, text="Agradecimientos a la pagina https://lawsie.github.io/guizero/")
        windowButton = PushButton(self.window, text="Close",command=self.close_window)

    #Mediante el siguiente método se cierra el formulario de autores del juego.
    def close_window(self):
        self.window.hide()

    #Mediante el siguiente método se hace el proceso de autenticación, se verfica la existencia del usuario en base de datos.    
    def openUser(self):
        user = self.gEngine.authUser(re.sub("\s+$", "", self.formInput1.value), re.sub("\s+$", "", self.formInput2.value) )
        if user is not None:            
            if user.role == 1:
                self.openPlayer()                
            else:
                self.openAdmin()
        else:
            print("Credenciales no validas")
        
    #Mediante el siguiente método se muestra la interfaz principal del usuario jugador.
    def openPlayer(self):
        self.app.destroy()
        viewLogin = StartPlayerView(self.gEngine,"Player Start Menu")

    #mediante el siguiente método se muestra la interfaz principal del usuario administrador.
    def openAdmin(self):
        self.app.destroy()
        viewLogin = StartAdminView(self.gEngine, "Admin Start Menu")
        
    