from random import *
from Aula import Aula
from PuestoAlumno import PuestoAlumno
from PuestoProfesor import PuestoProfesor
from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado
from Proyector import Proyector
from Cpu import Cpu

# Identificadores que tendrán cada una de las aulas creadas
lista_identificador_aula = ["A", "B", "C"]
lista_aulas = []

# Por cada identificador crear un aula nueva y asociarlo a ella
for i in lista_identificador_aula:
    aula_nueva = Aula()
    # numero de puestos que tendra el aula
    numero_puestos = randint(5, 15)
    # se establece el identificador del aula
    aula_nueva.establecer_identificador(i)
    # se crean el numero de puesto que va a tener el aula
    for n in range(numero_puestos):
        # el primero puesto siempre es el del profesor
        if n == 0:
            puesto_nuevo = PuestoProfesor()
            puesto_nuevo.establecer_proyector(Proyector())
            puesto_nuevo.establecer_cpu(Cpu())
        else:
            puesto_nuevo = PuestoAlumno()
            puesto_nuevo.establecer_cpu(Cpu())
            puesto_nuevo.establecer_cpu(Cpu())

        # por cada puesto hay que crear sus elementos
        puesto_nuevo.establecer_monitor(Monitor())
        puesto_nuevo.establecer_raton(Raton())
        puesto_nuevo.establecer_teclado(Teclado())
        # se establece el estado de cada uno de los aparatos del puesto
        for a in puesto_nuevo.aparatos:
            averiado = randint(1, 20)
            if averiado <= 3:
                a.establecer_averiado(True)
            else:
                a.establecer_averiado(False)
        # se establece el identificador del aula
        puesto_nuevo.establecer_identificador(n)
        # se añaden los puestos al aula
        aula_nueva.establecer_puesto(puesto_nuevo)

    # se añade el aula a la lista de aulas existentes
    lista_aulas.append(aula_nueva)

for a in lista_aulas:
    print(f"Aula {a.identificador} con {len(a.puestos)} puestos")
    a.encender_apagar()
    a.obtener_puestos_defectuosos()
    a.encender_apagar()
