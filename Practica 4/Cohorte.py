from Centuria import Centuria
from Tribuno import Tribuno


class Cohorte:

    def __init__(self):
        self.identificador = ""
        self.tribuno = None
        self.centurias = []

    def poblar(self):
        self.tribuno = Tribuno()

        for c in range(6):
            centuria = Centuria()
            centuria.establecer_identificador(f"#{c + 1}")
            centuria.poblar()
            centuria.centurion.establecer_identificador(f"#{c + 1}")
            self.centurias.append(centuria)

    def obtener_numero_soldados(self):
        numero_soldados = 0
        for c in self.centurias:
            numero_soldados += c.obtener_numero_soldados()

        return numero_soldados

    def obtener_numero_oficiales(self):
        numero_oficiales = 0
        if self.tribuno:
            numero_oficiales += 1

        for c in self.centurias:
            numero_oficiales += c.obtener_numero_oficiales()

        return numero_oficiales

    def establecer_identificador(self, identificador):
        self.identificador = identificador

    def obtener_unidades(self):
        lista_unidades = [self.tribuno]

        for c in self.centurias:
            lista_unidades.extend(c.obtener_unidades())

        return lista_unidades
