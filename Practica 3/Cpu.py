from Aparato import Aparato


class Cpu(Aparato):

    def __init__(self):
        super().__init__()
        self.numero_veces_encendido = 0

    def encender_apagar(self):
        super().encender_apagar()
        if self.encendido:
            self.numero_veces_encendido += 1
