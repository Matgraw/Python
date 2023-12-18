from Militar import Militar


class Oficial(Militar):

    def __init__(self):
        super().__init__()
        self.puntos_vida = 100
        self.puntos_ataque = 1
        self.puntos_defensa = 1
