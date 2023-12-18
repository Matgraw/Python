"""
Módulo que tendrá un generador de turnos y un decorador para esos turnos que será lo que
se le mostrará al usuario para que sepa el turno que tiene
"""


def generador_turnos(tipo):
    """
    Generador de turnos para las distintas areas existentes en la farmacia
    :param tipo: [1] es Perfumeria, [2] es Farmacia y [3] es cosmetica
    :return: devuelve el turno correspondiente cuando se invoque a la función
    """
    turno_p = 1
    turno_f = 1
    turno_c = 1

    while True:
        if tipo == "P":
            yield f"{tipo}-{turno_p}"
            turno_p += 1
        elif tipo == "F":
            yield f"{tipo}-{turno_f}"
            turno_f += 1
        else:
            yield f"{tipo}-{turno_c}"
            turno_c += 1


p = generador_turnos("P")
f = generador_turnos("F")
c = generador_turnos("C")


def turno(tipo):
    """
    Decorador de turnos. Es el tiquet que se le daría al usuario al pedir turno
    :param tipo: [1] es Perfumeria, [2] es Farmacia y [3] es cosmetica
    :return: Devuelve el texto con el turno del usuario
    """
    print("*"*25)
    print("Su turno es ")
    if tipo == "P":
        print(next(p))
    elif tipo == "F":
        print(next(f))
    else:
        print(next(c))

    print("Espere a ser atendido")

    print("*" * 25)
