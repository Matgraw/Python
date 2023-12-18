def saludar_persona(nombre):
    """
    Esta funcion sirve para saludar a las personas
    """
    print("Hola "+ nombre)

saludar_persona("Miguel")
saludar_persona("Javier")
print("-------------------------------------------------------------")
def multiplicar(numero1, numero2):
    total = numero1 * numero2
    return total

resultado = multiplicar(54,351)
print(resultado)
print("-------------------------------------------------------------")
def chequear_3_cifras(lista):

    lista_3_cifras =[]

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras

resultado = chequear_3_cifras([555,99,600])
print(resultado)
print("-------------------------------------------------------------")
precios_cafe = [('Capuchino',1.5),('Expresso',2.5),('Moka',1.9)]

def cafe_mas_caro (lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ""

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe

    return cafe_mas_caro, precio_mayor

cafe,precio = cafe_mas_caro(precios_cafe)
print(f"El café más caro es {cafe} cuyo precio es {precio}")
print("-------------------------------------------------------------")
from random import shuffle
# Lista inicial
palitos = ['-','--','---','----']

# Mezclar palitos
def mezclar (lista):
    shuffle(lista)
    return lista

# Pedirle intento
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input("Elige un número del 1 al 4: ")

    return int(intento)

# Comprobar intento
def comprobar_intento(lista,intento):
    if lista[intento-1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")

    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
comprobar_intento(palitos_mezclados,seleccion)

print("-------------------------------------------------------------")
def suma(*args):
    return sum(args)

print(suma(5,5,6,7,5023))
print("-------------------------------------------------------------")
def suma_multiple(**kwargs):
    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor

    return total


print(suma_multiple(a=5,b=5,c=6,d=7,e=5023))
print("-------------------------------------------------------------")
def suma_multiple_nueva(num1, num2, *args, **kwargs):
    total = 0

    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        #total += valor

    #return total


suma_multiple_nueva(9,5,4,3,6,8,a=5,b=5,c=6,d=7,e=5023)