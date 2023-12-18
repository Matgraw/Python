def ceros_consecutivos(*args):
    numero_anterior = -1

    for n in args:
        if n == 0 and numero_anterior == n:
            return True

        numero_anterior = n

    return False

print(ceros_consecutivos(5,6,1,0,0,9,3,5))
print(ceros_consecutivos(6,0,5,1,0,3,0,1))