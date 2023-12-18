# Lorem ipsum dolor sit amet consectetur adipiscing elit, maecenas platea facilisi bibendum metus ridiculus, porta parturient pharetra interdum montes nostra
# Añadido control de flujo después de verlo en el día 4
texto = input("Dime el texto que se va a analizar: ").lower()
letras = input("Dime tres letras: ").lower()

if len(letras) > 3:
    print("ERROR!!!! Se han introducido más de 3 letras")
elif letras.isalpha():
    #Convertir el texto en una lista
    lista_texto = texto.split()

    #Numero de veces que aparece cada letra en el texto
    print("===========================================================================================")
    print(f"La letra '{letras[0]}' aparece {texto.count(letras[0])} veces en el texto analizado")
    print(f"La letra '{letras[1]}' aparece {texto.count(letras[1])} veces en el texto analizado")
    print(f"La letra '{letras[2]}' aparece {texto.count(letras[2])} veces en el texto analizado")
    #Numero de palabras que hay a los largo de todo el texto
    print("===========================================================================================")
    print(f"El numero de palabras en el texto analizado son {len(lista_texto)} palabras")
    # Primera y ultima letra del texto
    print("===========================================================================================")
    print(f"La primera letra del texto es {texto[0]}")
    print(f"La ultima letra del texto es {texto[-1]}")
    # Texto invertido
    print("===========================================================================================")
    print("El texto invertido quedaría de la siguiente manera:")
    lista_texto_invertida = lista_texto
    lista_texto_invertida.reverse()
    print(" ".join(lista_texto_invertida))
    # Se encuentra la palabra Python en el texto
    print("===========================================================================================")
    diccionario_existe = {True: "Se ha encontrado la palabra Python en el texto", False:"No existe la palabra Python en el texto"}
    existe_palabra = ("python" in texto)
    print(diccionario_existe[existe_palabra])
else:
    print("ERROR!!!! Se han introducido caracteres no permitidos")