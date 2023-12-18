class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    def __init__(self,edad,color,altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Pio")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")

print(Pajaro.__bases__)
print(Animal.__subclasses__())

print('*'*50)

piolin = Pajaro(2,'amarillo',60)
mi_animal = Animal(5,'negro')

piolin.nacer()
piolin.hablar()
print(piolin.color)

print('*'*50)
piolin.hablar()
piolin.volar(100)