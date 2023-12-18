##### Ejemplos de utilización de integer y float #####
print("#############################################################")
mi_numero = 1
print(mi_numero)
print(type(mi_numero))
mi_numero = 1 + 3
print(mi_numero + mi_numero)
print(type(mi_numero))
mi_numero = 5.8
print(mi_numero)
print(type(mi_numero))
mi_numero = 5 + 5.8
print(mi_numero)
print(type(mi_numero))
num1 = 7.5
num2 = 2.5
num_total = num1 + num2
print(num_total)
print(type(num1 + num2))
edad = input("Dime tu edad: ") # Los input por pantalla siempre son string
print("Tu edad es "+ edad)
nueva_edad = 1 + edad # Da error porque no se puede sumar integer con string
print("Vas a cumplir "+ nueva_edad)