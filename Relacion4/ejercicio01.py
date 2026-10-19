from peliculas import peliculas

pelicula = {
    "titulo": "Avatar",
    "duracion": 134,
    "año_estreno": 2025,
    "edad_recomendada": 18,
    "generos": ["Ciencia Ficcion", "Aventura"]
}

peliculas.append(pelicula)

print(peliculas[-1])