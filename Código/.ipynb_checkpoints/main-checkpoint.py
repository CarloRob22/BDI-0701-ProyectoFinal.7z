from Core.MySQLEngine import MySQLEngine
from Core.ConfigConnection import ConfigConnection
from Core.classes.gameEngine import MyGameEngine
from Core.views.screenSplash import ScreenSplash

def main():
    
    config = ConfigConnection(
        "localhost",
        "3306",
        "admin",
        "admin",
        "GameManager3"
    ) 

    mEngine = MySQLEngine(config)
    gEngine = MyGameEngine(mEngine)

    screenSplash = ScreenSplash(gEngine, "screen splash")

    screenSplash.app.tk.mainloop()
    


if __name__ == "__main__":
    main()
