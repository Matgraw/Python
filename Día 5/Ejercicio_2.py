def letras_unicas(palabra):
    """
    Devuelve las letras unicas de una palabra ordenadas alfabeticamente
    :param palabra: palabra a analizar
    :return: devuelve una lista con las letras unicas ordenada alfabeticamente
    """
    palabra = palabra.lower()
    lista_devuelta = []

    for letra in palabra:
        if letra not in lista_devuelta:
            lista_devuelta.append(letra)

    lista_devuelta.sort()

    return lista_devuelta

print(letras_unicas("cascarrabias"))