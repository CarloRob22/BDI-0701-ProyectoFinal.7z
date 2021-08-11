USE GameManager;

INSERT INTO UserRole (var_name) VALUES 
    ("player"),
    ("administrator")
;

INSERT INTO User (var_firstName, var_lastName, var_email, var_nickname, var_password, tin_role_FK) VALUES
    ("Roberto","Duran","rob@email.com","rob","12345678",2),
    ("Fernando","Murillo","fer@email.com","fer","12345678",2),
    ("Marco","Ruiz","mar@email.com","mar","12345678",2),
    ("Carlos","Gutierrez","car@email.com","car","12345678",1),
    ("David","Perez","dav@email.com","dav","12345678",1),
    ("Alex","Martinez","ale@email.com","ale","12345678",1),
    ("John","Nunez","john@email.com","john","12345678",1)
;

INSERT INTO GameState (var_name) VALUES
    ("In progress"),
    ("On hold"),
    ("On pause"),    
    ("In defeat"),
    ("In success")
;

INSERT INTO Game (var_name) VALUES
    ("Flood it"),
    ("Destroy the dots")
;