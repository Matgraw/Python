def es_numero_primo(n):
    """
    Función para saber si un numero es primo
    :param n: numero al que hay que indicar si es primo
    :return: devuelve true si es un numero primo o false si no lo es
    """
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

def contar_primos(numero_limite):
    """
    Funcion para obtener la cantidad de numeros primos que hay en una lista
    :param numero_limite: numero limite para obtener los primos hasta ese rango
    :return: devuelve la cantidad de numeros primos que hay
    """
    lista_numeros = list(range(0,numero_limite))
    cantidad = 0

    for n in lista_numeros:
        if es_numero_primo(n):
            cantidad += 1

    return cantidad


print(contar_primos(10))

