import sqlite3
import uuid
import datetime


conn = sqlite3.connect('alquiler.db')

cursor = conn.cursor()

def crear_tablas():
    cursor.execute(
        '''
    CREATE TABLE IF NOT EXISTS usuarios (
    uuid_usuario VARCHAR PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    nombre VARCHAR,
    fecha_nacimineto TIMESTAMP NOT NULL,
    pais VARCHAR    
    )                  
    '''
    )
    
    cursor.execute(
        '''
    CREATE TABLE IF NOT EXISTS peliculas (
    uuid_pelicula VARCHAR PRIMARY KEY,
    titulo VARCHAR UNIQUE NOT NULL,
    genero VARCHAR,
    duracion INTEGER    
    )                  
    '''
    )
    cursor.execute(
        '''
    CREATE TABLE IF NOT EXISTS alquileres (
    uuid_alquiler VARCHAR PRIMARY KEY,
    uuid_usuario VARCHAR,
    uuid_pelicula VARCHAR,
    fecha VARCHAR,
    precio REAL,
    modo_reproduccion VARCHAR NOT NULL,
    FOREIGN KEY (uuid_usuario) REFERENCES usuarios(uuid_usuario),
    FOREIGN KEY (uuid_pelicula) REFERENCES peliculas(uuid_pelicula)
    )                  
    '''
    )
    
    conn.commit()
    
def insertar_usuario():
    uuid_usuario = str(uuid.uuid4())
    email = input("Ingrese el email del usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del usuario: ")
    pais = input("Ingrese el país del usuario: ")
   
    query = '''INSERT INTO usuarios (uuid_usuario, email, nombre, fecha_nacimineto, pais)
    VALUES (?, ?, ?, ?, ?)
    '''
    
    cursor.execute(query, (uuid_usuario, email, nombre, fecha_nacimiento, pais))
    conn.commit()
    print(f"Usuario {nombre} insertado con éxito.") 
    
def insertar_peliculas():
    uuid_pelicula = str(uuid.uuid4())
    titulo = input("Ingrese el título de la película: ")
    genero = input("Ingrese el género de la película: ")
    duracion = input("Ingrese la duración de la película (en minutos): ")

    
def cerrar_conexion():
    cursor.close()
    conn.close()


def menu():
    crear_tablas()
    while True:
        print("\nMenu")
        print("1. Insertar un usuario")
        print("2. Insertar una película")
        print("3. Alquilar una película")
        print("4. Listar usuarios")
        print("5. Listar películas")
        print("6. Listar alquileres")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            insertar_usuario()
#       elif opcion == "2":
#       insertar_peliculas()
#       elif opcion == "3":
#       alquilarUsuarios()
#       elif opcion == "4":
#       listar_usuarios()
#       elif opcion == "5":
#       listar_peliculas()
#       elif opcion == "6":
#       listar_alquileres()
        elif opcion == "0":
            cerrar_conexion()
            break
    #   else:
    #       print("Opción no válida, intente nuevamente.")


menu()