lista = ['a','b','c','d']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra: {numero_letra}: "+ letra)
print("-------------------------------------------------------------")
lista_nombres = ['Pablo','Laura','Fede','Luis','Julia']
for nombre in lista_nombres:
    if nombre.startswith('L'):
        print(nombre)
    else:
        print("Nombre que no comienza con L")

print("-------------------------------------------------------------")
numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(f"Valor parcial de la suma = {mi_valor}")

print(f"Valor final de la suma = {mi_valor}")

print("-------------------------------------------------------------")
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

print("-------------------------------------------------------------")
diccionario = {'clave1':'a','clave2':'b','clave3':'c'}
for item in diccionario:
    print(item)
for item in diccionario.items():
    print(item)
for item in diccionario.values():
    print(item)