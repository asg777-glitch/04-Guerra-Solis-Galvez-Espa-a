with open("numeros.txt", "w") as archivo1:
    archivo1.write("1\n")
    archivo1.write("9\n")
    archivo1.write("4\n")
    archivo1.write("5\n")
    archivo1.write("9\n")
    archivo1.write("1\n")
    archivo1.write("3\n")
    archivo1.write("2\n")
    archivo1.write("7\n")
    archivo1.write("8\n")

total=0
with open("numeros.txt", "r") as archivo:
    for linea in archivo:
       
        linea_limpia = linea.strip()
        if linea_limpia: 
            numero = int(linea_limpia)  
            total += numero

print(f"La suma total es: {total}")

with open("resultado.txt", "w") as archivo_resultado:
    archivo_resultado.write(f"La suma total es: {total/10}\n")