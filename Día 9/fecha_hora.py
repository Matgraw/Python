import datetime

mi_hora = datetime.time(17, 35)
print(type(mi_hora))
print(mi_hora)
print(mi_hora.minute)
print(mi_hora.hour)

mi_fecha = datetime.date(2025, 10, 17)
print(mi_fecha)
print(mi_fecha.day)
print(mi_fecha.ctime())

print(mi_fecha.today())
