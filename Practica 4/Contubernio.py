from Optione import Optione
from Infanteria import Infanteria
from Caballeria import Caballeria
from random import *


class Contubernio:

    def __init__(self):
        self.identificador = ""
        self.optione = None
        self.soldados = []

    def poblar(self):
        self.optione = Optione()

        for s in range(8):
            tipo_soldado = randint(1, 2)
            if tipo_soldado == 1:
                soldado = Infanteria()
                soldado.establecer_identificador(f"#{s+1}")
                self.soldados.append(soldado)
            else:
                soldado = Caballeria()
                soldado.establecer_identificador(f"#{s+1}")
                self.soldados.append(soldado)

    def obtener_numero_soldados(self):
        return len(self.soldados)

    def obtener_numero_oficiales(self):
        if self.optione:
            return 1

    def establecer_identificador(self, identificador):
        self.identificador = identificador

    def obtener_unidades(self):
        lista_unidades = [self.optione]

        for s in self.soldados:
            lista_unidades.append(s)

        return lista_unidades
