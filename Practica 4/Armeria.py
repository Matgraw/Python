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
            else:
                total_escudos += 1

        print(f"Obteniendo número de armas exitentes en la armería...")
        print(f"- {total_gladios} gladios")
        print(f"- {total_pilums} pilums")
        print(f"- {total_arcos} arcos")
        print(f"- {total_escudos} escudos")

    def pedir_arma_por_tipo(self, militar, tipo_arma=None):
        # Si hay armas en el amacen, se empiezan las comprobaciones para armar a los militares
        if len(self.armas) > 0:
            # Si se ha rellenado el tipo de arma
            if tipo_arma:
                # Si el tipo de arma es uno de los permitidos
                if tipo_arma in ['Arco', 'Escudo', 'Gladio', 'Pilum']:
                    # Si el militar que pide el arma es un oficial
                    if type(militar).__name__ in ['Comandante', 'Centurion', 'Tribuno', 'Optione']:
                        # Si el tipo de arma es un Gladio
                        if tipo_arma == 'Gladio':
                            # Se coge el primer Gladio de la lista de armas.
                            arma_elegida = next((arma for arma in self.armas if type(arma).__name__ == tipo_arma), None)
                            # Si se ha encontrado el arma, se le asigna al oficial
                            if arma_elegida:
                                militar.establecer_arma(arma_elegida)
                                self.armas.remove(arma_elegida)
                            # Si no se ha encontrado es que no quedan Gladios en la armaría
                            else:
                                print(f"{type(militar).__name__} {militar.identificador} no quedan armas de tipo {tipo_arma} en la armeria.")
                        # Si no es un Gladio no se le permite armarse
                        else:
                            print(f"{type(militar).__name__} {militar.identificador} eres un oficial y sólo puedes armarte con Gladios")
                    # Si el militar que pide el arma es un soldado de infanteria
                    elif type(militar).__name__ == 'Infanteria':
                        # Se elige el primer arma del tipo elegido
                        arma_elegida = next((arma for arma in self.armas if type(arma).__name__ == tipo_arma), None)
                        # si se ha encontrado el arma se le asigna al soldado
                        if arma_elegida:
                            militar.establecer_arma(arma_elegida)
                            self.armas.remove(arma_elegida)
                        # Si no se ha encontrado es que no quedan armas del tipo elegido
                        else:
                            print(f"{type(militar).__name__} {militar.identificador} no quedan armas de tipo {tipo_arma} en la armeria.")

                        # Se elige el primer Escudo de la lista de armas
                        arma_elegida = next((arma for arma in self.armas if type(arma).__name__ == 'Escudo'), None)
                        # si se ha encontrado el arma se le asigna al soldado
                        if arma_elegida:
                            militar.establecer_arma(arma_elegida)
                            self.armas.remove(arma_elegida)
                        # Si no se ha encontrado es que no quedan armas del tipo elegido
                        else:
                            print(f"{type(militar).__name__} {militar.identificador} no quedan Escudos en la armeria.")
                    # Si el militar que pide el arma es un soldado
                    else:
                        # Se elige el primer arma del tipo elegido
                        arma_elegida = next((arma for arma in self.armas if type(arma).__name__ == tipo_arma), None)
                        # si se ha encontrado el arma se le asigna al soldado
                        if arma_elegida:
                            militar.establecer_arma(arma_elegida)
                            self.armas.remove(arma_elegida)
                        # Si no se ha encontrado es que no quedan armas del tipo elegido
                        else:
                            print(f"{type(militar).__name__} {militar.identificador} no quedan armas de tipo {tipo_arma} en la armeria.")
                # Si no es un arma de los tipos permitidos
                else:
                    print(f"{type(militar).__name__} {militar.identificador} no existen armas del tipo {tipo_arma}")
            # Si no se ha rellenado el tipo de arma, se asigna un Gladio de manera aleatoria
            else:
                # Si el militar es oficial, se le asigna un Gladio
                if type(militar).__name__ in ['Comandante', 'Centurion', 'Tribuno', 'Optione']:
                    # Se coge el primer Gladio de la lista de armas.
                    arma_elegida = next((arma for arma in self.armas if type(arma).__name__ == 'Gladio'), None)
                    # si se ha encontrado el arma se le asigna al oficial
                    if arma_elegida:
                        militar.establecer_arma(arma_elegida)
                        self.armas.remove(arma_elegida)
                    # Si no se ha encontrado es que no quedan armas del tipo elegido
                    else:
                        print(f"{type(militar).__name__} {militar.identificador} no quedan gladios en la armeria.")
                        # Si el militar que pide el arma es un soldado de infanteria
                elif type(militar).__name__ == 'Infanteria':
                    # Se coge el primer arma de la lista de armas.
                    arma_elegida = random.choice(self.armas)
                    # si se ha encontrado el arma se le asigna al soldado
                    if arma_elegida:
                        militar.establecer_arma(arma_elegida)
                        self.armas.remove(arma_elegida)
                    # Si no se ha encontrado es que no quedan armas del tipo elegido
                    else:
                        print(f"{type(militar).__name__} {militar.identificador} no quedan armas en la armeria.")

                    # Se elige el primer Escudo de la lista de armas
                    arma_elegida = next((arma for arma in self.armas if type(arma).__name__ == 'Escudo'), None)
                    # si se ha encontrado el arma se le asigna al soldado
                    if arma_elegida:
                        militar.establecer_arma(arma_elegida)
                        self.armas.remove(arma_elegida)
                    # Si no se ha encontrado es que no quedan armas del tipo elegido
                    else:
                        print(f"{type(militar).__name__} {militar.identificador} no quedan Escudos en la armeria.")
                # Si el militar es un soldado, se le asigna un arma aleatoria
                else:
                    # Se coge el primer arma de la lista de armas.
                    arma_elegida = random.choice(self.armas)
                    # si se ha encontrado el arma se le asigna al soldado
                    if arma_elegida:
                        militar.establecer_arma(arma_elegida)
                        self.armas.remove(arma_elegida)
                    # Si no se ha encontrado es que no quedan armas del tipo elegido
                    else:
                        print(f"{type(militar).__name__} {militar.identificador} no quedan armas en la armeria.")
        # Si no quedan armas en la armeria
        else:
            print(f"{type(militar).__name__} {militar.identificador} no quedan armas en la armeria")
