from Optione import Optione
from Infanteria import Infanteria
from Caballeria import Caballeria
from random import *


class Contubernio:

    def __init__(self):
        self.soldados = []
        self.optione = None

    def poblar(self):
        self.optione = Optione()

        for s in range(8):
            tipo_soldado = randint(1, 2)
            if tipo_soldado == 1:
                self.soldados.append(Infanteria())
            else:
                self.soldados.append(Caballeria())

    def obtener_soldados(self):
        return len(self.soldados)

    def obtener_oficiales(self):
        if self.optione:
            return 1
