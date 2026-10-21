with open("saludo.txt", "w") as archivo:
    archivo.write("Rodolfo Félix Gálvez\n")
    archivo.write("Hola sigma boy")

with open("saludo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)