class Pajaro:

    alas = True

    # Metodo constructor del objeto
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pio, mi color es {}".format(self.color))

    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("El pajaro mira")

piolin = Pajaro('amarillo','canario')

print(f"Mi pajaro es un {piolin.especie} y es de color {piolin.color}")
print(piolin.alas)
piolin.volar(50)
piolin.pintar_negro()

print('*'*50)

Pajaro.poner_huevos(3)

print('*'*50)

Pajaro.mirar()