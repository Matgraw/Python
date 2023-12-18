from Television import Television
from Mando import Mando

# Creacion de objetos
tele_salon = Television()
mando_salon = Mando(tele_salon)

tele_habitacion = Television()
mando_habitacion = Mando(tele_habitacion)

# Encender los televisores
mando_habitacion.encender_apagar_tv()
mando_salon.encender_apagar_tv()

# Poner canal numero 5 y bajar el volumen dos veces
mando_salon.cambiar_canal_tv(5)

repeticiones = 2
pasadas = 0
while pasadas != repeticiones:
    mando_salon.bajar_volumen_tv()
    pasadas += 1

# Poner canal numero 3 y subir el volumen tres veces
mando_habitacion.cambiar_canal_tv(3)

repeticiones = 3
pasadas = 0
while pasadas != repeticiones:
    mando_habitacion.subir_volumen_tv()
    pasadas += 1

# Conocer el estado de los televisores
tele_salon.estado_televisor()
tele_habitacion.estado_televisor()
