##### Ejemplos de utilización de conversiones entre tipos de datos #####
print("#############################################################")
num1 = 20
num2 = 30.5
print(type(num1))
num1 = num1 + num2 # Conversion implicita
print(type(num1))
print(type(num2))

num1 = 5.8
print(num1)
print(type(num1))
num2 = int(num1)
print(num2)
print(type(num2))

edad = input("Dime tu edad: ")
print(type(edad))
edad = int(edad)
print(type(edad))
nueva_edad = 1 + edad
print(f"Vas a cumplir {nueva_edad} años")

x = 10
y = 5
print("La suma de {} y {} es igual a {}".format(x,y,x+y))

color = "rojo"
matricula = 7693
print(f"El auto es {color} y su matricula es {matricula}")