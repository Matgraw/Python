from Contubernio import Contubernio
from Centurion import Centurion


class Centuria:

    def __init__(self):
        self.identificador = ""
        self.centurion = None
        self.contubernios = []

    def poblar(self):
        self.centurion = Centurion()

        for c in range(10):
            contubernio = Contubernio()
            contubernio.establecer_identificador(f"#{c+1}")
            contubernio.poblar()
            contubernio.optione.establecer_identificador(f"#{c + 1}")
            self.contubernios.append(contubernio)

    def obtener_numero_soldados(self):
        numero_soldados = 0
        for c in self.contubernios:
            numero_soldados += c.obtener_numero_soldados()

        return numero_soldados

    def obtener_numero_oficiales(self):
        numero_oficiales = 0
        if self.centurion:
            numero_oficiales += 1

        for c in self.contubernios:
            numero_oficiales += c.obtener_numero_oficiales()

        return numero_oficiales

    def establecer_identificador(self, identificador):
        self.identificador = identificador

    def obtener_unidades(self):
        lista_unidades = [self.centurion]

        for c in self.contubernios:
            lista_unidades.extend(c.obtener_unidades())

        return lista_unidades
