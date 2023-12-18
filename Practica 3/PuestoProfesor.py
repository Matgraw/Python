from Puesto import Puesto


class PuestoProfesor(Puesto):

    def __init__(self):
        super().__init__()

    def establecer_cpu(self, cpu):
        self.aparatos.append(cpu)

    def establecer_proyector(self, proyector):
        self.aparatos.append(proyector)

    def encender_apagar(self):
        super().encender_apagar()
