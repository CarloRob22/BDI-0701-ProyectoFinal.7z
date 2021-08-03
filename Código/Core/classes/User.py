

class User:
    def __init__(self,id ,firstName, lastName, email, nickName, role):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.nickName = nickName
        self.role = role
        self.gameMatch = None

    
    def startGameMatch(self):
        pass

    def closeGameMatch(self):
        pass

    def pauseGameMatch(self):
        pass