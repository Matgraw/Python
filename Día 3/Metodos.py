texto = "Este es el texto de Federico"
resultado = texto.upper()
print(resultado)
resultado = texto[2].upper()
print(resultado)
resultado = texto.lower()
print(resultado)
resultado = texto.split() ## genera una lista
print(resultado)
resultado = texto.split("t")
print(resultado)
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
resultado = " ".join([a,b,c,d])
print(resultado)
resultado = texto.find("s")
print(resultado)
resultado = texto.find("g") ## Devuelve -1 si no lo encuentra
print(resultado)
resultado = texto.replace("Federico","todos")
print(resultado)