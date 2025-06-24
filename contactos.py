import json
import os

# =========================
# 📇 GESTOR DE CONTACTOS EN PYTHON
# =========================

# Archivo donde se guardan los contactos
ARCHIVO_CONTACTOS = "contactos.json"

# Variables
lista_de_contactos = []
proximo_id_contacto = 1


# -------------------
# 📂 Funciones de archivo
# -------------------
def cargar_contactos():
    global lista_de_contactos, proximo_id_contacto
    if os.path.exists(ARCHIVO_CONTACTOS):
        with open(ARCHIVO_CONTACTOS, "r", encoding="utf-8") as f:
            lista_de_contactos.extend(json.load(f))
            if lista_de_contactos:
                proximo_id_contacto = max(c["id"] for c in lista_de_contactos) + 1


def guardar_contactos():
    with open(ARCHIVO_CONTACTOS, "w", encoding="utf-8") as f:
        json.dump(lista_de_contactos, f, indent=4, ensure_ascii=False)


# -------------------
# ➕ Agregar
# -------------------
def agregar_contacto(nombre, telefono, organizacion):
    global proximo_id_contacto
    nuevo_contacto = {
        "id": proximo_id_contacto,
        "nombre": nombre,
        "telefono": telefono,
        "organizacion": organizacion.lower().strip()
    }
    lista_de_contactos.append(nuevo_contacto)
    proximo_id_contacto += 1
    guardar_contactos()
    print(f"\n✅ Contacto '{nombre}' añadido con éxito.\n")


# -------------------
# 🔎 Mostrar
# -------------------
def mostrar_contactos(filtro_org=None):
    print("\n📒 LISTA DE CONTACTOS")
    print("-" * 40)
    if not lista_de_contactos:
        print("🚫 No hay contactos guardados.")
        return

    if filtro_org:
        contactos = [c for c in lista_de_contactos if c["organizacion"] == filtro_org.lower().strip()]
        if not contactos:
            print(f"🚫 No se encontraron contactos en '{filtro_org}'.")
            return
    else:
        contactos = lista_de_contactos

    contactos = sorted(contactos, key=lambda c: c["nombre"].lower())

    for c in contactos:
        print(f"🆔 {c['id']} | 👤 {c['nombre']} | 📞 {c['telefono']} | 🏷️ {c['organizacion'].capitalize()}")

    print("-" * 40)


# -------------------
# ✏️ Editar
# -------------------
def buscar_contacto_por_id(id_buscado):
    for c in lista_de_contactos:
        if c["id"] == id_buscado:
            return c
    return None


def editar_contacto(id_contacto):
    contacto = buscar_contacto_por_id(id_contacto)
    if contacto:
        print(f"\n🛠️ Editando contacto ID {id_contacto} (deja vacío para no cambiar)")
        nuevo_nombre = input(f"👤 Nuevo nombre [{contacto['nombre']}]: ") or contacto['nombre']
        nuevo_telefono = input(f"📞 Nuevo teléfono [{contacto['telefono']}]: ") or contacto['telefono']
        nueva_org = input(f"🏷️ Nueva organización [{contacto['organizacion']}]: ") or contacto['organizacion']
        contacto.update({
            "nombre": nuevo_nombre,
            "telefono": nuevo_telefono,
            "organizacion": nueva_org.lower().strip()
        })
        guardar_contactos()
        print("✅ Contacto actualizado con éxito.\n")
    else:
        print(f"❌ No se encontró contacto con ID {id_contacto}.")


# -------------------
# 🗑️ Eliminar
# -------------------
def eliminar_contacto(id_contacto):
    contacto = buscar_contacto_por_id(id_contacto)
    if contacto:
        lista_de_contactos.remove(contacto)
        guardar_contactos()
        print(f"🗑️ Contacto '{contacto['nombre']}' eliminado.\n")
    else:
        print(f"❌ No se encontró contacto con ID {id_contacto}.")


# -------------------
# ▶️ Programa principal
# -------------------
cargar_contactos()

while True:
    print("\n📋 MENÚ DE CONTACTOS")
    print("1️⃣ Agregar nuevo contacto")
    print("2️⃣ Mostrar todos los contactos")
    print("3️⃣ Mostrar contactos por organización")
    print("4️⃣ Editar contacto")
    print("5️⃣ Eliminar contacto")
    print("0️⃣ Salir")
    opcion = input("🔹 Elige una opción: ")

    if opcion == '1':
        nombre = input("👤 Nombre: ")
        telefono = input("📞 Teléfono: ")
        organizacion = input("🏷️ Organización (familia, amigo, trabajo, otro): ")
        agregar_contacto(nombre, telefono, organizacion)

    elif opcion == '2':
        mostrar_contactos()

    elif opcion == '3':
        filtro = input("🔍 ¿Qué organización quieres ver?: ")
        mostrar_contactos(filtro_org=filtro)

    elif opcion == '4':
        try:
            id_c = int(input("✏️ ID del contacto a editar: "))
            editar_contacto(id_c)
        except ValueError:
            print("❌ Debes ingresar un número válido.")

    elif opcion == '5':
        try:
            id_c = int(input("🗑️ ID del contacto a eliminar: "))
            eliminar_contacto(id_c)
        except ValueError:
            print("❌ Debes ingresar un número válido.")

    elif opcion == '0':
        print("👋 ¡Hasta luego!")
        break

    else:
        print("🚫 Opción no válida. Intenta de nuevo.")
