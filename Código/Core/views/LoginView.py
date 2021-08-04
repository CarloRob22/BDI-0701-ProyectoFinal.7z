from guizero import *
from .View import View
from .StartPlayerView import StartPlayerView
from .StartAdminView import StartAdminView
import json

class LoginView(View):   
    def __init__(self, gEngine, title="view", width=840, height=620, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)
        self.gEngine = gEngine


        titleBox = Box(self.app)
        titleBox.resize(self.width, (15*self.height)/100)
        title = Text(titleBox, text="Bienvenido", height=150, size=15)

        buttonsBox = Box(self.app)
        buttonsBox.resize(self.width, (2*self.height)/100)

        self.Lnickname = Text(self.app, text="Nickname") 
        self.nickname = TextBox(self.app,width=15)
        self.Lpassword = Text(self.app, text="Password") 
        self.password = TextBox(self.app,width=15,hide_text=True)

        submitBox = Box(self.app)
        submitBox.resize(self.width, (15*self.height)/100)

        submitButton = PushButton(submitBox, text="Submit", command=self.openUser)

#------------Authores
        def open_window():
            window.show()
            windowtext = Text(window, text="Agradecimientos a la pagina https://lawsie.github.io/guizero/")
            windowButton = PushButton(window, text="Close",command=close_window)

        def close_window():
            window.hide()

        authorBox = Box(self.app)
        authorBox.resize(self.width, (7*self.height)/100)

        window = Window(self.app, title = "Autores", height=150, width=840)
        window.hide()
    
        autorPop = Window(self.app)
        autorPop.hide()
        authorButton = PushButton(authorBox, text="Author's",command=open_window)


    
    def openUser(self):
        user = self.gEngine.authUser(self.nickname.value, self.password.value)
        if user is not None:            
            if user.role == 1:
                self.openPlayer()                
            else:
                self.openAdmin()
        else:
            print("Credenciales no validas")
        

    def openPlayer(self):
        self.app.destroy()
        viewLogin = StartPlayerView(self.gEngine,"Player Start Menu")

    def openAdmin(self):
        self.app.destroy()
        viewLogin = StartAdminView()

    def verifyRole():
        pass
    
    