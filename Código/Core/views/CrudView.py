# ------------------------------
# Imports
# ------------------------------

from guizero import *
from .View import View
from .DestroyDotsView import DestroyDotsView
from .FloodItView import FloodItView
import re
import json

class CrudView(View):    
    def __init__(self, gEngine, title="view", width=1400, height=750, layout="grid", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)        
        self.gEngine = gEngine
        self.returning = 1         
        
        insertText = Text(self.app, text="Inserte un nuevo jugador", size=18, height=3, width=55, align="left", grid=[0,0])
        #insertText.bg = "blue"

        insertText = Text(self.app, text="Borrar Jugador", size=18, height=3, width=55, align="left", grid=[1,0])
        #insertText.bg = "blue"

        self.Listbox = ListBox(self.app, height=400, width=500, align="center", grid=[1,1,1,10], scrollbar=True, command=self.onClicItem)
        
        self.tk_Listbox = self.Listbox.children[0].tk
        
        self.fillListUser()
        #self.Listbox.when_clicked = self.onClicItem()
        
        self.DeleteBotton = PushButton(self.app, text="Eliminar", height=2, width=35,  grid=[1,11], command=self.deleteItem)
        self.DeleteBotton.enabled = False
        self.DeleteBotton.bg = "firebrick"

        self.UpdateBotton = PushButton(self.app, text="Actualizar", height=2, width=35,  grid=[1,12], command=self.updateDataUser)
        self.UpdateBotton.enabled = False
        self.UpdateBotton.bg = "tan1"

        FirstNText = Text(self.app, text="Nombre", height=2, width=40, align="left", grid=[0,1])
        #FirstNText.bg = "yellow"

        self.FirstNInput = TextBox(self.app, height=3, width=55 ,multiline=True, grid=[0,2])
        #FirstNInput.bg = "green"

        LastNText = Text(self.app, text="Apellido", height=2, width=40, align="left", grid=[0,3])
        #LastNText.bg = "yellow"

        self.LastNInput = TextBox(self.app, height=3, width=55 ,multiline=True, grid=[0,4])
        #LastNInput.bg = "green"

        EmailText = Text(self.app, text="Correo", height=2, width=40, align="left", grid=[0,5])
        #EmailText.bg = "yellow"

        self.EmailInput = TextBox(self.app, height=3, width=55 ,multiline=True, grid=[0,6])
        #EmailInput.bg = "green"

        NicknameText = Text(self.app, text="Apodo", height=2, width=40, align="left", grid=[0,7])
        #NicknameText.bg = "yellow"

        self.NicknameInput = TextBox(self.app, height=3, width=55 ,multiline=True, grid=[0,8])
        #NicknameInput.bg = "green"

        PasswordText = Text(self.app, text="Contrasena", height=2, width=43, align="left", grid=[0,9])
        #PasswordText.bg = "yellow"

        self.PasswordInput = TextBox(self.app, hide_text=True, height=3, width=55 ,multiline=True, grid=[0,10])
        #PasswordInput.bg = "green"

        #SubmitText = Text(self.app, height=1, width=25, align="left", grid=[0,11])
        #SubmitText.bg = "yellow"

        self.SubmitBotton = PushButton(self.app, text="Agregar", height=2, width=30, grid=[0,12], command=self.insertUser)
        #self.SubmitBotton.enabled = False
        self.SubmitBotton.bg = "green"
        

        #metodo utilizado para llenar lista de usuarios registrados.
    
    def fillListUser(self):
        self.dataUser = self.gEngine.getAllDataUser()
        for i in self.dataUser:
            self.Listbox.insert(i[0],"{} - {} {} - {}".format(i[0],i[1],i[2],i[3]))            
        
    def onClicItem(self):                
        self.select = re.split(' ', self.Listbox.value)[0]          
        self.fillTextboxUser(self.select)
        self.DeleteBotton.enabled = True
        self.UpdateBotton.enabled = True
        self.SubmitBotton.enabled = True

    def deleteItem(self):
        self.gEngine.deleteUser(self.select)
        self.Listbox.clear()
        self.fillListUser()
        self.FirstNInput.value = ''
        self.LastNInput.value = ''
        self.EmailInput.value = ''
        self.NicknameInput.value = ''
        self.PasswordInput.value = ''
        self.DeleteBotton.enabled = False
        self.UpdateBotton.enabled = False
                
    
    def fillTextboxUser(self, idUser):        
        data = self.gEngine.fillTextboxUser(idUser)
        self.userData= json.loads(data[0][0])
        print(self.userData["idUser"])
        self.FirstNInput.value = self.userData["firstName"]
        self.LastNInput.value = self.userData["lastName"]
        self.EmailInput.value = self.userData["email"]
        self.NicknameInput.value = self.userData["nickName"]
        self.PasswordInput.value = self.userData["password"]
        
    def insertUser(self):        
        firsName = re.sub("\s+$", "", self.FirstNInput.value)
        lastName = re.sub("\s+$", "", self.LastNInput.value)
        email = re.sub("\s+$", "",self.EmailInput.value)
        nickName = re.sub("\s+$","",self.NicknameInput.value)
        password = re.sub("\s+$", "", self.PasswordInput.value)

        if firsName != '' and lastName != '' and email != '' and nickName != '' and password != '':
            if self.verifyExistence(email, nickName) == True:
                self.gEngine.insertUser(firsName,lastName,email,nickName, password)
                self.Listbox.clear()
                self.fillListUser()
                self.FirstNInput.value = ''
                self.LastNInput.value = ''
                self.EmailInput.value = ''
                self.NicknameInput.value = ''
                self.PasswordInput.value = ''
            else:
                print("correo o apodo ya registrados")
                self.app.info("Datos no validos", "Correo o apodo ya registrados")
        else:
            self.app.info("Campos vacios", "debe llenar todos los campos")
            
        
    def updateDataUser(self):
        idUser = self.select
        firsName = re.sub("\s+$", "", self.FirstNInput.value)
        lastName = re.sub("\s+$", "", self.LastNInput.value)
        email = re.sub("\s+$", "",self.EmailInput.value)
        nickName = re.sub("\s+$","",self.NicknameInput.value)
        password = re.sub("\s+$", "", self.PasswordInput.value)
        if self.verifyExistence(email, nickName, idUser) == True:
            self.gEngine.updateDataUser(idUser,firsName,lastName,email,nickName, password)
            self.Listbox.clear()
            self.fillListUser()
            self.fillTextboxUser(idUser)
        else:
            print("correo o apodo ya registrados")
            self.app.info("Datos no validos", "Correo o apodo ya registrados")

    def verifyExistence(self,email, nickName,idUser=None):
        self.dataUser = self.gEngine.getAllDataUser()
        for i in self.dataUser:            
            if idUser != None:
                idUser = int(idUser)
                
            if idUser is not int(i[0]): 
                print("{},{}".format(i[0],idUser))
                print("{},{}".format(i[3],email))
                print("{},{}".format(i[4],nickName))
                if i[3] == email or i[4]==nickName:                                    
                    return False
                            
        return True        