class Militar:

    def __init__(self):
        self.puntos_vida = None
        self.puntos_ataque = None
        self.puntos_defensa = None
        self.armas = []

    def establecer_arma(self, arma):
        self.armas.append(arma)
