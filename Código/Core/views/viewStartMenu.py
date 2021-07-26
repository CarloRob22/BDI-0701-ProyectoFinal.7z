from guizero import Box, Text, PushButton
from .view import View

class ViewStartMenu(View):
    def __init__(self, title="view", width=700, height=700, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)

        
        #Estilos para el titulo de la ventana
        titleBox = Box(self.app)
        titleBox.resize(self.width, (15*self.height)/100)
        title = Text(titleBox, text="Ventana de inicio", height=200, size=20)

        buttonsBox = Box(self.app)
        buttonsBox.resize(self.width, (70*self.height)/100)
        

        newGameBox = Box(buttonsBox)
        newGameBox.resize(self.width, (33.333333333*((70*self.height)/100))/100)
        

        newGameButton = PushButton(newGameBox, text="Iniciar juego", height=5, width=40)
       

        resumeGameBox = Box(buttonsBox)
        resumeGameBox.resize(self.width, (33.333333333*((70*self.height)/100))/100)
        

        resumeGameButton = PushButton(resumeGameBox, text="Reanudar juego", height=5, width=40)

        scoreUserBox = Box(buttonsBox)
        scoreUserBox.resize(self.width, (33.333333333*((70*self.height)/100))/100)
        

        scoreUserButton = PushButton(scoreUserBox, text="Mostrar tabla de puntuaciones", height=5, width=40)

        sectionExitBox = Box(self.app)
        sectionExitBox.resize(self.width, (15*self.height)/100)
        

        logoutBox = Box(sectionExitBox)
        logoutBox.resize((30*self.width)/100, (15*self.height)/100)
        logoutBox.bg = "red"

        logoutBtn = PushButton(logoutBox, text="Salir de la sesion", width=20, height=2)
        logoutBtn.text_color = "white"
        logoutBtn.text_size = 14 

        self.display()

