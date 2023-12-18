diccionario = {'c1':'valor1','c2':'valor2'}
print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']
print(resultado)

cliente = {'nombre':'Juan','apellido':'Fuentes','peso':88,'altura':1.76}
consulta = (cliente['apellido'])
print(consulta)

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'][1])
print(dic['c3']['s2'])

diccionario['c3'] = 'valor3'
print(diccionario)
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())