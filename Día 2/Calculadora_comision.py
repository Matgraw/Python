##### Proyecto 2 - Comision de ventas #####
nombre_vendedor = input("Dime tu nombre: ")
ingresos = input("Dime cuanto dinero has conseguido este mes: ")
ingresos = float(ingresos)
comision = round((ingresos * 13) / 100,2)
print(f"{nombre_vendedor} ha conseguido este mes {ingresos}€, por lo que se lleva una comisión de {comision}€")
