from Core.classes.Auth import Auth

class MyGameEngine:
    
    def __init__(self, db):
        self.db = db
        self.view = None
        self.user = None

    def authUser(self, email, password):
        self.user = Auth(self.db).auth(email, password)
        return self.user
    

    
                    


    
