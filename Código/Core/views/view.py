from guizero import App

class View:
    def __init__(self, title="view", width=700, height=700, layout="auto", bg="white", visible=True):
        self.title = title
        self.width = width
        self.height = height
        self.layout = layout
        self.bg = bg
        self.visible = visible
        self.app = App(title=self.title, width=self.width, height=self.height, layout=self.layout, bg=self.bg, visible=self.visible)
        self.show_center() 

    def show_center(self):
        screen_width = self.app.tk.winfo_screenwidth()
        screen_height = self.app.tk.winfo_screenheight()
        x = (screen_width/2) - (self.width/2)
        y = (screen_height/2) - (self.height/2)
        self.app.tk.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))
        

        

    def display(self):
        self.app.display()