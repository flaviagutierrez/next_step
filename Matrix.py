matriz= [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
#opcion 1: recorriendo con indices
num_filas=len(matriz)
num_columnas=len(matriz[0])
for i in range(num_filas):
  for j in range(num_columnas):
   elemento=matriz[i][j]
   print(f"El elemento en ({i},{j}) es {elemento}")

  #opcion 2: recorriendo con elementos
  for fila_actual in matriz:
    for elemento in fila_actual:
      print(elemento, end=" ")
    print()