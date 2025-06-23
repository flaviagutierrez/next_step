matriz_5x5 = []

for i in range(5):
    fila = []
    for j in range(5):
        fila.append(0)
    matriz_5x5.append(fila)

# Imprimir la matriz
for fila in matriz_5x5:
    for elemento in fila:
        print(elemento, end="\t")
    print()
