from guizero import *
from .View import View
from .DestroyDotsView import DestroyDotsView
from .FloodItView import FloodItView

class StartPlayerView(View):
    def __init__(self, gEngine, title="view", width=700, height=700, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)
        self.gEngine = gEngine

        
        #Estilos para el titulo de la ventana
        titleBox = Box(self.app)
        titleBox.resize(self.width, (15*self.height)/100)
        title = Text(titleBox, text="Ventana de inicio", height=200, size=20)

        buttonsBox = Box(self.app)
        buttonsBox.resize(self.width, (70*self.height)/100)

        newFloodItBox = Box(buttonsBox)
        newFloodItBox.resize(self.width, (25*((70*self.height)/100))/100)
        newFloodItButton = PushButton(newFloodItBox, text="Iniciar juego Flood It", height=4, width=40, command=self.newFloodIt)

        newDestroyDotsBox = Box(buttonsBox)
        newDestroyDotsBox.resize(self.width, (25*((70*self.height)/100))/100)
        newDestroyDotsButton = PushButton(newDestroyDotsBox, text="Iniciar juego Destroy the dots", height=4, width=40, command=self.newDestroyDots)

        resumeGameBox = Box(buttonsBox)
        resumeGameBox.resize(self.width, (25*((70*self.height)/100))/100)
        resumeGameButton = PushButton(resumeGameBox, text="Reanudar juego", height=4, width=40)

        scoreUserBox = Box(buttonsBox)
        scoreUserBox.resize(self.width, (25*((70*self.height)/100))/100)
        scoreUserButton = PushButton(scoreUserBox, text="Mostrar tabla de puntuaciones", height=4, width=40)

        sectionExitBox = Box(self.app)
        sectionExitBox.resize(self.width, (15*self.height)/100)
        

        logoutBox = Box(sectionExitBox)
        logoutBox.resize((30*self.width)/100, (15*self.height)/100)
        logoutBox.bg = "red"

        logoutBtn = PushButton(logoutBox, text="Salir de la sesion", width=20, height=2, command=self.app.destroy)
        logoutBtn.text_color = "white"
        logoutBtn.text_size = 14 

    def newFloodIt(self):
        self.app.destroy()
        self.gEngine.startMatch(1)
        destroyDots = FloodItView()

    def newDestroyDots(self):
        self.app.destroy()
        self.gEngine.startMatch(2)
        destroyDots = DestroyDotsView()
        


    



    