from Soldado import Soldado


class Caballeria(Soldado):

    def __init__(self):
        super().__init__()
        self.puntos_ataque = 7
        self.puntos_defensa = 8
