# Diccionario para una Canción
cancion = {
    "titulo": "Shape of You",
    "artista": "Ed Sheeran",
    "album": "Divide",
    "duracion_segundos": 233,
    "genero": "Pop",
    "fecha_lanzamiento": ["2017-01-06"], 
    "colaboradores": ["Johnny McDaid", "Steve Mac"]
}

# Diccionario para un Coche
coche = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020,
    "color": "Negro",
    "placa": "ABC-1234",
    "caracteristicas": {
        "tipo_motor": "Gasolina",
        "potencia_hp": 132,
        "transmision": "Automática"
    }
}

# Diccionario para un Post de Red Social
post_red_social = {
    "id_post": 987654321,
    "autor": "user.py",
    "contenido_texto": "¡Learning python!",
    "fecha_publicacion": "2025-06-23 15:30:00",
}

def imprimir_cancion(cancion):
    print("🎵 Canción:")
    print(f"  Título: {cancion['titulo']}")
    print(f"  Artista: {cancion['artista']}")
    print(f"  Álbum: {cancion['album']}")
    print(f"  Duración: {cancion['duracion_segundos']} segundos")
    print(f"  Género: {cancion['genero']}")
    print(f"  Fecha de lanzamiento: {', '.join(cancion['fecha_lanzamiento'])}")
    print(f"  Colaboradores: {', '.join(cancion['colaboradores'])}")
    print()

def imprimir_coche(coche):
    print("🚗 Coche:")
    print(f"  Marca: {coche['marca']}")
    print(f"  Modelo: {coche['modelo']}")
    print(f"  Año: {coche['año']}")
    print(f"  Color: {coche['color']}")
    print(f"  Placa: {coche['placa']}")
    print("  Características:")
    for clave, valor in coche['caracteristicas'].items():
        print(f"    - {clave.replace('_', ' ').capitalize()}: {valor}")
    print()

def imprimir_post(post):
    print("📱 Post de Red Social:")
    print(f"  ID: {post['id_post']}")
    print(f"  Autor: {post['autor']}")
    print(f"  Contenido: {post['contenido_texto']}")
    print(f"  Fecha de publicación: {post['fecha_publicacion']}")
    print()

# Llamamos a las funciones para imprimir los diccionarios
imprimir_cancion(cancion)
imprimir_coche(coche)
imprimir_post(post_red_social)