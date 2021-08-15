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
    def __init__(self, gEngine, title="view", width=75, height=70, layout="auto", bg="gray92", visible=True):
        super().__init__(title, width, height, layout, bg, visible)        
        self.gEngine = gEngine
        self.returning = 1         
        
        allBox = Box(self.app, layout="auto", width=self.pixel_width, height=self.pixel_height)
        allBox.tk.pack()
        allBox.tk.pack_propagate(0)

        #INICIO SECCION DE FORMULARIO PARA AGREGAR JUGADOR        
        allBoxCol1 = Box(allBox, layout="auto", align="left", border=1)
        allBoxCol1.resize((allBox.tk.winfo_reqwidth()*50)/100, allBox.tk.winfo_reqheight())
        allBoxCol1.tk.pack_propagate(0)

            #INICIO TITULO DE SECCION DE FORMULARIO PARA AGREGAR JUGADOR
        allBoxCol1Row1 = Box(allBoxCol1, layout="auto")
        allBoxCol1Row1.tk.pack()
        allBoxCol1Row1.resize(allBoxCol1.tk.winfo_reqwidth(), (allBoxCol1.tk.winfo_reqheight()*10)/100)
        allBoxCol1Row1.tk.pack_propagate(0)
        allBoxCol1Row1.bg = "forest green"
        title = Text(allBoxCol1Row1, text="Datos del jugador", size=16, color="white")
        title.tk.place(x=allBoxCol1Row1.tk.winfo_reqwidth()/2, y=allBoxCol1Row1.tk.winfo_reqheight()/2, anchor="center")
            #FINAL TITULO DE SECCION DE FORMULARIO PARA AGREGAR JUGADOR

            #INICIO FORMULARIO PARA AGREGAR JUGADOR
        allBoxCol1Row2 = Box(allBoxCol1, layout="auto")
        allBoxCol1Row2.tk.pack()
        allBoxCol1Row2.resize(allBoxCol1.tk.winfo_reqwidth(), (allBoxCol1.tk.winfo_reqheight()*90)/100)
        allBoxCol1Row2.tk.pack_propagate(0)

        allBoxCol1Row2Row1 = Box(allBoxCol1Row2, layout="auto")
        allBoxCol1Row2Row1.resize(allBoxCol1Row2.tk.winfo_reqwidth(), (allBoxCol1Row2.tk.winfo_reqheight()*16.666666667)/100)
        allBoxCol1Row2Row1.tk.pack_propagate(0)

        allBoxLabelCol1Row2Row1 = Box(allBoxCol1Row2Row1, layout="auto")
        allBoxLabelCol1Row2Row1.resize((allBoxCol1Row2Row1.tk.winfo_reqwidth()*78)/100, (allBoxCol1Row2Row1.tk.winfo_reqheight()*40)/100)
        allBoxLabelCol1Row2Row1.tk.place(x=allBoxCol1Row2Row1.tk.winfo_reqwidth()/2, y=allBoxCol1Row2Row1.tk.winfo_reqheight()/2, anchor="center")
        allBoxLabelCol1Row2Row1.tk.pack_propagate(0)

        FirstNText = Text(allBoxLabelCol1Row2Row1, text="Nombre:", align="left")
        FirstNText.text_size = 12

        allBoxInputCol1Row2Row1 = Box(allBoxCol1Row2Row1, layout="auto")
        allBoxInputCol1Row2Row1.resize(allBoxCol1Row2Row1.tk.winfo_reqwidth(), (allBoxCol1Row2Row1.tk.winfo_reqheight()*60)/100)
        allBoxInputCol1Row2Row1.tk.pack_propagate(0)

        self.FirstNInput = TextBox(allBoxInputCol1Row2Row1, width=70, height=2,  multiline=True)
        self.FirstNInput.tk.place(x=allBoxInputCol1Row2Row1.tk.winfo_reqwidth()/2, y=allBoxInputCol1Row2Row1.tk.winfo_reqheight()/2, anchor="center")
        self.FirstNInput.bg = "white"

        allBoxCol1Row2Row2 = Box(allBoxCol1Row2, layout="auto")
        allBoxCol1Row2Row2.resize(allBoxCol1Row2.tk.winfo_reqwidth(), (allBoxCol1Row2.tk.winfo_reqheight()*16.666666667)/100)
        allBoxCol1Row2Row2.tk.pack_propagate(0)

        allBoxLabelCol1Row2Row2 = Box(allBoxCol1Row2Row2, layout="auto")
        allBoxLabelCol1Row2Row2.resize((allBoxCol1Row2Row2.tk.winfo_reqwidth()*78)/100, (allBoxCol1Row2Row2.tk.winfo_reqheight()*40)/100)
        allBoxLabelCol1Row2Row2.tk.place(x=allBoxCol1Row2Row2.tk.winfo_reqwidth()/2, y=allBoxCol1Row2Row2.tk.winfo_reqheight()/2, anchor="center")
        allBoxLabelCol1Row2Row2.tk.pack_propagate(0)

        LastNText = Text(allBoxLabelCol1Row2Row2, text="Apellido:", align="left")
        LastNText.text_size = 12

        allBoxInputCol1Row2Row2 = Box(allBoxCol1Row2Row2, layout="auto")
        allBoxInputCol1Row2Row2.resize(allBoxCol1Row2Row2.tk.winfo_reqwidth(), (allBoxCol1Row2Row2.tk.winfo_reqheight()*60)/100)
        allBoxInputCol1Row2Row2.tk.pack_propagate(0)

        self.LastNInput = TextBox(allBoxInputCol1Row2Row2, width=70, height=2,  multiline=True)
        self.LastNInput.tk.place(x=allBoxInputCol1Row2Row2.tk.winfo_reqwidth()/2, y=allBoxInputCol1Row2Row2.tk.winfo_reqheight()/2, anchor="center")
        self.LastNInput.bg = "white"

        allBoxCol1Row2Row3 = Box(allBoxCol1Row2, layout="auto")
        allBoxCol1Row2Row3.resize(allBoxCol1Row2.tk.winfo_reqwidth(), (allBoxCol1Row2.tk.winfo_reqheight()*16.666666667)/100)
        allBoxCol1Row2Row3.tk.pack_propagate(0)

        allBoxLabelCol1Row2Row3 = Box(allBoxCol1Row2Row3, layout="auto")
        allBoxLabelCol1Row2Row3.resize((allBoxCol1Row2Row3.tk.winfo_reqwidth()*78)/100, (allBoxCol1Row2Row3.tk.winfo_reqheight()*40)/100)
        allBoxLabelCol1Row2Row3.tk.place(x=allBoxCol1Row2Row3.tk.winfo_reqwidth()/2, y=allBoxCol1Row2Row3.tk.winfo_reqheight()/2, anchor="center")
        allBoxLabelCol1Row2Row3.tk.pack_propagate(0)

        EmailText = Text(allBoxLabelCol1Row2Row3, text="Correo:", align="left")
        EmailText.text_size = 12

        allBoxInputCol1Row2Row3 = Box(allBoxCol1Row2Row3, layout="auto")
        allBoxInputCol1Row2Row3.resize(allBoxCol1Row2Row3.tk.winfo_reqwidth(), (allBoxCol1Row2Row3.tk.winfo_reqheight()*60)/100)
        allBoxInputCol1Row2Row3.tk.pack_propagate(0)

        self.EmailInput = TextBox(allBoxInputCol1Row2Row3, width=70, height=2,  multiline=True)
        self.EmailInput.tk.place(x=allBoxInputCol1Row2Row3.tk.winfo_reqwidth()/2, y=allBoxInputCol1Row2Row3.tk.winfo_reqheight()/2, anchor="center")
        self.EmailInput.bg = "white"

        allBoxCol1Row2Row4 = Box(allBoxCol1Row2, layout="auto")
        allBoxCol1Row2Row4.resize(allBoxCol1Row2.tk.winfo_reqwidth(), (allBoxCol1Row2.tk.winfo_reqheight()*16.666666667)/100)
        allBoxCol1Row2Row4.tk.pack_propagate(0)

        allBoxLabelCol1Row2Row4 = Box(allBoxCol1Row2Row4, layout="auto")
        allBoxLabelCol1Row2Row4.resize((allBoxCol1Row2Row4.tk.winfo_reqwidth()*78)/100, (allBoxCol1Row2Row4.tk.winfo_reqheight()*40)/100)
        allBoxLabelCol1Row2Row4.tk.place(x=allBoxCol1Row2Row4.tk.winfo_reqwidth()/2, y=allBoxCol1Row2Row4.tk.winfo_reqheight()/2, anchor="center")
        allBoxLabelCol1Row2Row4.tk.pack_propagate(0)

        NicknameText = Text(allBoxLabelCol1Row2Row4, text="Apodo:", align="left")
        NicknameText.text_size = 12

        allBoxInputCol1Row2Row4 = Box(allBoxCol1Row2Row4, layout="auto")
        allBoxInputCol1Row2Row4.resize(allBoxCol1Row2Row4.tk.winfo_reqwidth(), (allBoxCol1Row2Row4.tk.winfo_reqheight()*60)/100)
        allBoxInputCol1Row2Row4.tk.pack_propagate(0)

        self.NicknameInput = TextBox(allBoxInputCol1Row2Row4, width=70, height=2,  multiline=True)
        self.NicknameInput.tk.place(x=allBoxInputCol1Row2Row4.tk.winfo_reqwidth()/2, y=allBoxInputCol1Row2Row4.tk.winfo_reqheight()/2, anchor="center")
        self.NicknameInput.bg = "white"

        allBoxCol1Row2Row5 = Box(allBoxCol1Row2, layout="auto")
        allBoxCol1Row2Row5.resize(allBoxCol1Row2.tk.winfo_reqwidth(), (allBoxCol1Row2.tk.winfo_reqheight()*16.666666667)/100)
        allBoxCol1Row2Row5.tk.pack_propagate(0)

        allBoxLabelCol1Row2Row5 = Box(allBoxCol1Row2Row5, layout="auto")
        allBoxLabelCol1Row2Row5.resize((allBoxCol1Row2Row5.tk.winfo_reqwidth()*78)/100, (allBoxCol1Row2Row5.tk.winfo_reqheight()*40)/100)
        allBoxLabelCol1Row2Row5.tk.place(x=allBoxCol1Row2Row5.tk.winfo_reqwidth()/2, y=allBoxCol1Row2Row5.tk.winfo_reqheight()/2, anchor="center")
        allBoxLabelCol1Row2Row5.tk.pack_propagate(0)

        passwordText = Text(allBoxLabelCol1Row2Row5, text="Clave de acceso:", align="left")
        passwordText.text_size = 12

        allBoxInputCol1Row2Row5 = Box(allBoxCol1Row2Row5, layout="auto")
        allBoxInputCol1Row2Row5.resize(allBoxCol1Row2Row5.tk.winfo_reqwidth(), (allBoxCol1Row2Row5.tk.winfo_reqheight()*60)/100)
        allBoxInputCol1Row2Row5.tk.pack_propagate(0)

        self.PasswordInput = TextBox(allBoxInputCol1Row2Row5, width=70, height=2,  multiline=True)
        self.PasswordInput.tk.place(x=allBoxInputCol1Row2Row5.tk.winfo_reqwidth()/2, y=allBoxInputCol1Row2Row5.tk.winfo_reqheight()/2, anchor="center")
        self.PasswordInput.bg = "white"

        allBoxCol1Row2Row6 = Box(allBoxCol1Row2, layout="auto")
        allBoxCol1Row2Row6.resize(allBoxCol1Row2.tk.winfo_reqwidth(), (allBoxCol1Row2.tk.winfo_reqheight()*16.666666667)/100)
        allBoxCol1Row2Row6.tk.pack_propagate(0)


        allBoxCol1Row2Row6Col1 = Box(allBoxCol1Row2Row6, layout="auto", align="left")
        allBoxCol1Row2Row6Col1.tk.pack()
        allBoxCol1Row2Row6Col1.resize((allBoxCol1Row2Row6.tk.winfo_reqwidth()*50)/100, allBoxCol1Row2Row6.tk.winfo_reqheight())
        allBoxCol1Row2Row6Col1.tk.pack_propagate(0)

        self.SubmitBotton = PushButton(allBoxCol1Row2Row6Col1, text="Agregar", width=30, height=3, command=self.insertUser)
        self.SubmitBotton.tk.place(x=allBoxCol1Row2Row6Col1.tk.winfo_reqwidth()/2, y=allBoxCol1Row2Row6Col1.tk.winfo_reqheight()/2, anchor="center")
        self.SubmitBotton.tk.pack_propagate(0)
        self.SubmitBotton.bg = "forest green"
        self.SubmitBotton.text_color = "white"


        allBoxCol1Row2Row6Col2 = Box(allBoxCol1Row2Row6, layout="auto", align="left")
        allBoxCol1Row2Row6Col2.tk.pack()
        allBoxCol1Row2Row6Col2.resize((allBoxCol1Row2Row6.tk.winfo_reqwidth()*50)/100, allBoxCol1Row2Row6.tk.winfo_reqheight())
        allBoxCol1Row2Row6Col2.tk.pack_propagate(0)

        self.returnBotton = PushButton(allBoxCol1Row2Row6Col2, text="Regresar", width=30, height=3,command=self.ReturnAdmin)
        self.returnBotton.tk.place(x=allBoxCol1Row2Row6Col2.tk.winfo_reqwidth()/2, y=allBoxCol1Row2Row6Col2.tk.winfo_reqheight()/2, anchor="center")
        self.returnBotton.tk.pack_propagate(0)
        self.returnBotton.bg = "plum4"
        self.returnBotton.text_color = "white"



        #INICIO SECCION DE FORMULARIO PARA ELIMINAR O ACTUALIZAR JUGADOR        
        allBoxCol2 = Box(allBox, layout="auto", align="left")
        allBoxCol2.resize((allBox.tk.winfo_reqwidth()*50)/100, allBox.tk.winfo_reqheight())
        allBoxCol2.tk.pack_propagate(0)

            #INICIO TITULO DE SECCION DE FORMULARIO PARA ELIMINAR O ACTUALIZAR JUGADOR
        allBoxCol2Row1 = Box(allBoxCol2, layout="auto")
        allBoxCol2Row1.tk.pack()
        allBoxCol2Row1.tk.pack_propagate(0)
        allBoxCol2Row1.resize(allBoxCol2.tk.winfo_reqwidth(), (allBoxCol2.tk.winfo_reqheight()*10)/100)
        allBoxCol2Row1.bg = "navy"
        title = Text(allBoxCol2Row1, text="Lista de usuarios", size=16, color="white")
        title.tk.place(x=allBoxCol2Row1.tk.winfo_reqwidth()/2, y=allBoxCol2Row1.tk.winfo_reqheight()/2, anchor="center")

        allBoxCol2Row2 = Box(allBoxCol2, layout="auto")
        allBoxCol2Row2.tk.pack()
        allBoxCol2Row2.resize(allBoxCol2.tk.winfo_reqwidth(), (allBoxCol2.tk.winfo_reqheight()*75)/100)
        allBoxCol2Row2.tk.pack_propagate(0)

        self.Listbox = ListBox(allBoxCol2Row2, scrollbar=True, command=self.onClicItem)
        self.Listbox.resize((allBoxCol2Row2.tk.winfo_reqwidth()*80)/100, (allBoxCol2Row2.tk.winfo_reqheight()*80)/100)
        self.Listbox.tk.place(x=allBoxCol2Row2.tk.winfo_reqwidth()/2, y=allBoxCol2Row2.tk.winfo_reqheight()/2, anchor="center")    
        self.Listbox.tk.pack_propagate(0)
        self.Listbox.bg = "white"
        

        allBoxCol2Row3 = Box(allBoxCol2, layout="auto")
        allBoxCol2Row3.tk.pack()
        allBoxCol2Row3.resize(allBoxCol2.tk.winfo_reqwidth(), (allBoxCol2.tk.winfo_reqheight()*15)/100)
        allBoxCol2Row3.tk.pack_propagate(0)

        allBoxCol2Row3Col1 = Box(allBoxCol2Row3, layout="auto", align="left")
        allBoxCol2Row3Col1.tk.pack()
        allBoxCol2Row3Col1.resize((allBoxCol2Row3.tk.winfo_reqwidth()*50)/100, allBoxCol2Row3.tk.winfo_reqheight())
        allBoxCol2Row3Col1.tk.pack_propagate(0)

        self.DeleteBotton = PushButton(allBoxCol2Row3Col1, text="Eliminar", width=30, height=3, command=self.deleteItem)
        self.DeleteBotton.tk.place(x=allBoxCol2Row3Col1.tk.winfo_reqwidth()/2, y=allBoxCol2Row3Col1.tk.winfo_reqheight()/2, anchor="center")
        self.DeleteBotton.tk.pack_propagate(0)
        self.DeleteBotton.bg = "firebrick"
        self.DeleteBotton.text_color = "white"


        allBoxCol2Row3Col2 = Box(allBoxCol2Row3, layout="auto", align="left")
        allBoxCol2Row3Col2.tk.pack()
        allBoxCol2Row3Col2.resize((allBoxCol2Row3.tk.winfo_reqwidth()*50)/100, allBoxCol2Row3.tk.winfo_reqheight())
        allBoxCol2Row3Col2.tk.pack_propagate(0)

        self.UpdateBotton = PushButton(allBoxCol2Row3Col2, text="Actualizar", width=30, height=3,command=self.updateDataUser)
        self.UpdateBotton.tk.place(x=allBoxCol2Row3Col2.tk.winfo_reqwidth()/2, y=allBoxCol2Row3Col2.tk.winfo_reqheight()/2, anchor="center")
        self.UpdateBotton.tk.pack_propagate(0)
        self.UpdateBotton.bg = "tan1"
        self.UpdateBotton.text_color = "white"

        self.fillListUser()



            #FINAL TITULO DE SECCION DE FORMULARIO PARA ELIMINAR O ACTUALIZAR JUGADOR
             
        
        

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

    def ReturnAdmin(self):
        from .StartAdminView import StartAdminView
        self.app.destroy()
        viewLogin = StartAdminView(self.gEngine, "Admin Start Menu")      