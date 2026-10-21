with open("nombres.txt", "w", ) as archivo:
    for i in range(5):
        nombre = input(f"Escribe el nombre {i + 1}: ")
        archivo.write(nombre + "\n")

print("Los estudiantes se guardaron en nombres.txt.")