class Aula:

    def __init__(self):
        self.identificador = ""
        self.puestos = []

    def establecer_identificador(self, identificador):
        self.identificador = identificador

    def establecer_puesto(self, puesto):
        self.puestos.append(puesto)

    def encender_apagar(self):
        for p in self.puestos:
            p.encender_apagar()

    def obtener_puestos_defectuosos(self):
        for p in self.puestos:
            aparatos_averiados = [a for a in p.aparatos if a.averiado]

            if len(aparatos_averiados) > 0:
                print(f"Aula {self.identificador}. Puesto {p.identificador}:")

                for a in aparatos_averiados:
                    clase_aparato = type(a).__name__

                    if clase_aparato in ['Cpu', 'Proyector']:
                        print(f"- {clase_aparato} averiado. Se ha encendido {a.numero_veces_encendido} veces")
                    else:
                        print(f"- {clase_aparato} averiado")
