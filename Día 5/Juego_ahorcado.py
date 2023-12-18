from random import choice


def elegir_palabra():
    """
    Devuelve la palabra que se tiene que adivinar
    :return: Devuelve la palabra elegida al azar dentro del listado dado
    """
    palabras = ['manzana', 'cuaderno', 'ordenador', 'cascarrabias',
                'pantalla', 'botella', 'miocardio', 'luciernaga']
    palabra_elegida = choice(palabras).lower()

    return palabra_elegida


def sustituir_palabra_con_guiones(palabra):
    """
    Devuelve la palabra elegida al azar sustituida por guiones
    :param palabra: palabra que se va a sustituir
    :return: palabra sustituida por guiones
    """
    palabra_oculta = []

    for letra in palabra:
        palabra_oculta.append("_")

    return palabra_oculta


def solicitar_letra():
    """
    Función que solicita al usuario la letra que se quiere adivinar.
    :return: Devuelve la letra elegida por el usuario
    """
    contador = 0

    while contador == 0:
        letra = input("Dime una letra: ").lower()
        if letra.isalpha() and len(letra) == 1:
            contador = 1

    return letra


def jugar_ahorcado():
    """
    Función para jugar al ahorcado hasta acertar la palabra o quedarse sin vidas.
    """
    print("*"*50)
    numero_vidas = 6
    letras_incorrectas = []
    palabra_elegida = elegir_palabra()
    palabra_oculta = sustituir_palabra_con_guiones(palabra_elegida)
    print(f"Número de vidas disponibles: {numero_vidas}\n")
    print(f"La palabra que hay que averiguar es:\n{''.join(palabra_oculta)}")
    print("*"*50)

    while (numero_vidas > 0) and ("_" in palabra_oculta):
        letra = solicitar_letra()
        if letra not in palabra_elegida:
            letras_incorrectas.append(letra)
            numero_vidas -= 1

            if numero_vidas == 0:
                print(f"¡¡¡LO SIENTO!!! Has perdido. La palabra oculta era '{palabra_elegida}'\n")
            else:
                print(f"NÚMERO DE VIDAS RESTANTES = {numero_vidas} ")
                print(f"Estas son las letras que has elegido incorrectamente: \n{'-'.join(letras_incorrectas)}\n")
        else:
            for indice, letra_usuario in enumerate(palabra_elegida):
                if letra_usuario == letra:
                    palabra_oculta[indice] = letra_usuario

            if "_" not in palabra_oculta:
                print(f"¡¡¡¡ENHORABUENA!!!! Has acertado la palabra oculta: {palabra_elegida}\n")
            else:
                print(f"La palabra oculta es: {''.join(palabra_oculta)}\n")


jugar_ahorcado()
