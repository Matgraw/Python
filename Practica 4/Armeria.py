from Arco import Arco
from Pilum import Pilum
from Gladio import Gladio
from Escudo import Escudo
import random


class Armeria:
    total_arcos = 2500
    total_pilum = 3000
    total_gladios = 2000
    total_escudos = 5800

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
        self.armas.append(arma)

    def recibir_cargamento(self, armas):
        for a in armas:
            self.armas.append(a)

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
            else:
                total_escudos += 1

        print(f"Obteniendo número de armas exitentes en la armería...")
        print(f"- {total_gladios} gladios")
        print(f"- {total_pilums} pilums")
        print(f"- {total_arcos} arcos")
        print(f"- {total_escudos} escudos")

    def pedir_arma_por_tipo(self, militar, tipo_arma=None):
        arma_principal = None
        gladios = [arma for arma in self.armas if type(arma).__name__ == "Gladio"]
        escudos = [arma for arma in self.armas if type(arma).__name__ == "Escudo"]

        # Si hay armas en la armería, se empiezan las comprobaciones para armar a los militares
        if len(self.armas) > 0:
            # Si se ha rellenado el tipo de arma
            if tipo_arma:
                # Si el tipo de arma es uno de los permitidos
                if tipo_arma in ['Arco', 'Escudo', 'Gladio', 'Pilum']:
                    armas_por_tipo = [arma for arma in self.armas if type(arma).__name__ == tipo_arma]

                    # Si el militar que pide el arma es un oficial
                    if type(militar).__name__ in ['Comandante', 'Centurion', 'Tribuno', 'Optione']:
                        # Si el tipo de arma es un Gladio
                        if tipo_arma == 'Gladio':
                            # Se coge el primer Gladio de la lista de armas.
                            arma_principal = random.choice(armas_por_tipo)
                    # Si el militar que pide el arma es un soldado de infanteria
                    elif type(militar).__name__ == 'Infanteria':
                        # Se elige el primer Escudo de la lista de armas
                        arma_secundaria = random.choice(escudos)
                        # si se ha encontrado el arma se le asigna al soldado
                        if arma_secundaria:
                            militar.establecer_arma(arma_secundaria)
                            self.armas.remove(arma_secundaria)
                        # Se elige el primer arma del tipo elegido
                        arma_principal = random.choice(armas_por_tipo)
                    # Si el militar que pide el arma es un soldado
                    else:
                        # Se elige el primer arma del tipo elegido
                        arma_principal = random.choice(armas_por_tipo)
            # Si no se ha rellenado el tipo de arma, se asigna un Gladio de manera aleatoria
            else:
                # Si el militar es oficial, se le asigna un Gladio
                if type(militar).__name__ in ['Comandante', 'Centurion', 'Tribuno', 'Optione']:
                    # Se coge el primer Gladio de la lista de armas.
                    arma_principal = random.choice(gladios)
                # Si el militar que pide el arma es un soldado de infanteria
                elif type(militar).__name__ == 'Infanteria':
                    # Se elige el primer Escudo de la lista de armas
                    arma_secundaria = random.choice(escudos)
                    # si se ha encontrado el arma se le asigna al soldado
                    if arma_secundaria:
                        militar.establecer_arma(arma_secundaria)
                        self.armas.remove(arma_secundaria)
                    # Se coge el primer arma de la lista de armas.
                    arma_principal = random.choice(self.armas)
                # Si el militar es un soldado, se le asigna un arma aleatoria
                else:
                    # Se coge el primer arma de la lista de armas.
                    arma_principal = random.choice(self.armas)

            # Asignar el arma principal a cada militar
            if arma_principal:
                militar.establecer_arma(arma_principal)
                self.armas.remove(arma_principal)
