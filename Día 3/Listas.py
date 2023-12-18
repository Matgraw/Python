mi_lista = ["c","b","a"]
otra_lista = ["hola",55,6.1]
print(type(mi_lista))
resultado = len(mi_lista)
print(resultado)
resultado = mi_lista[0]
print(resultado)
resultado = mi_lista[0:2]
print(resultado)
mi_lista_total = mi_lista + otra_lista
print(mi_lista_total)
mi_lista_total[0] = 'alfa'
print(mi_lista_total)
mi_lista_total.append("g")
print(mi_lista_total)
eliminado = mi_lista_total.pop(3)
print(mi_lista_total)
print(eliminado)
mi_lista.sort()
print(mi_lista)
mi_lista.reverse()
print(mi_lista)
