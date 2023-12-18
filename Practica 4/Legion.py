from Cohorte import Cohorte
from Comandante import Comandante


class Legion:

    def __init__(self):
        self.cohortes = []
        self.comandante = None
        self.campamento = None

    def poblar(self):
        self.comandante = Comandante()

        for c in range(10):
            cohorte = Cohorte()
            cohorte.poblar()
            self.cohortes.append(cohorte)

    def obtener_soldados(self):
        numero_soldados = 0
        for c in self.cohortes:
            numero_soldados += c.obtener_soldados()

        return numero_soldados

    def obtener_oficiales(self):
        numero_oficiales = 0
        if self.comandante:
            numero_oficiales += 1

        for c in self.cohortes:
            numero_oficiales += c.obtener_oficiales()

        return numero_oficiales

    def establecer_campamento(self, campamento):
        self.campamento = campamento
