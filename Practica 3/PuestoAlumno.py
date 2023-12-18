from Puesto import Puesto


class PuestoAlumno(Puesto):
    
    def __init__(self):
        super().__init__()

    def establecer_cpu(self, cpu):
        self.aparatos.append(cpu)

    def encender_apagar(self):
        super().encender_apagar()
