# =========================
# LISTA DE CONTACTOS EN PYTHON
# =========================

# Variables 
lista_de_contactos = []
proximo_id_contacto = 1  # Para generar IDs únicos

# Agregar 
def agregar_contacto(nombre, telefono, email):
    global proximo_id_contacto
    nuevo_contacto = {
        "id": proximo_id_contacto,
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    lista_de_contactos.append(nuevo_contacto)
    proximo_id_contacto += 1
    print(f"✅ Contacto '{nombre}' añadido con éxito.")

# Mostrar 
def mostrar_contactos():
    print("\n--- 📇 LISTA DE CONTACTOS ---")
    if not lista_de_contactos:
        print("¡No hay contactos guardados!")
        return
    for c in lista_de_contactos:
        print(f"ID: {c['id']} | Nombre: {c['nombre']} | Tel: {c['telefono']} | Email: {c['email']}")

# Buscar
def buscar_contacto_por_id(id_buscado):
    for c in lista_de_contactos:
        if c["id"] == id_buscado:
            return c
    return None

# Editar 
def editar_contacto(id_contacto):
    contacto = buscar_contacto_por_id(id_contacto)
    if contacto:
        print(f"Editando contacto ID {id_contacto} (deja vacío para no cambiar)")
        nuevo_nombre = input(f"Nuevo nombre [{contacto['nombre']}]: ") or contacto['nombre']
        nuevo_telefono = input(f"Nuevo teléfono [{contacto['telefono']}]: ") or contacto['telefono']
        nuevo_email = input(f"Nuevo email [{contacto['email']}]: ") or contacto['email']
        contacto.update({
            "nombre": nuevo_nombre,
            "telefono": nuevo_telefono,
            "email": nuevo_email
        })
        print("✅ Contacto actualizado con éxito.")
    else:
        print(f"❌ No se encontró contacto con ID {id_contacto}.")

# Eliminar 
def eliminar_contacto(id_contacto):
    contacto = buscar_contacto_por_id(id_contacto)
    if contacto:
        lista_de_contactos.remove(contacto)
        print(f"✅ Contacto '{contacto['nombre']}' eliminado.")
    else:
        print(f"❌ No se encontró contacto con ID {id_contacto}.")

# Bucle 
while True:
    print("\n==== MENÚ DE CONTACTOS ====")
    print("1. Agregar nuevo contacto")
    print("2. Mostrar todos los contactos")
    print("3. Editar contacto")
    print("4. Eliminar contacto")
    print("0. Salir")
    opcion = input("Elige una opción: ")

    if opcion == '1':
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        agregar_contacto(nombre, telefono, email)

    elif opcion == '2':
        mostrar_contactos()

    elif opcion == '3':
        try:
            id_c = int(input("ID del contacto a editar: "))
            editar_contacto(id_c)
        except ValueError:
            print("❌ Debes ingresar un número válido.")

    elif opcion == '4':
        try:
            id_c = int(input("ID del contacto a eliminar: "))
            eliminar_contacto(id_c)
        except ValueError:
            print("❌ Debes ingresar un número válido.")

    elif opcion == '0':
        print("¡Hasta luego!")
        break

    else:
        print("❌ Opción no válida. Inténtalo de nuevo.")
