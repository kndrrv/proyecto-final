from libro import Libro
from usuario import Usuario
import json

class Biblioteca: # se crea la clase biblioteca para manejar los libros y usuarios
    def __init__(self):
        self.libros = [] # lista de libros en la biblioteca
        self.usuarios = []  # lista de usuarios registrados
        self.archivo_libros = "libros.json" # archivo para guardar los libros
        self.archivo_usuarios = "usuarios.json" # archivo para guardar los usuarios

    def agregar_libro(self, libro):
        self.libros.append(libro) # añade un libro a la lista

    def registrar_usuario(self, usuario): # verifica que el ID no esté repetido
        for u in self.usuarios:
            if u.id_usuario == usuario.id_usuario:
                raise ValueError(f"Ya existe un usuario con el ID {usuario.id_usuario}")
        self.usuarios.append(usuario)

    def prestar_libro(self, titulo, id_usuario): # busca al usuario por id
        usuario = None
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                usuario = u
                break
        if not usuario:
            raise ValueError(f"No se encontró usuario con ID {id_usuario}")

        libro = None # busca un libro disponible por título
        for l in self.libros:
            if l.titulo == titulo and l.disponible:
                libro = l
                break
        if not libro:
            raise ValueError(f"El libro '{titulo}' no está disponible")

        libro.disponible = False # marca el libro como no disponible
        usuario.libros_prestados.append(libro) # lo añade a la lista de prestados al usuario

    def devolver_libro(self, titulo, id_usuario): # busca al usuario
        usuario = None
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                usuario = u
                break
        if not usuario:
            raise ValueError(f"No se encontró usuario con ID {id_usuario}")

        libro = None  # busca libros en lista de libros prestados
        for l in usuario.libros_prestados:
            if l.titulo == titulo:
                libro = l
                break
        if not libro:
            raise ValueError(f"El usuario no tiene prestado el libro '{titulo}'")

        libro.disponible = True
        usuario.libros_prestados.remove(libro)

    def mostrar_libros_disponibles(self): # muestra los libros disponibles
        print("\nLibros disponibles:")
        for libro in self.libros:
            if libro.disponible:
                print(f"[{libro.consecutivo}] {libro.titulo} - {libro.autor} (Vol. {libro.numero_de_volumen})")

    def mostrar_usuarios(self): # muestra los usuarios
        for usuario in self.usuarios:
            print(f"\nUsuario: {usuario.nombre} (ID: {usuario.id_usuario})")
            if usuario.libros_prestados:
                print("Libros prestados:")
                for libro in usuario.libros_prestados:
                    print(f"- {libro.titulo}")
            else:
                print("No tiene libros prestados")

    def guardar_datos(self):
        try: 
            with open(self.archivo_libros, 'w') as f:# guarda los libros en un archivo json
                json.dump([libro.to_dict() for libro in self.libros], f, indent=4)

            with open(self.archivo_usuarios, 'w') as f: # guarda los usuarios en un archivo json
                json.dump([usuario.to_dict() for usuario in self.usuarios], f, indent=4)

        except Exception as e:
            print(f"Error al guardar los datos: {str(e)}")

    def cargar_datos(self):   
        try:
            with open(self.archivo_libros, 'r') as f: # carga los libros desde un archivo json
                libros_data = json.load(f)
                self.libros = [Libro.from_dict(datos) for datos in libros_data]
        except FileNotFoundError:
            pass  # el archivo no existe aún


        try: # carga los usuarios desde un archivo json
            with open(self.archivo_usuarios, 'r') as f:
                usuarios_data = json.load(f)
                self.usuarios = [Usuario.from_dict(datos, self) for datos in usuarios_data]
        except FileNotFoundError:
            pass  # El archivo no existe aún.

        except Exception as e:
            print(f"Error al cargar los datos: {str(e)}")