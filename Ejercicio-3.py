import os
directorio = os.path.dirname(os.path.abspath(__file__))
archivo_nombres = os.path.join(directorio, "lista-estudiantes-aprobados.txt")

with open(archivo_nombres, "r") as archivo:
    lineas = archivo.readlines()
    
    cantidad_nombres = len(lineas)
    
    print("=" * 50)
    print(f"El archivo 'nombres.txt' tiene un total de: **{cantidad_nombres}** nombres.")
    print("=" * 50)
