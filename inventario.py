# 1. Crear una lista vacía llamada inventario
inventario = []

# 2. Crear tres diccionarios con productos diferentes
producto1 = {"nombre": "Short 'Guess'", "stock": 15}
producto2 = {"nombre": "Pantalon jean", "stock": 10}
producto3 = {"nombre": "Crop Top 'Strapless'", "stock": 12}

# 3. Añadir los diccionarios a la lista inventario
inventario.append(producto1)
inventario.append(producto2)
inventario.append(producto3)

# 4. Imprimir la cantidad de tipos de producto en el inventario
print(f"Número de tipos de producto en el inventario: {len(inventario)}\n")

# 5. Recorrer la lista inventario e imprimir el resumen de cada producto
print("--- Inventario Actual ---")
for producto in inventario:
    print(f"- {producto['nombre']}: {producto['stock']} unidades en stock.")