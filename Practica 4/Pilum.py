from Arma import Arma


class Pilum(Arma):
    def __init__(self):
        super().__init__()
        self.puntos_ataque = 9
        self.puntos_defensa = 1
