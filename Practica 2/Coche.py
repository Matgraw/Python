class Coche:

    def __init__(self):
        self.ruedas = []
        self.asientos = []
        self.motor = None

    def quitar_rueda(self, numero_rueda):
        self.ruedas.pop(numero_rueda)

    def poner_rueda(self, numero_rueda, rueda):
        self.ruedas.insert(numero_rueda, rueda)

    def quitar_asiento(self, numero_asiento):
        self.asientos.pop(numero_asiento)

    def poner_asiento(self, numero_asiento, asiento):
        self.asientos.insert(numero_asiento, asiento)

    def quitar_motor(self):
        self.motor = None

    def poner_motor(self, motor):
        self.motor = motor
