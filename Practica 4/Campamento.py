from Armeria import Armeria
from Hospital import Hospital


class Campamento:

    def __init__(self):
        self.legion = None
        self.edificios = []
        self.edificios.append(Armeria())
        self.edificios.append(Hospital())

    def establecer_legion(self, legion):
        if self.legion:
            print("Este campamento está ocupado. Búscate otro donde acampar")
        else:
            self.legion = legion
            self.legion.establecer_campamento(self)

    def obtener_armeria(self):
        return self.edificios[0]

    def obtener_hospital(self):
        return self.edificios[1]
