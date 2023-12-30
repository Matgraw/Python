from Venda import Venda
from Paquete import Paquete


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
        print("*"*50)
        print("Recibiendo cargamento de materiales de hospital...")
        for m in materiales:
            self.materiales_hospital.append(m)
        print("Hospital cargado correctamente!!!!")

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