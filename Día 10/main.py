import pygame
import random
import math
from pygame import mixer

# Iniciar el objeto para permitir toda su funcionalidad
pygame.init()

# Crear la pantalla indicando su tamaño
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Invasión espacial")
icono = pygame.image.load("Iconos\\ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Iconos\\Fondo.jpg")

# Agregar musica
mixer.music.load('Musica\\MusicaFondo.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

# Jugador. Para la posicion, hay que tener en cuenta el tamaño del icono
img_jugador = pygame.image.load("Iconos\\cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Enemigo. Para la posicion, hay que tener en cuenta el tamaño del icono
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 20

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("Iconos\\enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

# Bala. Para la posicion, hay que tener en cuenta el tamaño del icono
balas = []
img_bala = pygame.image.load("Iconos\\bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 2
bala_visible = False

# Variable de puntuacion
puntuacion = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# Texto final de juego
fuente_final = pygame.font.Font('freesansbold.ttf', 40)


def texto_final():
    """
    Funcion que muestra el texto con el final del juego
    :return: No devuelve nada. Solo pinta el texto en la pantalla del juego
    """
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (200, 250))


def mostrar_puntuacion(x, y):
    """
    Funcion que permite pintar la puntuacion en la pantalla del juego
    :param x: Posicion x en la que se encuentra la puntuacion
    :param y: Posicion y en la que se encuentra la puntuacion
    :return: No devuelve nada. Pinta la puntuacion dentro de la pantalla del juego
    """
    texto = fuente.render(f"Puntuación: {puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


def jugador(x, y):
    """
    Funcion que permite pintar al jugador dentro de la pantalla del juego
    :param x: Posicion X en la que se encuentra el jugador
    :param y: Posicion Y en la que se encuentra el jugador
    :return: No devuelve nada. Pinta al jugador dentro de la pantalla del juego
    """
    pantalla.blit(img_jugador, (x, y))


def enemigo(x, y, ene):
    """
    Funcion que permite pintar al enemigo dentro de la pantalla del juego
    :param x: Posicion X en la que se encuentra el enemigo
    :param y: Posicion Y en la que se encuentra el enemigo
    :param ene: Enemigo al que se le esta editando la posicion
    :return: No devuelve nada. Pinta al enemigo dentro de la pantalla del juego
    """
    pantalla.blit(img_enemigo[ene], (x, y))


def disparar_bala(x, y):
    """
    Funcion que permite pintar la bala dentro de la pantalla del juego
    :param x: Posicion X en la que se encuentra la bala
    :param y: Posicion Y en la que se encuentra la bala
    :return: No devuelve nada. Pinta la bala dentro de la pantalla del juego
    """
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


def hay_colision(x_1, y_1, x_2, y_2):
    """
    Funcion que indica si la bala ha chocado contra algún enemigo
    :param x_1: Posicion x del enemigo
    :param y_1: Posicion y del enemigo
    :param x_2: Posicion x de la bala
    :param y_2: Posicion y de la bala
    :return: Devuelve True si ha habido colision o False si no la ha habido
    """
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # Cambiar la imagen del fondo de la pantalla
    pantalla.blit(fondo, (0, 0))

    # Por cada evente que se haga sobre la pantalla que aparece
    for evento in pygame.event.get():
        # Evento cuando se pulsa la X de la pantalla. Esto permite que se cierre el juego
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento cuando se pulsa un tecla del teclado
        if evento.type == pygame.KEYDOWN:
            # Comprobar si ha sido la flecha izquierda
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3

            # Comprobar si ha sido la flecha derecha
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3

            # Comprobar si ha sido la barra espaciadora
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('Musica\\disparo.mp3')
                sonido_bala.set_volume(0.4)
                sonido_bala.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)

        # Evento cuando se suelta una tecla del teclado
        if evento.type == pygame.KEYUP:
            # Comprobar si ha sido la flecha izquierda
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar posicion del jugador
    jugador_x += jugador_x_cambio

    # Mantener dentro de bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Modificar posicion del enemigo
    for e in range(cantidad_enemigos):

        # Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000

            balas.clear()
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # Mantener dentro de bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colision
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])

            if colision_bala_enemigo:
                sonido_colision = mixer.Sound('Musica\\Golpe.mp3')
                sonido_colision.set_volume(0.5)
                sonido_colision.play()
                balas.remove(bala)
                puntuacion += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(50, 200)
                break

        # Se pinta el enemigo dentro de la pantalla
        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento de la bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)

    # Se pinta el jugador dentro de la pantalla
    jugador(jugador_x, jugador_y)

    # Se pinta la puntuacion
    mostrar_puntuacion(texto_x, texto_y)

    # Actualizar para que se vean los cambios
    pygame.display.update()
