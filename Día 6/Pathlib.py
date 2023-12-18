from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/migue/Desktop/Python/Día 6/prueba.txt')
ruta_windows = PureWindowsPath(carpeta)

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print(ruta_windows)
    print(carpeta.read_text())
    print(carpeta.name)
    print(carpeta.suffix)
    print(carpeta.stem)
    print("Genial, existe")


ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
carpeta = ruta.parents[3]
print(carpeta)