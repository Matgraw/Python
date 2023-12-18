from random import *
print("-------------------------------------------------------------")
aleatorio = randint(1,50)
print(aleatorio)

aleatorio = round(uniform(1,5),2)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['azul','rojo','verde','amarillo']
aleatorio = choice(colores)
print(aleatorio)

numeros = list (range(5,50,5))
shuffle(numeros)
print(numeros)