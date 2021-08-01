from guizero import *
from .view import View
from .viewStartMenu import ViewStartMenu
from .admin_interface import AdminInterface
from Core.views.ConfigConnection import ConfigConnection
#from Core.views.MySQLEngine import MySQLEngine
import mysql.connector

    


#mEngine = MySQLEngine(config)



#la.execute("SELECT * FROM userRole")

#la.execute("SELECT var_nickname, var_password FROM User;")

#result = la.fetchall()
#for i in result:
#    print(i)



class ViewLogin(View):
    mydb = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='123Qweasd',
        database='GameManager2'
    )
    mydb.cursor(buffered=True)

    def __init__(self, title="view", width=840, height=620, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)

 
        titleBox = Box(self.app)
        titleBox.resize(self.width, (15*self.height)/100)
        title = Text(titleBox, text="Bienvenido", height=150, size=25)

        buttonsBox = Box(self.app)
        buttonsBox.resize(self.width, (5*self.height)/100)


#----------Login-----------
#aun no funciona
    def Autenticar(cknickname,ckpassword):
        mydb = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='123Qweasd',
            database='GameManager2'
        )
        mydb.cursor()
        if mbdb.is_connected() == False:
           mydb.connect()
 
        else:

            la = mydb.cursor()
            
            query="SELECT var_nickname, var_password FROM User"

            try:
                la.execute(query)
                select=la.fetchall()
                openPlayer(self)
                for i in select:
                    print(i)          
            except:
                mydb.rollback()
                print("No inventes wey, no se pudo")
            finally:
                mydb.close()
        def probar():
            usuario=nickname.value
            contra=password.value

            Autenticar(usuario,contra)          

        def insert_nick(self):
            pass


        def insert_pass(self):
            pass

        labelnick = Text(self.app, text="Nickname") 
        nickname = TextBox(self.app)
        labelpassword = Text(self.app, text="Password") 
        password = TextBox(self.app, hide_text=True)
        submitBox = Box(self.app)
        submitBox.resize(self.width, (15*self.height)/100)

        submitButton = PushButton(submitBox, text="Submit", command=probar)


#------------Autores--------
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

        def condicion(self):
            pass


        def openPlayer(self):
            self.app.destroy()
            viewLogin = ViewStartMenu("algo")

        def openAdmin(self):
            self.app.destroy()
            viewLogin = AdminInterface()

        def verifyRole():
            pass