from Venda import Venda
from Paquete import Paquete
import random


class Hospital:
    total_vendas = 25000
    total_paquetes = 30000

    def __init__(self):
        self.materiales_hospital = []

        for a in range(self.total_vendas):
            self.materiales_hospital.append(Venda())

        for a in range(self.total_paquetes):
            self.materiales_hospital.append(Paquete())

    def recibir_cargamento(self, materiales):
        for m in materiales:
            self.materiales_hospital.append(m)

    def hacer_inventario(self):
        print("*" * 50)
        total_vendas = 0
        total_paquetes = 0
        for material in self.materiales_hospital:
            tipo_material = type(material).__name__
            if tipo_material == "Venda":
                total_vendas += 1
            else:
                total_paquetes += 1

        print(f"Obteniendo número de materiales exitentes en el hospital...")
        print(f"- {total_vendas} vendas")
        print(f"- {total_paquetes} paquetes")

    def curar(self, militar):
        material_curar = None
        vendas = [material for material in self.materiales_hospital if material == "Venda"]
        paquetes = [material for material in self.materiales_hospital if material == "Paquete"]

        # Si hay material en el hospital, se empiezan las comprobaciones para curar a los militares
        if len(self.materiales_hospital) > 0:
            # Si se trata de un oficial, que tiene 100 puntos de salud
            if type(militar).__name__ in ['Comandante', 'Centurion', 'Tribuno', 'Optione']:
                puntos_vida_maximo = 100

                # Si tiene la salud al completo no tiene sentido curarse.
                if puntos_vida_maximo > militar.puntos_vida >= puntos_vida_maximo - 30:
                    material_curar = random.choice(vendas)
                # Si ha bajado mas de 30 puntos, se usa un paquete:
                elif militar.puntos_vida < puntos_vida_maximo - 30:
                    material_curar = random.choice(paquetes)
            # Si el militar es un soldado, se le asigna un arma aleatoria
            else:
                puntos_vida_maximo = 150

                # Si tiene la salud al completo no tiene sentido curarse.
                if puntos_vida_maximo > militar.puntos_vida >= puntos_vida_maximo - 55:
                    material_curar = random.choice(vendas)
                # Si ha bajado mas de 30 puntos, se usa un paquete:
                elif militar.puntos_vida < puntos_vida_maximo - 55:
                    material_curar = random.choice(paquetes)

            # si se ha encontrado el material, se le suman los puntos de vida
            if material_curar:
                if militar.puntos_vida + material_curar.puntos_salud > puntos_vida_maximo:
                    militar.puntos_vida = puntos_vida_maximo
                else:
                    militar.puntos_vida = militar.puntos_vida + material_curar.puntos_salud

                self.materiales_hospital.remove(material_curar)
