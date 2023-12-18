class Mando:

    def __init__(self, television):
        self.television = television

    def encender_apagar_tv(self):
        if self.television.encendido:
            self.television.apagar()
        else:
            self.television.encender()

    def cambiar_canal_tv(self, canal):
        self.television.cambiar_canal(canal)

    def subir_volumen_tv(self):
        self.television.subir_volumen()

    def bajar_volumen_tv(self):
        self.television.bajar_volumen()
