def adivinar_clave():
    clave_correcta = "www"
    intentos = 3

    while intentos > 0:
        intento_usuario = input("Intenta adivinar la clave de 3 letras: ").lower()

        if len(intento_usuario) > 3:
            print("La clave debe tener exactamente 3 letras")
        elif not intento_usuario.isalpha():
            print("La clave solo debe contener letras")
        else:
            if intento_usuario == clave_correcta.lower():
                print("Enhorabuena lo conseguiste!")
                break
            elif intento_usuario[:2] == clave_correcta.lower()[:2]:
                print(f"Casi lo adivinas, no te cuento el intento. Te quedan {intentos} intentos")
            else:
                intentos -= 1
                if intentos == 0:
                    print(f"Se te acabaron los intentos. La clave correcta era {clave_correcta.lower()}")
                else:
                    print(f"Esa no es la clave. Te quedan {intentos} intentos")


adivinar_clave()
