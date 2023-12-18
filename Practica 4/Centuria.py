from Contubernio import Contubernio
from Centurion import Centurion


class Centuria:

    def __init__(self):
        self.contubernios = []
        self.centurion = None

    def poblar(self):
        self.centurion = Centurion()

        for c in range(10):
            contubernio = Contubernio()
            contubernio.poblar()
            self.contubernios.append(contubernio)

    def obtener_soldados(self):
        numero_soldados = 0
        for c in self.contubernios:
            numero_soldados += c.obtener_soldados()

        return numero_soldados

    def obtener_oficiales(self):
        numero_oficiales = 0
        if self.centurion:
            numero_oficiales += 1

        for c in self.contubernios:
            numero_oficiales += c.obtener_oficiales()

        return numero_oficiales
