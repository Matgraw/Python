from Coche import Coche
from Rueda import Rueda
from Asiento import Asiento
from Motor import Motor
from Mecanico import Mecanico
from random import *

# Iniciación de variables para la creación de los coches según el elegido
coche_seleccionado = 0
tipo_coche_seleccionado = ""
tipo_ruedas = ""
tipo_asientos = ""
cilindrada = 0
caballos = 0
tipo_carburante = ""
tipo_motor = ""
numero_ruedas = 0
numero_asientos = 0

print('*'*50)
print("[1] - Coche Normalito")
print("[2] - Coche Deportivo")
print("[3] - Coche Ahorro")
print("")
while coche_seleccionado not in (1, 2, 3):
    try:
        coche_seleccionado = int(input("Seleccione uno de los tipos de coche: "))
    except ValueError:
        print("Ese no es número de los permitidos")
    else:
        if coche_seleccionado not in (1, 2, 3):
            print("No es un tipo de coche válido")
        else:
            coche = Coche()

            if coche_seleccionado == 1:
                tipo_coche_seleccionado = "Coche Normalito"
                tipo_ruedas = "lisas"
                tipo_asientos = "cuero sintético"
                caballos = 150
                cilindrada = 1900
                tipo_carburante = "Diesel"
                tipo_motor = "Turbo Compresor"
                numero_ruedas = 4
                numero_asientos = 4

            elif coche_seleccionado == 2:
                tipo_coche_seleccionado = "Coche Deportivo"
                tipo_ruedas = "semilisas"
                tipo_asientos = "cuero"
                caballos = 490
                cilindrada = 3500
                tipo_carburante = "Gasolina"
                tipo_motor = "Compresor"
                numero_ruedas = 4
                numero_asientos = 4

            else:
                tipo_coche_seleccionado = "Coche Ahorro"
                tipo_ruedas = "rayadas"
                tipo_asientos = "nylon"
                caballos = 90
                cilindrada = 1400
                tipo_carburante = "Híbrido"
                tipo_motor = "Atmosférico"
                numero_ruedas = 4
                numero_asientos = 4

            # Asignar ruedas al coche
            for n in range(numero_ruedas):
                rueda = Rueda()
                rueda.establecer_tipo(tipo_ruedas)
                rueda.establecer_estado(randint(1, 10))
                coche.poner_rueda(n, rueda)

            # Asignar asientos al coche
            for n in range(numero_asientos):
                asiento = Asiento()
                asiento.establecer_tipo(tipo_asientos)
                asiento.establecer_estado(randint(1, 10))
                coche.poner_asiento(n, asiento)

            # Asignar motor al coche
            motor = Motor()
            motor.establecer_caballos(caballos)
            motor.establecer_cilindrada(cilindrada)
            motor.establecer_tipo(tipo_motor)
            motor.establecer_combustible(tipo_carburante)
            motor.establecer_estado(randint(1, 10))
            coche.poner_motor(motor)

            print('*' * 50)

            print(f"El coche elegido es: {tipo_coche_seleccionado}. Tiene las siguientes características")
            print(f"- {len(coche.ruedas)} ruedas {tipo_ruedas}")
            for r in coche.ruedas:
                print(f"-- La rueda {coche.ruedas.index(r)} está en estado {r.consultar_estado()}")
            print(f"- {len(coche.asientos)} asientos de {tipo_asientos}")
            for a in coche.asientos:
                print(f"-- El asiento {coche.asientos.index(a)} está en estado {a.consultar_estado()}")
            print(f"- Un motor de {cilindrada}cc, {caballos}CV, {tipo_carburante}, {tipo_motor} "
                  f"en estado {coche.motor.consultar_estado()}")

            print('*' * 50)

            # Llevamos el coche al taller para un diagnostico:
            Mecanico.diagnosticar(coche)
            Mecanico.reparar(coche)

            print('*' * 50)

            print(f"El coche elegido es: {tipo_coche_seleccionado}. Tiene las siguientes características")
            print(f"- {len(coche.ruedas)} ruedas {tipo_ruedas}")
            for r in coche.ruedas:
                print(f"-- La rueda {coche.ruedas.index(r)} está en estado {r.consultar_estado()}")
            print(f"- {len(coche.asientos)} asientos de {tipo_asientos}")
            for a in coche.asientos:
                print(f"-- El asiento {coche.asientos.index(a)} está en estado {a.consultar_estado()}")
            print(f"- Un motor de {cilindrada}cc, {caballos}CV, {tipo_carburante}, {tipo_motor} "
                  f"en estado {coche.motor.consultar_estado()}")

print('*'*50)
