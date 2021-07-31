@author roberto.duran@unah.hn, mruizq@unah.hn, fernando.murillo@unah.hn, yesenia.espinoza@unah.hn
@version 0.1.0

@date 2021/07/15

Documentación de Análisis
===

### Entidades
Se identifican los siguientes tipos entidades:

- Usuario
- Rol de usuario(Administrador y jugador)
- Registro de inicio de sesión(Log): registra cuando un usuario .previamente autenticado inicia sesión.
- ***Registro de Autenticación: Registra cuando un nuevo usuario se identifica dentro de la plataforma.***
- Juego(flood it ó destroy)
- Partida de juego: almacena tiempo de inicio y final de juego.
- Tablero personal: Almacena los 10 mejores tiempos de juegos   exitosos de un usuario.
- Bitacora
- Estado de juego (En espera, pausado, en progreso, derrota y terminado)
- Movimientos


Nota: se menciono que se podria usar un tipo de entidad administrador.

### Relaciones (relationship)

Se identifican las siguientes relaciones entre las entidades mecionadas anteriormente:

- ***Registro de autenticación : Usuario (1:N)***
- Registro de inicio de sesión : Usuario (1:N)
- Usuario : Rol de usuario (1:1)
- Usuario : Partida de juego (N:N)
- Juego : Partida de juego (1:N)
- Tablero personal : Partida de juego (1:N)
- Partida de juego : Estado de juego (1:1)
- Partida de juego : Movimientos (1:N)
- Bitacora : Usuario (1:N) 

Nota: Se considera que la tabla usuario puede servir como registro de autenticación.

