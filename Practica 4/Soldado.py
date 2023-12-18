from Militar import Militar


class Soldado(Militar):

    def __init__(self):
        super().__init__()
        self.puntos_vida = 150
