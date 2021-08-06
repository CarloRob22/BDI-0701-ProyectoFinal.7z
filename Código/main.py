from Core.MySQLEngine import MySQLEngine
from Core.ConfigConnection import ConfigConnection
from Core.classes.GameEngine import MyGameEngine
from Core.views.ScreenSplashView import ScreenSplashView

def main():
    
    config = ConfigConnection(
        "localhost",
        "3306",
       "admin",
        "admin",
        "GameManager"
    ) 

    mEngine = MySQLEngine(config)
    gEngine = MyGameEngine(mEngine)

    screenSplash = ScreenSplashView(gEngine, "screen splash")

    screenSplash.app.tk.mainloop()
    


if __name__ == "__main__":
    main()
 