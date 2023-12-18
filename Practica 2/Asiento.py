class Asiento:

    def __init__(self):
        self.tipo = ""
        self.estado = 0

    def establecer_tipo(self, tipo):
        self.tipo = tipo

    def establecer_estado(self, estado):
        self.estado = estado

    def consultar_estado(self):
        return self.estado
