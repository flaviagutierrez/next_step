matriz= [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
for fila in matriz:
  for elemento in fila:
      print(elemento, end=" ")
  print()

#Modificando matriz
print("Matriz con 0 en lugar de 1")

for i in range(len(matriz)):
  for j in range(len(matriz[i])):
      if matriz[i][j] == 1:
          matriz[i][j] = 0
for fila in matriz:
  for elemento in fila:
      print(elemento, end=" ")
  print()