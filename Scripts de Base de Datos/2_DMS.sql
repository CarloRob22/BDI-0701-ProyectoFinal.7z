USE GameManager2;

INSERT INTO UserRole (var_name) VALUES 
    ("player"),
    ("administrator")
;

INSERT INTO User (var_firstName, var_lastName, var_email, var_nickname, var_password, tin_role_FK) VALUES
    ("Fernando","Murillo","fer@email.com","fer","12345678",2),
    ("Carlos","Gutierrez","car@email.com","car","12345678",1),
    ("David","Perez","dav@email.com","dav","12345678",1),
    ("Alex","Martinez","ale@email.com","ale","12345678",1),
    ("John","Nunez","john@email.com","john","12345678",1)
;