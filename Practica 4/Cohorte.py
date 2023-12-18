from Centuria import Centuria
from Tribuno import Tribuno


class Cohorte:

    def __init__(self):
        self.centurias = []
        self.tribuno = None

    def poblar(self):
        self.tribuno = Tribuno()

        for c in range(6):
            centuria = Centuria()
            centuria.poblar()
            self.centurias.append(centuria)

    def obtener_soldados(self):
        numero_soldados = 0
        for c in self.centurias:
            numero_soldados += c.obtener_soldados()

        return numero_soldados

    def obtener_oficiales(self):
        numero_oficiales = 0
        if self.tribuno:
            numero_oficiales += 1

        for c in self.centurias:
            numero_oficiales += c.obtener_oficiales()

        return numero_oficiales
