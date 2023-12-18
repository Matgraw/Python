import os
import shutil

print(os.getcwd())

archivo = open('curso.txt','w')
archivo.write('texto de prueba')
archivo.close()

shutil.move('curso.txt', "C:\\Users\\migue\\Desktop")