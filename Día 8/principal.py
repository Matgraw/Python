"""
Modulo para hacer uso del generador de turnos interactuando con el cliente
"""
import numeros


def elegir_area():
    """
    Función que interactúa con el usuario para obtener los turnos que seleccione
    :return: Devuelve las opciones existentes así como la entrada de datos del usuario
    """

    while True:
        print("*" * 25)
        print("Áreas de atención disponibles:")
        print("[P] - Perfumería")
        print("[F] - Farmacia")
        print("[C] - Cosmética")
        print("*" * 25)

        try:
            opcion_elegida = input("Seleccione el área de atención: ").upper()
            ["P", "F", "C"].index(opcion_elegida)
        except ValueError:
            print("No es una opción válida\n")
        else:
            break

    numeros.turno(opcion_elegida)


def inicio():
    """
    Función que interactúa con el usuario para obtener los turnos que seleccione
    :return: Devuelve las opciones existentes así como la entrada de datos del usuario
    """

    while True:
        elegir_area()
        try:
            otro_turno = input("¿Quieres sacar otro turno? [S]/[N] ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("No es una opción válida")
        else:
            if otro_turno == "N":
                print("*" * 25)
                print("* Gracias por su visita *")
                print("*" * 25)
                break


inicio()
