class Puesto:

    def __init__(self):
        self.identificador = None
        self.aparatos = []

    def establecer_identificador(self, identificador):
        self.identificador = identificador

    def establecer_monitor(self, monitor):
        self.aparatos.append(monitor)

    def establecer_teclado(self, teclado):
        self.aparatos.append(teclado)

    def establecer_raton(self, raton):
        self.aparatos.append(raton)

    def encender_apagar(self):
        for a in self.aparatos:
            a.encender_apagar()
