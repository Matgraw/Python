## Sensible a myusculas y minusculas
## Si no encuentra una palabra o caracter, muestra una excepcion
## Si hay mas de una palabra o texto devuelve el primero que encuentra
mi_texto = "Esta es una prueba"
resultado = mi_texto[0]
print(resultado)
resultado = mi_texto[9]
print(resultado)
resultado = mi_texto[-4]
print(resultado)
resultado = mi_texto.index("n")
print(resultado)
resultado = mi_texto.index("prueba")
print(resultado)
resultado = mi_texto.index("a")
print(resultado)
resultado = mi_texto.index("a",5)
print(resultado)
resultado = mi_texto.rindex("a")
print(resultado)