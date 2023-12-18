from Soldado import Soldado


class Infanteria(Soldado):
    def __init__(self):
        super().__init__()
        self.puntos_ataque = 5
        self.puntos_defensa = 5

    def establecer_escudo(self, arma):
        self.armas.append(arma)
