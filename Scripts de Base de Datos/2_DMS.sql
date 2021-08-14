USE GameManager;

INSERT INTO UserRole (var_name) VALUES 
    ("player"),
    ("administrator")
;

INSERT INTO User (var_firstName, var_lastName, var_email, var_nickname, var_password, tin_role_FK) VALUES
    ("Roberto","Duran","rob@email.com","rob", AES_ENCRYPT('12345678','salt'),2),
    ("Fernando","Murillo","fer@email.com","fer", AES_ENCRYPT('12345678','salt'),2),
    ("Marco","Ruiz","mar@email.com","mar" , AES_ENCRYPT('12345678','salt'),2),
    ("Carlos","Gutierrez","car@email.com","car", AES_ENCRYPT('12345678','salt'),1),
    ("David","Perez","dav@email.com","dav", AES_ENCRYPT('12345678','salt'),1),
    ("Alex","Martinez","ale@email.com","ale",AES_ENCRYPT('12345678','salt'),1),
    ("John","Nunez","john@email.com","john",AES_ENCRYPT('12345678','salt'),1)
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