from collections import Counter
from collections import defaultdict
from collections import namedtuple

numeros = [8,6,9,5,4,5,8,5,4,9,6,5,7,4,5,8]
print(Counter(numeros))
frase = "Al pan pan y al vino vino"
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4])
print(serie.most_common())
print(list(serie))

mi_dic = defaultdict(lambda: 'nada') # {'uno': 'verde', 'dos': 'azul', 'tres': 'rojo'}
mi_dic['uno'] = 'verde'
print(mi_dic)
print(mi_dic['dos'])

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)
print(ariel.altura)
print(ariel.peso)
print(ariel[2])