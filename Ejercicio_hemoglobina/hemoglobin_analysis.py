import json
"""
Ejercicio para analizar la hemoglobina humana
Funciones del programa:
1. Leer la secuencia desde un archivo
2. Mostrar información básica
3. Calcular composición de aminoácidos
4. Calcular peso molecular
5. Calcular porcentaje hidrofóbico
6. Guardar resultados en JSON
"""

#Ejercicio 3 Para leer el archivo
with open("/workspaces/awsRestar/Ejercicio_hemoglobina/data/hemoglobin_clean.txt", "r") as file:
    sequence = file.read()

# Ejercicio4, Mostrar la informacion de la secuencia
print("Proteína: Hemoglobin beta")
#Visualiza el archivo que leyo anteriormente
print("Secuencia:", sequence)
# Con la funcion len calcula la longitud de la cadena
print("Longitud:", len(sequence))

# Crear lista de aminoacidos
amino_acidos = list("ACDEFGHIKLMNPQRSTVWY")

#Diccionario para hacer conteo
amino_count = {}

for j in amino_acidos:
    amino_count[j] = sequence.count(j)

print("\nConteo de aminoácidos")

for j, count in amino_count.items():
    print(j, count)

##Diccionario para Peso Molecular
peso_molecular = {
"A":89.1,"C":121.2,"D":133.1,"E":147.1,
"F":165.2,"G":75.1,"H":155.2,"I":131.2,
"K":146.2,"L":131.2,"M":149.2,"N":132.1,
"P":115.1,"Q":146.2,"R":174.2,"S":105.1,
"T":119.1,"V":117.1,"W":204.2,"Y":181.2
}

#Crear funcion para 
def calcular_peso_molecular(seq):

    peso = 0

    for j in seq:
        if j in peso_molecular:
            peso += peso_molecular[j]

    return peso

peso_molecular = calcular_peso_molecular(sequence)

print("\nPeso molecular:", peso_molecular)

#Calcular porcentaje hidrofobico
amino_hidrofobico = ["A","V","I","L","M","F","W","Y"]

count = 0

for j in sequence:
    if j in amino_hidrofobico:
        count += 1

porcentaje = (count / len(sequence)) * 100

print("\nPorcentaje hidrofóbico:", porcentaje)

results = {
"nombre proteina": "Hemoglobin beta",
"longitud": len(sequence),
"Conteo aminoacidos": amino_count,
"Peso Molecuar": peso_molecular,
"Porcentaje hidrofobico": porcentaje
}

with open("hemoglobin_results.json","w") as file:
    json.dump(results,file,indent=4)