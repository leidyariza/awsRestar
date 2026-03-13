def es_primo(num):
    if num < 2:
        return False
    for  i in range(2, num):
        if num % i == 0:
            return False
    return True

#Generar lista para los numeros primos de 1 al 50
primos = []
for n in range(1,251):
    if es_primo(n):
        primos.append(str(n))

print ("Números primos entre 1 y 250:")
print (", ".join(primos))
with open("result.txt","w") as archivo:
    archivo.write("\n".join(primos))
print("\nArchivo 'result.txt' generado con éxito.")
