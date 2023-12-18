mi_archivo = open('prueba.txt')

mi_linea = mi_archivo.readline()
print(mi_linea)
mi_linea = mi_archivo.readline()
print(mi_linea.rstrip())
mi_linea = mi_archivo.readline()
print(mi_linea)

mi_archivo.close()

print('-'*50)

mi_archivo = open('prueba.txt')
mi_lista = mi_archivo.readlines()
print(mi_lista)
mi_archivo.close()

print('-'*50)

mi_archivo = open('prueba.txt')
print(mi_archivo.read())
mi_archivo.close()