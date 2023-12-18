from Optione import Optione
from Soldado import Soldado


class Contubernio:

    def __init__(self):
        self.soldados = []
        self.optione = None

    def poblar(self):
        self.optione = Optione()

        for s in range(8):
            self.soldados.append(Soldado())

    def obtener_soldados(self):
        return len(self.soldados)

    def obtener_oficiales(self):
        if self.optione:
            return 1
