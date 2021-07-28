from guizero import *
from .view import View
from .viewStartMenu import ViewStartMenu
from .admin_interface import AdminInterface

class ViewLogin(View):   
    def __init__(self, title="view", width=840, height=620, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)

 
        titleBox = Box(self.app)
        titleBox.resize(self.width, (15*self.height)/100)
        title = Text(titleBox, text="Bienvenido", height=150, size=15)

        buttonsBox = Box(self.app)
        buttonsBox.resize(self.width, (2*self.height)/100)

        nickname = Text(self.app, text="Nickname") 
        nickname = TextBox(self.app, text="******")
        password = Text(self.app, text="Password") 
        password = TextBox(self.app, text="******")

        submitBox = Box(self.app)
        submitBox.resize(self.width, (15*self.height)/100)

        submitButton = PushButton(submitBox, text="Submit", command=self.openPlayer)

#------------
        def open_window():
            window.info(title="Agradecimientos A: ", text="https://lawsie.github.io/guizero/")


        authorBox = Box(self.app)
        authorBox.resize(self.width, (7*self.height)/100)

        window = Window(self.app, title = "Autores", height=250, width=250)
        window.hide()
    
        autorPop = Window(self.app)
        autorPop.hide()
        authorButton = PushButton(authorBox, text="Author's",command=open_window)

    def openPlayer(self):
        self.app.destroy()
        viewLogin = ViewStartMenu("algo")

    def openAdmin(self):
        self.app.destroy()
        viewLogin = AdminInterface()

    def verifyRole():
        pass