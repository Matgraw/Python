class Television:

    def __init__(self):
        self.encendido = False
        self.numero_canal = 0
        self.nivel_volumen = 5

    def cambiar_estado_inicial(self):
        self.numero_canal = 1
        self.nivel_volumen = 10

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

    def subir_volumen(self):
        if self.nivel_volumen == 30:
            print("El volumen ya está en nivel más alto")
        else:
            self.nivel_volumen += 1

    def bajar_volumen(self):
        if self.nivel_volumen == 0:
            print("El volumen ya está en el nivel más bajo")
        else:
            self.nivel_volumen -= 1

    def cambiar_canal(self, canal):
        if canal > 99 or canal < 0:
            print("No es posible cambiar la televisión a ese canal")
        else:
            self.numero_canal = canal

    def estado_televisor(self):
        if self.encendido:
            print(f"El televisor está encendido en el canal {self.numero_canal} "
                  f"a {self.nivel_volumen} puntos de volumen")
        else:
            print(f"El televisor está apagado")

