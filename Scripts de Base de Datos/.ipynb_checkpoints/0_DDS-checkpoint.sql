DROP DATABASE IF EXISTS GameManager;

CREATE DATABASE GameManager CHARACTER SET "utf8";

USE GameManager;

CREATE TABLE IF NOT EXISTS UserRole(
    tin_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
        COMMENT "Corresponde al identificador del rol de un usaurio",
    var_name VARCHAR(20) NOT NULL
        COMMENT "Corresponde al nombre del rol de usuario. En la aplicacion existiran
        dos roles; Usuario Jugador y Usuario administrador"
) COMMENT "Esta relation corresponde al tipo de entidad Rol de Usuario, la cual, 
almacena los roles que puede tener cada usuario dentro de la aplicacion";

CREATE TABLE IF NOT EXISTS User(
    int_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
        COMMENT "Corresponde al identificador del usuario",
    var_firstName VARCHAR(30) NOT NULL
        COMMENT "Corresponde al primer nombre del usuario",
    var_lastName VARCHAR(30) NOT NULL DEFAULT ""
        COMMENT "Corresponde al segundo nombre del usuario",
    var_email VARCHAR(60) UNIQUE NOT NULL 
        COMMENT "Corresponde al correo con el cual iniciar sesion el usuario",
    var_nickname VARCHAR(100) UNIQUE NOT NULL
        COMMENT "Corresponde a una palabra clave opcional con la cual el usuario
        podra iniciar sesion, tambien esta palabra clase se mostraria en cada score
        del jugador en conjunto con los nombres",
    var_password VARCHAR(20) NOT NULL
        COMMENT "Se utiliza en conjunto con el correo o nickname para inciar sesion",
    tin_role_FK TINYINT UNSIGNED NOT NULL
        COMMENT "Corresponde a la llave foranea que hace referencia al id del rol 
        del usuario",
    CONSTRAINT tin_role_FK1 FOREIGN KEY (tin_role_FK) REFERENCES UserRole(tin_id)
) COMMENT "Esta relation corresponde al tipo de entidad Usuario, la cual, Almacena los datos
de un usuario registrado";

CREATE TABLE IF NOT EXISTS UserSession(
    int_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
        COMMENT "Corresponde al identificador de cada sesion iniciada por un jugador registrado",
    tim_dueDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        COMMENT "Corresponde a la fecha y hora en que se inicio sesion",
    int_user_FK INT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea hace referencia al usuario registrado que inicio sesion",
    CONSTRAINT int_user_FK1 FOREIGN KEY(int_user_FK) REFERENCES User(int_id)
) COMMENT "Esta relation corresponde al tipo de entidad Sesion_De_Usuario, la cual genera un registro
cada vez que el usuario autentica sus datos. Esta relacion es de utilidad para recolectar
analiticos relacionados con la fecha de creacion de registros. Tambien normaliza el campo
fecha_de_creacion para muchas tablas";

CREATE TABLE IF NOT EXISTS GameState(
    tin_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
        COMMENT "Corresponde al identificador del estado que puede tener cada juego",
    var_name VARCHAR(30) NOT NULL
        COMMENT "Corresponde al nombre del estado de juego; Los estados de juego son
        juego en espera, juego pausado o juego actual en progreso."
) COMMENT "Esta relation corresponde al tipo de entidad Estado_de_juego, la cual,
almacena los tipos de estado que puede tener cada juego";

CREATE TABLE IF NOT EXISTS Game(
    tin_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
        COMMENT "Corresponde al identificador de cada juego que se puede manejar",
    var_name VARCHAR(50) NOT NULL
        COMMENT "Corresponde al nombre del juego; Los juegos disponibles seran Flood It y Destroy the dots"
) COMMENT "Esta relation corresponde al tipo de entidad Juego, la cual, almacena
los juegos disponibles en la aplicacion";

CREATE TABLE IF NOT EXISTS GameMatch(
    int_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT "Corresponde al identificador de cada partida de juego",
    tin_game_FK TINYINT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea indica el juego al cual pertenece la partida",
    int_session_FK INT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea nos proporciona la informacion de quien, cuando y en que sesion se creo la partida",
    CONSTRAINT tin_game_FK1 FOREIGN KEY(tin_game_FK) REFERENCES Game(tin_id),
    CONSTRAINT int_session_FK1 FOREIGN KEY(int_session_FK) REFERENCES UserSession(int_id)
) COMMENT "Esta relacion corresponde al tipo de entidad Partida, en la cual se
crea un nuevo registro, cada vez que se inicia un juego nuevo";

CREATE TABLE IF NOT EXISTS Score(
    int_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
        COMMENT "Corresponde al identificador del puntaje de un juego",
    sma_score SMALLINT UNSIGNED NOT NULL
        COMMENT "Corresponde a la magnitud del puntaje obtenido. Se selecciono
        el tipo SMALLINT ya que los puntajes maximos de los juegos seleccionados
        no tienden a ser muy altos",
    tim_timeScore TIME NOT NULL
        COMMENT "Corresponde al tiempo que le tomo al jugador obtener el puntaje",
    int_match_FK INT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea nos indica para que partida se registro el puntaje",
    int_session_FK INT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea nos proporciona la informacion de cuando
        y en que sesion se registro el puntaje",
    CONSTRAINT int_match_FK1 FOREIGN KEY(int_match_FK) REFERENCES GameMatch(int_id),
    CONSTRAINT int_session_FK2 FOREIGN KEY(int_session_FK) REFERENCES UserSession(int_id)
) COMMENT "Esta relacion corresponde al tipo de entidad Puntaje, en la cual se crea un nuevo
registro cada vez que un jugador termina una partida";

CREATE TABLE IF NOT EXISTS Movement(
    int_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
        COMMENT "Corresponde al identificador de cada movimiento realizado en una partida",
    tim_timeMovement TIME NOT NULL
        COMMENT "Corresponde al tiempo en que tardo el jugador en realizar el movimiento",
    int_match_FK INT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea nos indica para que partida se registro el movimiento",
    int_session_FK INT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea nos indica en que sesion se realizo el movimiento",
    CONSTRAINT int_match_FK2 FOREIGN KEY(int_match_FK) REFERENCES GameMatch(int_id),
    CONSTRAINT int_session_FK3 FOREIGN KEY(int_session_FK) REFERENCES UserSession(int_id)
) COMMENT "Esta relacion conrresponde al tipo de entidad Movimiento, en la cual se crea unj registro
cada vez que un jugador realiza un movimiento dentro de una partida";

CREATE TABLE IF NOT EXISTS StateMatch(
    int_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
        COMMENT "Corresponde al identificador de cada cambio de estado en una partida",
    tin_gameState_FK TINYINT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea nos indica cual fue el estado de juego al que se cambio 
        valga la redundancia el juego",
    int_match_FK INT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea nos indica para que partida ocurrio el cambio de estado",
    int_session_FK INT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea nos indica en que sesion o fecha ocurrio el cambio de estado para la partida",
    CONSTRAINT int_match_FK3 FOREIGN KEY(int_match_FK) REFERENCES GameMatch(int_id),
    CONSTRAINT int_session_FK4 FOREIGN KEY(int_session_FK) REFERENCES UserSession(int_id),
    CONSTRAINT tin_gameState_FK1 FOREIGN KEY(tin_gameState_FK) REFERENCES GameState(tin_id)
) COMMENT "Esta relacion corresponde al tipo de entidad Cambio De Estado, la almacena un registro
cada vez que un jugador decida cambiar el estado del juego dentro de una partida. ya sea
pausandolo, iniciandolo o manteniendolo en caso de cerrar la aplicacion";