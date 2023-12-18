from Arco import Arco
from Pilum import Pilum
from Gladio import Gladio
from Escudo import Escudo


class Armeria:
    total_arcos = 2500
    total_pilum = 3000
    total_gladios = 2000
    total_escudos = 1800

    def __init__(self):
        self.armas = []

        for a in range(self.total_arcos):
            self.armas.append(Arco())

        for a in range(self.total_pilum):
            self.armas.append(Pilum())

        for a in range(self.total_gladios):
            self.armas.append(Gladio())

        for a in range(self.total_escudos):
            self.armas.append(Escudo())

    def devolver_arma(self, arma):
        print("*" * 50)
        print("Devolviendo arma a la armería...")
        self.armas.append(arma)
        print("Arma devuelta correctamente!!!!")

    def recibir_cargamento(self, armas):
        print("*"*50)
        print("Recibiendo cargamento de armas...")
        for a in armas:
            self.armas.append(a)
        print("Armería cargada correctamente!!!!")

    def hacer_inventario(self):
        print("*" * 50)
        total_gladios = 0
        total_pilums = 0
        total_arcos = 0
        total_escudos = 0
        for arma in self.armas:
            tipo_arma = type(arma).__name__
            if tipo_arma == "Gladio":
                total_gladios += 1
            elif tipo_arma == "Pilum":
                total_pilums += 1
            elif tipo_arma == "Arco":
                total_arcos += 1
            else :
                total_escudos += 1

        print(f"Obteniendo número de armas exitentes en la armería...")
        print(f"- {total_gladios} gladios")
        print(f"- {total_pilums} pilums")
        print(f"- {total_arcos} arcos")
        print(f"- {total_escudos} escudos")

