import os

directorio = os.path.dirname(os.path.abspath(__file__))
directorio_padre = os.path.dirname(directorio)
archivo_nombres = os.path.join(directorio_padre, "nombres.txt")

try:
    with open(archivo_nombres, "r", encoding="utf-8") as archivo:
        lineas = [linea for linea in archivo if linea.strip()]

    cantidad_nombres = len(lineas)

    print("=" * 50)
    print(f"El archivo 'nombres.txt' tiene un total de: {cantidad_nombres} nombres.")
    print("=" * 50)

except FileNotFoundError:
    print(f"No se encontró el archivo en: {archivo_nombres}")