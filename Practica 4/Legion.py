from Cohorte import Cohorte
from Comandante import Comandante


class Legion:

    def __init__(self):
        self.comandante = None
        self.campamento = None
        self.cohortes = []

    def poblar(self):
        self.comandante = Comandante()
        self.comandante.establecer_identificador(f"#1")

        for c in range(10):
            cohorte = Cohorte()
            cohorte.establecer_identificador(f"#{c + 1}")
            cohorte.poblar()
            cohorte.tribuno.establecer_identificador(f"#{c + 1}")
            self.cohortes.append(cohorte)

    def obtener_numero_soldados(self):
        numero_soldados = 0
        for c in self.cohortes:
            numero_soldados += c.obtener_numero_soldados()

        return numero_soldados

    def obtener_numero_oficiales(self):
        numero_oficiales = 0
        if self.comandante:
            numero_oficiales += 1

        for c in self.cohortes:
            numero_oficiales += c.obtener_numero_oficiales()

        return numero_oficiales

    def establecer_campamento(self, campamento):
        self.campamento = campamento

    def obtener_unidades(self):
        lista_unidades = [self.comandante]

        for c in self.cohortes:
            lista_unidades.extend(c.obtener_unidades())

        return lista_unidades

    def establecer_armamento(self):
        if self.campamento:
            unidades = self.obtener_unidades()

            for u in unidades:
                self.campamento.obtener_armeria().pedir_arma_por_tipo(u)
        else:
            print("No pueden armarse sus tropas porque la legión no está asentada en ningún campamento")
