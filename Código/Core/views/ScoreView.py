from guizero import *
from .View import View


class ScoreView(View):
    def __init__(self, gEngine, title="view", width=1200, height=900, layout="grid", bg="white", visible=True):
        super().__init__(title, width, height, layout, bg, visible)
        self.gEngine = gEngine
        self.returning = 0

        leftTitleMarginBox = Box(self.app, grid=[0,0], width=(self.width*10)/100, height=(self.height*15)/100, border=1)
        titleContainerBox = Box(self.app, layout="grid", grid=[1,0], width=(self.width*80)/100, height=(self.height*15)/100, border=1)
        titleText = Text(titleContainerBox, text="Tabla de los mejores puntajes obtenidos", size=22, width="fill", height="fill", grid=[0,0])
        rightTitleMarginBox = Box(self.app, grid=[2,0], width=(self.width*10)/100, height=(self.height*15)/100, border=1)


        leftTableMarginBox = Box(self.app, grid=[0,1], width=(self.width*10)/100, height=(self.height*70)/100, border=1)
        tableContainerBox = Box(self.app, layout="grid", grid=[1,1], width=(self.width*80)/100, height=(self.height*70)/100, border=1)
        rightTableMarginBox = Box(self.app, grid=[2,1], width=(self.width*10)/100, height=(self.height*70)/100, border=1)

        tableRowContainerBox1  = Box(tableContainerBox, layout="grid", grid=[0,0], width=(self.width*80)/100, height=(((self.height*70)/100)*10)/100, border=1)
        col1TableRowContainerBox1  = Box(tableRowContainerBox1, layout="grid", grid=[0,0], align="left", width=(((self.width*80)/100)*5)/100, height=(((self.height*70)/100)*10)/100, border=1)
        
        col2TableRowContainerBox1  = Box(tableRowContainerBox1, layout="grid", grid=[1,0], align="left", width=(((self.width*80)/100)*19)/100, height=(((self.height*70)/100)*10)/100, border=1)
        col3TableRowContainerBox1  = Box(tableRowContainerBox1, layout="grid", grid=[2,0], align="left", width=(((self.width*80)/100)*19)/100, height=(((self.height*70)/100)*10)/100, border=1)
        col4TableRowContainerBox1  = Box(tableRowContainerBox1, layout="grid", grid=[3,0], align="left", width=(((self.width*80)/100)*19)/100, height=(((self.height*70)/100)*10)/100, border=1)
        col5TableRowContainerBox1  = Box(tableRowContainerBox1, layout="grid", grid=[4,0], align="left", width=(((self.width*80)/100)*19)/100, height=(((self.height*70)/100)*10)/100, border=1)
        col6TableRowContainerBox1  = Box(tableRowContainerBox1, layout="grid", grid=[5,0], align="left", width=(((self.width*80)/100)*19)/100, height=(((self.height*70)/100)*10)/100, border=1)


        tableRowContainerBox2  = Box(tableContainerBox, layout="grid", grid=[0,1], width=(self.width*80)/100, height=(((self.height*70)/100)*9)/100, border=1)

        tableRowContainerBox3  = Box(tableContainerBox, layout="grid", grid=[0,2], width=(self.width*80)/100, height=(((self.height*70)/100)*9)/100, border=1)

        tableRowContainerBox4  = Box(tableContainerBox, layout="grid", grid=[0,3], width=(self.width*80)/100, height=(((self.height*70)/100)*9)/100, border=1)

        tableRowContainerBox5  = Box(tableContainerBox, layout="grid", grid=[0,4], width=(self.width*80)/100, height=(((self.height*70)/100)*9)/100, border=1)

        tableRowContainerBox6  = Box(tableContainerBox, layout="grid", grid=[0,5], width=(self.width*80)/100, height=(((self.height*70)/100)*9)/100, border=1)

        tableRowContainerBox7  = Box(tableContainerBox, layout="grid", grid=[0,6], width=(self.width*80)/100, height=(((self.height*70)/100)*9)/100, border=1)

        tableRowContainerBox8  = Box(tableContainerBox, layout="grid", grid=[0,7], width=(self.width*80)/100, height=(((self.height*70)/100)*9)/100, border=1)

        tableRowContainerBox9  = Box(tableContainerBox, layout="grid", grid=[0,8], width=(self.width*80)/100, height=(((self.height*70)/100)*9)/100, border=1)

        tableRowContainerBox10  = Box(tableContainerBox, layout="grid", grid=[0,9], width=(self.width*80)/100, height=(((self.height*70)/100)*9)/100, border=1)
        
        tableRowContainerBox11  = Box(tableContainerBox, layout="grid", grid=[0,10], width=(self.width*80)/100, height=(((self.height*70)/100)*9)/100, border=1)


        


          



    