class Mecanico:

    @staticmethod
    def diagnosticar(coche):
        hay_piezas_averiadas = 0
        print("*** Piezas defectuosas del coche ***")
        if coche.motor.consultar_estado() < 3:
            hay_piezas_averiadas += 1
            print(f"- Motor")

        for r in coche.ruedas:
            if r.consultar_estado() < 3:
                hay_piezas_averiadas += 1
                print(f"- Rueda {coche.ruedas.index(r)}")

        for a in coche.asientos:
            if a.consultar_estado() < 3:
                hay_piezas_averiadas += 1
                print(f"- Asiento {coche.asientos.index(a)}")

        if hay_piezas_averiadas == 0:
            print("- No hay ninguna pieza averiada")

    @staticmethod
    def reparar(coche):
        if coche.motor.consultar_estado() < 3:
            motor_nuevo = coche.motor
            motor_nuevo.establecer_estado(10)
            coche.quitar_motor()
            coche.poner_motor(motor_nuevo)

        for r in coche.ruedas:
            if r.consultar_estado() < 3:
                rueda_nueva = r
                rueda_nueva.establecer_estado(10)
                posicion_rueda = coche.ruedas.index(r)
                coche.quitar_rueda(posicion_rueda)
                coche.poner_rueda(posicion_rueda, rueda_nueva)

        for a in coche.asientos:
            if a.consultar_estado() < 3:
                asiento_nuevo = a
                asiento_nuevo.establecer_estado(10)
                posicion_asiento = coche.asientos.index(a)
                coche.quitar_asiento(posicion_asiento)
                coche.poner_asiento(posicion_asiento, asiento_nuevo)
