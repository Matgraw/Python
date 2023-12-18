from Arma import Arma


class Escudo(Arma):
    def __init__(self):
        super().__init__()
        self.puntos_ataque = 1
        self.puntos_defensa = 6
