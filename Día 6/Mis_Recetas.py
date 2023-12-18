import os
from pathlib import Path
from os import system

def bienvenida():
    print("*"*50)
    print("Bienvenido al administrador de recetas...")
    ruta_recetas = Path(os.getcwd()) / "Recetas"
    print(f"Las recetas se encuentran en: {ruta_recetas}.")

    total_recetas = len(list(Path(ruta_recetas).glob("**/*.txt")))
    print(f"Tienes un total de {total_recetas} recetas.")
    print(f"Debe elegir una de las siguientes opciones para continuar:")
    print(f"[1] - leer receta")
    print(f"[2] - crear receta")
    print(f"[3] - crear categoría")
    print(f"[4] - eliminar receta")
    print(f"[5] - eliminar categoría")
    print(f"[6] - finalizar programa")
    print("*" * 50)

    return ruta_recetas

def listar_categorias_recetas(ruta,tipo):
    """
    Funcion que devuelve la lista de categorias or recetas existentes en un ruta especificada
    :param ruta: ruta donde se van a buscar las categorias o recetas
    :param tipo: Si es 1 se listan las categorias
                 Si es 2 se listan las recetas
    :return: Devuelve una lista de categorias o de recetas
    """
    categorias_recetas = []
    ficheros = os.scandir(ruta)
    for fichero in ficheros:
        if tipo == 1 and fichero.is_dir():
            categorias_recetas.append(fichero.name)
        elif tipo == 2 and fichero.is_file():
            categorias_recetas.append(fichero.name.rstrip(".txt"))

    return ' \n- '.join(categorias_recetas)

def elegir_opcion(teclado, ruta):
    """
    Funcion que le pide informacion al usuario por pantalla
    :param teclado: Si es 1 es la opcion a realizar,
                    Si es 2 es la categoria elegida
                    Si es 3 es la receta elegida
                    Si es 4 es la categoria que se va a crear
                    Si es 5 es el nombre de la receta que se va a crear
                    Si es 6 es la espera del usuario para continuar
    :param ruta: Ruta donde se encuentran las categorias y recetas
    :return: devuelve la opcion seleccionada segun cada cosa
    """
    if teclado == 1:
        opcion_seleccionada = input("Seleccione opción deseada: ")

        while opcion_seleccionada not in ('1','2','3','4','5','6'):
            print("La opción seleccionada no es válida. Elige uno de los valores permitidos")
            opcion_seleccionada = input("Seleccione opción deseada: ")

        return opcion_seleccionada

    elif teclado == 2:
        categorias = listar_categorias_recetas(ruta,1)
        opcion_seleccionada = input(f"Elige una de las siguientes categorías:\n- {categorias}\n=> ")
        return opcion_seleccionada
    elif teclado == 3:
        categorias = listar_categorias_recetas(ruta,2)
        opcion_seleccionada = input(f"Elige una de las siguientes recetas:\n- {categorias}\n=>")
        return opcion_seleccionada
    elif teclado == 4:
        opcion_seleccionada = input(f"Elige el nombre de la categoría nueva: ")
        return opcion_seleccionada
    elif teclado == 5:
        opcion_seleccionada = input(f"Elige el nombre de la receta nueva: ")
        return opcion_seleccionada
    elif teclado == 6:
        opcion_seleccionada = input(f"\n\nPulse cualquier tecla para continuar... ")
        system("cls")
        bienvenida()
        return opcion_seleccionada

def es_directorio_vacio(ruta):
    directorio = os.listdir(ruta)

    if len(directorio) == 0:
        return True

    return False

def es_directorio_existente(ruta):
    if ruta.exists() and ruta.is_dir():
        return True

    return False

def acceder_a_recetas ():
    ruta_recetas = bienvenida()
    opcion_seleccionada = elegir_opcion(1,ruta_recetas)

    while opcion_seleccionada != '6':
        # ---------------- LEER RECETA ---------------- #
        if opcion_seleccionada == '1':
            categoria_seleccionada = elegir_opcion(2,ruta_recetas)
            ruta_buscar = ruta_recetas / categoria_seleccionada

            if es_directorio_existente(ruta_buscar):
                if es_directorio_vacio(ruta_buscar):
                    print("No hay recetas en la categoría seleccionada para leer")
                else:
                    receta_elegida = elegir_opcion(3,ruta_buscar) + ".txt"
                    fichero = ruta_buscar / receta_elegida

                    if fichero.exists():
                        receta = open(Path(fichero),'r')
                        print(receta.read())
                        receta.close()
                    else:
                        print("No existe la receta elegida")
            else:
                print("No existe la categoría elegida.")
        # ---------------- CREAR RECETA ---------------- #
        elif opcion_seleccionada == '2':
            categoria_seleccionada = elegir_opcion(2, ruta_recetas)
            ruta_buscar = ruta_recetas / categoria_seleccionada

            if es_directorio_existente(ruta_buscar):
                receta_elegida = elegir_opcion(5, ruta_buscar) + ".txt"
                fichero = ruta_buscar / receta_elegida

                if fichero.exists():
                    print("Ya existe la receta elegida y se va a sobreescribir")
                    texto = input("Indica los pasos a seguir para realizar la receta:\n")
                    receta = open(fichero,'w')
                    receta.write(texto)
                    receta.close()
                    print("¡¡¡¡Receta modificada correctamente!!!!")
                else:
                    texto = input("Indica los pasos a seguir para realizar la receta:\n")
                    receta = open(fichero, 'w')
                    receta.write(texto)
                    receta.close()
                    print("¡¡¡¡Receta creada correctamente!!!!")
            else:
                print("No existe la categoría elegida.")
        # ---------------- CREAR CATEGORIA ---------------- #
        elif opcion_seleccionada == '3':
            categoria_seleccionada = elegir_opcion(4,ruta_recetas)
            ruta_buscar = ruta_recetas / categoria_seleccionada

            if ruta_buscar.exists():
                print("No se puede crear la categoría porque ya existe")
            else:
                os.makedirs(ruta_buscar)
                print("Categoria creada correctamente")
        # ---------------- ELIMINAR RECETA ---------------- #
        elif opcion_seleccionada == '4':
            categoria_seleccionada = elegir_opcion(2, ruta_recetas)
            ruta_buscar = ruta_recetas / categoria_seleccionada

            if es_directorio_existente(ruta_buscar):
                if es_directorio_vacio(ruta_buscar):
                    print("La categoría no tiene recetas que se puedan eliminar")
                else:
                    receta_elegida = elegir_opcion(3, ruta_buscar) + ".txt"
                    fichero = ruta_buscar / receta_elegida

                    if fichero.exists():
                        os.remove(fichero)
                        print("Receta eliminada correctamente")
                    else:
                        print("No existe la receta elegida")
            else:
                print("No existe la categoría elegida.")
        # ---------------- ELIMINAR CATEGORIA ---------------- #
        else:
            categoria_seleccionada = elegir_opcion(2,ruta_recetas)
            ruta_buscar = ruta_recetas / categoria_seleccionada

            if es_directorio_existente(ruta_buscar):
                if es_directorio_vacio(ruta_buscar):
                    os.rmdir(ruta_buscar)
                    print("Categoría eliminada correctamente")
                else:
                    print("No se puede eliminar la categoría porque hay recetas incluidas")
            else:
                print("No existe la categoría elegida.")

        elegir_opcion(6, ruta_recetas)
        opcion_seleccionada = elegir_opcion(1,ruta_recetas)

    print("Gracias por su consulta. ¡Espero que nos volvamos a ver pronto!")

acceder_a_recetas()