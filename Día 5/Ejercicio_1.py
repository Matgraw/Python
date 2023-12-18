def devolver_distintos(num1, num2, num3):
    """
    Funcion que devuelve el numero en funcion de condiciones
    :param num1: numero 1
    :param num2: numero 2
    :param num3: numero 3
    :return: devuelve el numero correspondiente segun las condiciones
    """

    lista_numeros = [num1, num2, num3]
    suma = num1 + num2 + num3

    if suma > 15:
        return max(lista_numeros)
    elif suma < 10:
        return min(lista_numeros)
    else:
        lista_numeros.sort
        return lista_numeros[1]

print(devolver_distintos(2,5,9))