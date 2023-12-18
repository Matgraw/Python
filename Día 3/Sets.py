mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3,1,2,1,2,1,2,1,(1,2,3),1}
print(type(otro_set))
print(otro_set)

print(len(mi_set))
print(2 in mi_set)
s3 = mi_set.union(otro_set)
print(s3)
mi_set.add(6)
print(mi_set)
mi_set.remove(3)
print(mi_set)
mi_set.discard(2)
print(mi_set)