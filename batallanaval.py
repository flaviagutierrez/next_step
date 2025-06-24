import random

TAMANO_TABLERO = 4
NUM_BARCOS = 2
INTENTOS = 6

# tablero vacío 
def crear_tablero():
    return [["O"] * TAMANO_TABLERO for _ in range(TAMANO_TABLERO)]

# imprimir tablero 
def imprimir_tablero(tablero):
    print("\n  " + " ".join(str(i) for i in range(TAMANO_TABLERO)))
    for i, fila in enumerate(tablero):
        print(f"{i} " + " ".join(fila))

def colocar_barcos():
    barcos = set()
    while len(barcos) < NUM_BARCOS:
        fila = random.randint(0, TAMANO_TABLERO - 1)
        col = random.randint(0, TAMANO_TABLERO - 1)
        barcos.add((fila, col))
    return barcos

def coordenada_valida(fila, col):
    return 0 <= fila < TAMANO_TABLERO and 0 <= col < TAMANO_TABLERO

# juego 
def jugar_batalla_naval():
    tablero = crear_tablero()
    barcos = colocar_barcos()
    intentos = INTENTOS
    aciertos = 0

    print("🛳️ ¡Bienvenido a Batalla Naval 4x4!")
    print(f"Tienes {intentos} intentos para encontrar {NUM_BARCOS} barcos.\n")

    while intentos > 0 and aciertos < NUM_BARCOS:
        imprimir_tablero(tablero)
        try:
            fila = int(input("Ingresa fila (0-3): "))
            col = int(input("Ingresa columna (0-3): "))
        except ValueError:
            print("❌ Entrada no válida. Usa números.")
            continue

        if not coordenada_valida(fila, col):
            print("❌ Coordenadas fuera del tablero.")
            continue

        if tablero[fila][col] in ("X", "✔"):
            print("⚠️ Ya intentaste esa posición.")
            continue

        if (fila, col) in barcos:
            print("🎯 ¡Tocado!")
            tablero[fila][col] = "✔"
            barcos.remove((fila, col))
            aciertos += 1
        else:
            print("💦 Agua.")
            tablero[fila][col] = "X"
            intentos -= 1

        print(f"Intentos restantes: {intentos} | Barcos restantes: {NUM_BARCOS - aciertos}\n")

    # final
    imprimir_tablero(tablero)
    if aciertos == NUM_BARCOS:
        print("\n🏆 ¡Ganaste! Hundiste todos los barcos.")
    else:
        print("\n💀 ¡Perdiste! Los barcos restantes estaban en:")
        for fila, col in barcos:
            print(f"  - ({fila}, {col})")

# Ejecutar
if __name__ == "__main__":
    jugar_batalla_naval()