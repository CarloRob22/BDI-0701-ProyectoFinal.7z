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
    big_id SERIAL PRIMARY KEY
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
    var_password VARBINARY(255) NOT NULL
        COMMENT "Se utiliza en conjunto con el correo o nickname para inciar sesion",
    tin_role_FK TINYINT UNSIGNED NOT NULL
        COMMENT "Corresponde a la llave foranea que hace referencia al id del rol 
        del usuario",
    CONSTRAINT tin_role_FK1 FOREIGN KEY (tin_role_FK) REFERENCES UserRole(tin_id)
) COMMENT "Esta relation corresponde al tipo de entidad Usuario, la cual, Almacena los datos
de un usuario registrado";

CREATE TABLE IF NOT EXISTS Journal(
    big_id SERIAL PRIMARY KEY
        COMMENT "Corresponde al identificador de cada registro de bitacora",
    tim_dueDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        COMMENT "Corresponde a la fecha y hora en que se registro la accion del usuario",
    var_action VARCHAR(500) NOT NULL
        COMMENT "Mediante este campo se describe la acción insertada en la bitácora",
    big_user_FK BIGINT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea hace referencia al usuario que realizo la accion
        registrada en la bitacora",    
    CONSTRAINT big_user_FK2 FOREIGN KEY(big_user_FK) REFERENCES User(big_id)
) COMMENT "Esta relacion corresponde al tipo de entidad Bitacora, la cual almacena un
registro cada vez que un usuario realiza algunas acciones especificas dentro de la
aplicacion";

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
    big_id SERIAL PRIMARY KEY COMMENT "Corresponde al identificador de cada partida de juego",
    tim_lastTime TIME NOT NULL DEFAULT "00:00:00"
        COMMENT "Corresponde al ultimo tiempo de juego registrado, el cual se actualiza cada vez que un jugador hace un cambio de estado
        en el juego",
    tim_dueDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "Corresponde a la fecha en que se creo la partida",
    tin_game_FK TINYINT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea indica el juego al cual pertenece la partida",
    big_user_FK BIGINT UNSIGNED NOT NULL 
        COMMENT "Esta llave foranea indica el jugador que inicio la partida",
    tin_gameState_FK TINYINT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea indica el estado en el que se encuentra el juego",
    CONSTRAINT tin_game_FK1 FOREIGN KEY(tin_game_FK) REFERENCES Game(tin_id),
    CONSTRAINT big_user_FK3 FOREIGN KEY(big_user_FK) REFERENCES User(big_id),
    CONSTRAINT tin_gameState_FK1 FOREIGN KEY(tin_game_FK) REFERENCES GameState(tin_id)
) COMMENT "Esta relacion corresponde al tipo de entidad Partida, en la cual se
crea un nuevo registro, cada vez que se inicia un juego nuevo";

CREATE TABLE IF NOT EXISTS Score(
    big_id SERIAL PRIMARY KEY
        COMMENT "Corresponde al identificador del puntaje de un juego",
    dec_score DECIMAL(6,2) UNSIGNED NOT NULL
        COMMENT "Corresponde a la magnitud del puntaje obtenido. Se selecciono
        el tipo SMALLINT ya que los puntajes maximos de los juegos seleccionados
        no tienden a ser muy altos",
    tim_timeScore TIME NOT NULL
        COMMENT "Corresponde al tiempo que le tomo al jugador obtener el puntaje",
    tim_dueDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP 
        COMMENT "Corresponde a la fecha en que se registro el puntaje",
    big_match_FK BIGINT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea nos indica para que partida se registro el puntaje",
    CONSTRAINT big_match_FK1 FOREIGN KEY(big_match_FK) REFERENCES GameMatch(big_id)
) COMMENT "Esta relacion corresponde al tipo de entidad Puntaje, en la cual se crea un nuevo
registro cada vez que un jugador termina una partida";

CREATE TABLE IF NOT EXISTS Movement(
    big_id SERIAL PRIMARY KEY
        COMMENT "Corresponde al identificador de cada movimiento realizado en una partida",
    tim_timeMovement TIME NOT NULL
        COMMENT "Corresponde al tiempo en que tardo el jugador en realizar el movimiento",
    blo_move  BLOB NOT NULL 
        COMMENT "Este campo guarda el movimiento realizado en un formato json",
    big_match_FK BIGINT UNSIGNED NOT NULL
        COMMENT "Esta llave foranea nos indica en que partida ocurre el movimiento",    
    CONSTRAINT big_match_FK2 FOREIGN KEY(big_match_FK) REFERENCES GameMatch(big_id)
) COMMENT "Esta relacion conrresponde al tipo de entidad Movimiento, en la cual se crea unj registro
cada vez que un jugador realiza un movimiento dentro de una partida";

    