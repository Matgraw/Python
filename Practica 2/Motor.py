class Motor:

    def __init__(self):
        self.caballos = 0
        self.combustible = ""
        self.cilindrada = 0
        self.estado = 0
        self.tipo = ""
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True

    def apagar(self):
        if self.encendido:
            self.encendido = False

    def establecer_caballos(self, caballos):
        self.caballos = caballos

    def establecer_combustible(self, combustible):
        self.combustible = combustible

    def establecer_cilindrada(self, cilindrada):
        self.cilindrada = cilindrada

    def establecer_estado(self, estado):
        self.estado = estado

    def establecer_tipo(self, tipo):
        self.tipo = tipo

    def consultar_estado(self):
        return self.estado
