from Core.MySQLEngine import MySQLEngine
from Core.ConfigConnection import ConfigConnection
from Core.classes.GameEngine import MyGameEngine
from Core.views.ScreenSplashView import ScreenSplashView
import configparser
import os


def main():    
    config = configparser.ConfigParser()
    config.sections()
    
    config.read('../config.ini')    
  
    Host = config['mysql']['host']
    Port = int(config['mysql']['port'])
    User = config['mysql']['user']
    Pws = config['mysql']['password']
    Dabase = config['mysql']['database']


    config = ConfigConnection(
        Host,
        Port,
        User,
        Pws,
        Dabase
    ) 

    mEngine = MySQLEngine(config)
    gEngine = MyGameEngine(mEngine)

    screenSplash = ScreenSplashView(gEngine, "screen splash")

    screenSplash.app.tk.mainloop()
    


if __name__ == "__main__":
    main()