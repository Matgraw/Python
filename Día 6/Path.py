from pathlib import Path

guia = Path(Path.home(),"Desktop","Python","Día 6","Europa")

for txt in Path(guia).glob("*.txt"):
    print(txt)

print('-'*50)

for txt in Path(guia).glob("**/*.txt"):
    print(txt)

print('-'*50)

guia_nueva = Path(Path.home(),"Desktop","Python","Día 6","Europa","España","Barcelona","Sagrada_Familia.txt")
en_europa = guia_nueva.relative_to(Path(Path.home(),"Desktop","Python","Día 6","Europa"))
en_espana = guia_nueva.relative_to(Path(Path.home(),"Desktop","Python","Día 6","Europa","España"))

print(en_europa)
print(en_espana)
