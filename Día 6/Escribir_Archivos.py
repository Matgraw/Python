archivo = open('prueba1.txt','w')

archivo.write('Soy el nuevo texto\n')

archivo.close()

print('-'*50)

archivo = open('prueba1.txt','w')

lista = ['Soy','el','nuevo','texto']

for p in lista:
    archivo.writelines(p +'\n')

archivo.close()

print('-'*50)

archivo = open('prueba1.txt','a')

archivo.write('Soy el nuevo texto\n')

archivo.close()

print('-'*50)