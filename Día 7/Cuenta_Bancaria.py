import random

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente (Persona):
    def __init__(self,nombre, apellido,numero_cuenta,saldo):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def __str__(self):
        return f"Nombre del cliente: {self.nombre} {self.apellido}\nNúmero de cuenta: {self.numero_cuenta}\nSaldo: {self.saldo}€"

    def ingresar(self,dinero):
        self.saldo = self.saldo + dinero

    def retirar(self, dinero):
        if self.saldo == 0:
            print("No tienes dinero en la cuenta. Ingrese dinero antes de retirarlo")
        elif dinero > self.saldo:
            print("No puedes retirar más dinero del que hay en la cuenta")
        else:
            self.saldo = self.saldo - dinero

def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    saldo = 0.0
    numero_cuenta = f"ES13 {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(1000,9999)}"
    cliente_nuevo = Cliente(nombre,apellido,numero_cuenta,saldo)

    return cliente_nuevo

def inicio():
    cliente = crear_cliente()
    print('*' * 50)
    print(cliente)
    opcion_cliente = "0"

    while opcion_cliente != "3":
        print('*' * 50)
        print("Indique que quiere hacer: ")
        print("[1] - Ingresar dinero. ")
        print("[2] - Retirar dinero. ")
        print("[3] - Salir. ")
        print('*' * 50)
        opcion_cliente = input("Indique que desea realizar: ")

        if opcion_cliente.isnumeric():
            if opcion_cliente not in ("1","2","3"):
                print("No es una opción válida. Vuelve a intentarlo")
            else:
                if opcion_cliente == "1":
                    dinero = float(input("Indique la cantidad a ingresar: "))
                    cliente.ingresar(dinero)
                elif opcion_cliente == "2":
                    dinero = float(input("Indique la cantidad a retirar: "))
                    cliente.retirar(dinero)
        else:
            print("No es una opción válida. Vuelve a intentarlo")

        print('*' * 50)
        print(cliente)

    print("Gracias por su visita. ¡Vuelva pronto!")

inicio()