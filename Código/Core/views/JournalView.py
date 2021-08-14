from tkinter import Button, Listbox
from guizero import *
from .View import View


class JournalView(View):
    def __init__(self, gEngine, title="view", width=700, height=500, layout="auto", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)
        self.gEngine = gEngine
        self.returning = 0

        allBox = Box(self.app, layout="auto", width=self.width, height=self.height, border=1)
        allBox.tk.pack()
        allBox.tk.pack_propagate(0)

        #INICIO SECCION DEL TITULO        
        allColBox1 = Box(allBox, layout="auto")
        allColBox1.tk.pack()
        allColBox1.tk.pack_propagate(0)
        allColBox1.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*15)/100)
        #allColBox1.bg = "navy"
        title = Text(allColBox1, text="Registro de bitacora", size=18)
        title.tk.place(x=allColBox1.tk.winfo_reqwidth()/2, y=allColBox1.tk.winfo_reqheight()/2, anchor="center")
        #FINAL SECCION DEL TITULO

        #INICIO SECCION DE LA LISTA
        allColBox2 = Box(allBox, layout="auto")
        allColBox2.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*70)/100)
        allColBox2.tk.pack_propagate(0)

        list = []
        actions = self.gEngine.getJournalActions()
        
        for action in actions:
            #print(action)
            list.append("{} | {}".format(action[0],action[1]))
            print(action[1])

        

        listBox = ListBox(allColBox2, scrollbar=True, items=list)
        listBox.resize((allColBox2.tk.winfo_reqwidth()*85)/100, (allColBox2.tk.winfo_reqheight()*85)/100)
        listBox.tk.place(x=allColBox2.tk.winfo_reqwidth()/2, y=allColBox2.tk.winfo_reqheight()/2, anchor="center")
        listBox.tk.pack_propagate(0)
        listBox.bg = "azure1"
        
        #FINAL SECCION DE LA LISTA
        
        #INICIO SECCIOM DE BOTONES
        allColBox3 = Box(allBox, layout="auto")
        allColBox3.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*15)/100)
        allColBox3.tk.pack_propagate(0)


        returnButton = PushButton(allColBox3, text="Regresar", width=20, height=2, command=self.ReturnAdmin)
        returnButton.tk.place(x=allColBox3.tk.winfo_reqwidth()/2, y=allColBox3.tk.winfo_reqheight()/2, anchor="center")
        returnButton.tk.pack_propagate(0)
        returnButton.bg = "RoyalBlue4"

    def ReturnAdmin(self):
        from .StartAdminView import StartAdminView
        self.app.destroy()
        viewLogin = StartAdminView(self.gEngine, "Admin Start Menu")
          



    