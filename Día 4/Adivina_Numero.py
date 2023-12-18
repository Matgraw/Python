from random import randint

nombre = input("Dime tu nombre: ")
print()
print(f"Hola {nombre}, he pensado un número entre el 1 y el 100 y tienes\n"
      f"ocho intentos para adivinarlo. ¡Vamos allá!")
print()

# Numero aleatorio que hay que adivinar
numero_maquina = randint(1,100)
# Numero de intentos del usuario
numero_intentos = 1

while numero_intentos < 9:
    numero_usuario = int(input(f"Número elegido en el intento {numero_intentos}: "))

    # Numeros no validos
    if (numero_usuario < 1) or (numero_usuario > 100):
        print("El número elegido no está permitido")
    # Numero menor que el secreto
    elif numero_usuario < numero_maquina:
        print("El número elegido es menor que el número secreto")
    # Numero mayor que el secreto
    elif numero_usuario > numero_maquina:
        print("El número elegido es mayor que el número secreto")
    # Numero correcto y se sale del programa
    else:
        print()
        print(f"¡¡¡HAS GANADO!!! El número secreto era el {numero_maquina} y lo has acertado en {numero_intentos} intentos")
        break

    numero_intentos += 1
else:
    print()
    print(f"¡¡¡HAS PERDIDO!!! El número secreto era el {numero_maquina}")