from guizero import *
from .view import View
from .viewStartMenu import ViewStartMenu
from .admin_interface import AdminInterface
import json

class ViewLogin(View):   
    def __init__(self, gEngine, title="view", width=840, height=620, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)
        self.gEngine = gEngine


        titleBox = Box(self.app)
        titleBox.resize(self.width, (15*self.height)/100)
        title = Text(titleBox, text="Bienvenido", height=150, size=15)

        buttonsBox = Box(self.app)
        buttonsBox.resize(self.width, (2*self.height)/100)

        self.Lnickname = Text(self.app, text="Nickname") 
        self.nickname = TextBox(self.app)
        self.Lpassword = Text(self.app, text="Password") 
        self.password = TextBox(self.app)

        submitBox = Box(self.app)
        submitBox.resize(self.width, (15*self.height)/100)

        submitButton = PushButton(submitBox, text="Submit", command=self.openUser)

#------------
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
        usuario = self.nickname.value
        contra = self.password.value
        user = self.gEngine.auth(usuario, contra)
        if user is not None:            
            user = json.loads(user)        
            self.gEngine.addUser(user["id"],user["firstName"],user["lastName"],user["email"],user["nickname"],user["tin_role"])
            self.gEngine.sessionInJournal()
            if user["tin_role"] == 1:
                self.openPlayer()                
            else:
                self.openAdmin()
        else:
            print("Credenciales no validas")
        

    def openPlayer(self):
        self.app.destroy()
        viewLogin = ViewStartMenu("algo")

    def openAdmin(self):
        self.app.destroy()
        viewLogin = AdminInterface()

    def verifyRole():
        pass
    
    