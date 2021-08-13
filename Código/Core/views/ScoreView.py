from guizero import *
from .View import View


class ScoreView(View):
    def __init__(self, gEngine, title="view", width=1200, height=900, layout="auto", bg="white", visible=True):
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
        title = Text(allColBox1, text="Tabla de los 10 mejores puntajes", size=18)
        title.tk.place(x=allColBox1.tk.winfo_reqwidth()/2, y=allColBox1.tk.winfo_reqheight()/2, anchor="center")
        #FINAL SECCION DEL TITULO

        #INICIO SECCION DE LA TABLA
        allColBox2 = Box(allBox, layout="auto")
        allColBox2.tk.pack_propagate(0)
        allColBox2.resize(allBox.tk.winfo_reqwidth(), (allBox.tk.winfo_reqheight()*70)/100)
        #allColBox2.bg = "beige"

        tableBox = Box(allColBox2, layout="auto", border=0.2)
        tableBox.resize((allColBox2.tk.winfo_reqwidth()*85)/100, (allColBox2.tk.winfo_reqheight()*85)/100)
        tableBox.tk.place(x=allColBox2.tk.winfo_reqwidth()/2, y=allColBox2.tk.winfo_reqheight()/2, anchor="center")
        tableBox.tk.pack_propagate(0)
            #INICIO FILA 1 DE LA TABLA
        rowTableBox1 = Box(tableBox, layout="auto")
        rowTableBox1.resize(tableBox.tk.winfo_reqwidth(), (tableBox.tk.winfo_reqheight()*10)/100)
        rowTableBox1.tk.pack_propagate(0)
        rowTableBox1.bg ="RoyalBlue4"

                #INICIO COLUMNA 1 FILA 1 DE LA TABLA
        col1RowTableBox1 = Box(rowTableBox1, layout="auto", border=1, align="left")
        col1RowTableBox1.resize((rowTableBox1.tk.winfo_reqwidth()*5)/100, rowTableBox1.tk.winfo_reqheight())
        col1RowTableBox1.tk.pack_propagate(0)
        textCol1RowTableBox1le = Text(col1RowTableBox1, text="N", size=14)
        textCol1RowTableBox1le.tk.place(x=col1RowTableBox1.tk.winfo_reqwidth()/2, y=col1RowTableBox1.tk.winfo_reqheight()/2, anchor="center")
                #FINAL COLUMNA 1 FILA 1 DE LA TABLA

                 #INICIO COLUMNA 2 FILA 1 DE LA TABLA
        col2RowTableBox1 = Box(rowTableBox1, layout="auto", border=1, align="left")
        col2RowTableBox1.resize((rowTableBox1.tk.winfo_reqwidth()*23.75)/100, rowTableBox1.tk.winfo_reqheight())
        col2RowTableBox1.tk.pack_propagate(0)
        textCol2RowTableBox1le = Text(col2RowTableBox1, text="Juego", size=14)
        textCol2RowTableBox1le.tk.place(x=col2RowTableBox1.tk.winfo_reqwidth()/2, y=col2RowTableBox1.tk.winfo_reqheight()/2, anchor="center")
                #FINAL COLUMNA 2 FILA 1 DE LA TABLA

                #INICIO COLUMNA 3 FILA 1 DE LA TABLA
        col3RowTableBox1 = Box(rowTableBox1, layout="auto", border=1, align="left")
        col3RowTableBox1.resize((rowTableBox1.tk.winfo_reqwidth()*23.75)/100, rowTableBox1.tk.winfo_reqheight())
        col3RowTableBox1.tk.pack_propagate(0)
        textCol3RowTableBox1le = Text(col3RowTableBox1, text="Tiempo", size=14)
        textCol3RowTableBox1le.tk.place(x=col3RowTableBox1.tk.winfo_reqwidth()/2, y=col3RowTableBox1.tk.winfo_reqheight()/2, anchor="center")
                #FINAL COLUMNA 3 FILA 1 DE LA TABLA

                #INICIO COLUMNA 4 FILA 1 DE LA TABLA
        col4RowTableBox1 = Box(rowTableBox1, layout="auto", border=1, align="left")
        col4RowTableBox1.resize((rowTableBox1.tk.winfo_reqwidth()*23.75)/100, rowTableBox1.tk.winfo_reqheight())
        col4RowTableBox1.tk.pack_propagate(0)
        textCol4RowTableBox1le = Text(col4RowTableBox1, text="Puntaje", size=14)
        textCol4RowTableBox1le.tk.place(x=col4RowTableBox1.tk.winfo_reqwidth()/2, y=col4RowTableBox1.tk.winfo_reqheight()/2, anchor="center")
                #FINAL COLUMNA 4 FILA 1 DE LA TABLA

                #INICIO COLUMNA 5 FILA 1 DE LA TABLA
        col5RowTableBox1 = Box(rowTableBox1, layout="auto", border=1, align="left")
        col5RowTableBox1.resize((rowTableBox1.tk.winfo_reqwidth()*23.75)/100, rowTableBox1.tk.winfo_reqheight())
        col5RowTableBox1.tk.pack_propagate(0)
        textCol5RowTableBox1le = Text(col5RowTableBox1, text="Fecha", size=14)
        textCol5RowTableBox1le.tk.place(x=col5RowTableBox1.tk.winfo_reqwidth()/2, y=col5RowTableBox1.tk.winfo_reqheight()/2, anchor="center")
                #FINAL COLUMNA 6 FILA 1 DE LA TABLA
            #FINAL FILA 1 DE LA TABLA
            
               
        scores = self.gEngine.getUserScores()
        
        if len(scores)>0:

            counter = 1

            for score in scores.values():
                    #INICIO FILA 1 DE LA TABLA
                rowTableBox1 = Box(tableBox, layout="auto")
                rowTableBox1.resize(tableBox.tk.winfo_reqwidth(), (tableBox.tk.winfo_reqheight()*9)/100)
                rowTableBox1.tk.pack_propagate(0)

                        #INICIO COLUMNA 1 FILA 1 DE LA TABLA
                col1RowTableBox1 = Box(rowTableBox1, layout="auto", border=1, align="left")
                col1RowTableBox1.resize((rowTableBox1.tk.winfo_reqwidth()*5)/100, rowTableBox1.tk.winfo_reqheight())
                col1RowTableBox1.tk.pack_propagate(0)
                textCol1RowTableBox1le = Text(col1RowTableBox1, text="{}".format(counter), size=14)
                textCol1RowTableBox1le.tk.place(x=col1RowTableBox1.tk.winfo_reqwidth()/2, y=col1RowTableBox1.tk.winfo_reqheight()/2, anchor="center")
                        #FINAL COLUMNA 1 FILA 1 DE LA TABLA

                        #INICIO COLUMNA 2 FILA 1 DE LA TABLA
                col2RowTableBox1 = Box(rowTableBox1, layout="auto", border=1, align="left")
                col2RowTableBox1.resize((rowTableBox1.tk.winfo_reqwidth()*23.75)/100, rowTableBox1.tk.winfo_reqheight())
                col2RowTableBox1.tk.pack_propagate(0)
                textCol2RowTableBox1le = Text(col2RowTableBox1, text="{}".format(score['gameName']), size=14)
                textCol2RowTableBox1le.tk.place(x=col2RowTableBox1.tk.winfo_reqwidth()/2, y=col2RowTableBox1.tk.winfo_reqheight()/2, anchor="center")
                        #FINAL COLUMNA 2 FILA 1 DE LA TABLA

                        #INICIO COLUMNA 3 FILA 1 DE LA TABLA
                col3RowTableBox1 = Box(rowTableBox1, layout="auto", border=1, align="left")
                col3RowTableBox1.resize((rowTableBox1.tk.winfo_reqwidth()*23.75)/100, rowTableBox1.tk.winfo_reqheight())
                col3RowTableBox1.tk.pack_propagate(0)
                textCol3RowTableBox1le = Text(col3RowTableBox1, text="{}".format(score['time']), size=14)
                textCol3RowTableBox1le.tk.place(x=col3RowTableBox1.tk.winfo_reqwidth()/2, y=col3RowTableBox1.tk.winfo_reqheight()/2, anchor="center")
                        #FINAL COLUMNA 3 FILA 1 DE LA TABLA

                        #INICIO COLUMNA 4 FILA 1 DE LA TABLA
                col4RowTableBox1 = Box(rowTableBox1, layout="auto", border=1, align="left")
                col4RowTableBox1.resize((rowTableBox1.tk.winfo_reqwidth()*23.75)/100, rowTableBox1.tk.winfo_reqheight())
                col4RowTableBox1.tk.pack_propagate(0)
                textCol4RowTableBox1le = Text(col4RowTableBox1, text="{}".format(score['score']), size=14)
                textCol4RowTableBox1le.tk.place(x=col4RowTableBox1.tk.winfo_reqwidth()/2, y=col4RowTableBox1.tk.winfo_reqheight()/2, anchor="center")
                        #FINAL COLUMNA 4 FILA 1 DE LA TABLA

                        #INICIO COLUMNA 5 FILA 1 DE LA TABLA
                col5RowTableBox1 = Box(rowTableBox1, layout="auto", border=1, align="left")
                col5RowTableBox1.resize((rowTableBox1.tk.winfo_reqwidth()*23.75)/100, rowTableBox1.tk.winfo_reqheight())
                col5RowTableBox1.tk.pack_propagate(0)
                textCol5RowTableBox1le = Text(col5RowTableBox1, text="{}".format(score['date']), size=14)
                textCol5RowTableBox1le.tk.place(x=col5RowTableBox1.tk.winfo_reqwidth()/2, y=col5RowTableBox1.tk.winfo_reqheight()/2, anchor="center")
                        #FINAL COLUMNA 6 FILA 1 DE LA TABLA
                counter = counter + 1
                    #FINAL FILA 1 DE LA TABLA


        

        #FINAL SECCION DE LA TABLA


        


          



    