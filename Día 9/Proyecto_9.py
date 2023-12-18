import os
import re
from datetime import date
import time
import math

carpeta_principal = os.getcwd() + '\\Proyecto_Instrucciones\\Mi_Gran_Directorio'


def devolver_patron_encontrado(texto):
    patron = r'[N]\w{3}[-]\d{5}'
    encontrado = re.search(patron, texto)
    numero_serie_encontrado = ""

    if encontrado:
        inicio_patron = encontrado.start()
        fin_patron = encontrado.end()
        numero_serie_encontrado = texto[inicio_patron:fin_patron]

    return numero_serie_encontrado


def buscar_numero_serie():
    contador = 0
    fecha_hoy = date.today().strftime("%d/%m/%Y")
    print('-'*50)
    print(f"Fecha de búsqueda: {fecha_hoy}\n")
    print("ARCHIVO\t\t\t\tNRO. SERIE")
    print("-------\t\t\t\t----------")

    inicio = time.time()

    for ruta, subcarpetas, archivos in os.walk(carpeta_principal):
        for archivo in archivos:
            ruta_fichero = f"{ruta}\\{archivo}"
            archivo_abierto = open(ruta_fichero)

            for linea in archivo_abierto.readlines():
                numero_serie = devolver_patron_encontrado(linea)

                if numero_serie != "":
                    contador += 1
                    print(f"{archivo}\t\t{numero_serie}")

            archivo_abierto.close()

    fin = time.time()

    print(f"\nNúmeros encontrados: {contador}")
    print(f"Duración de la búsqueda: {math.ceil(fin-inicio)} segundos")
    print('-'*50)


buscar_numero_serie()
