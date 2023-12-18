import os

ruta = os.getcwd()

print(ruta)
print('-'*50)

ruta = os.chdir('C:\\Users\\migue\\Desktop\\Python_Ficheros')
ruta1 = 'C:\\Users\\migue\\Desktop\\Python\\Día 6\\prueba.txt'

archivo = open('otra_prueba.txt')
print(archivo)
print('-'*50)
fichero = os.path.basename(ruta1)
directorio = os.path.dirname(ruta1)
print(fichero,directorio)
print('-'*50)
elemento = os.path.split(ruta1)
print(elemento)
print('-'*50)
otro_archivo = open('C:\\Users\\migue\\Desktop\\Python_Ficheros\\otra_prueba.txt')
print(otro_archivo.read())
print('-'*50)

from pathlib import Path

carpeta = Path('C:/Users/migue/Desktop/Python_Ficheros')
archivo = carpeta / 'otra_prueba.txt'
mi_archivo = open(archivo)
print(mi_archivo.read())