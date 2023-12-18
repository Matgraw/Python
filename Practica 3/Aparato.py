class Aparato:

    def __init__(self):
        self.encendido = None
        self.averiado = None

    def establecer_averiado(self, averiado):
        self.averiado = averiado

    def encender_apagar(self):
        if self.encendido:
            self.encendido = False
        else:
            self.encendido = True
