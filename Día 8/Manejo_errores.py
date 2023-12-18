def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un número: "))
        except:
            print("Ese no es número")
        else:
            print(f"El número introducido es {numero}")
            break

    print("Gracias")

pedir_numero()

def suma():
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    print(n1+n2)
    print("Gracias por sumar" + n1)

try:
    # codigo que queremos probar
    suma()
except TypeError:
    #codigo a ejecutar si no hay un error
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un número")
else:
    #codigo adicional si no hay error
    print("Hiciste todo bien")
finally:
    #codigo que se va a ejecutar de todos modos
    print("Eso fue todo")