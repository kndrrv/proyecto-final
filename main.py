from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca

def main(): # función principal
    biblioteca = Biblioteca()
    biblioteca.cargar_datos()

    while True:
        print("\n=== SISTEMA DE BIBLIOTECA VIRTUAL ===")
        print("1. Registrar libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Ver libros disponibles")
        print("6. Ver usuarios y sus libros")
        print("7. Salir")

        try:
            opcion = input("\nSeleccione una opción: ")
            if not opcion.isdigit():
                raise ValueError("Por favor, ingrese un número")
            opcion = int(opcion)

            if opcion == 1:
                titulo = input("Título del libro: ")
                autor = input("Autor: ")
                while True:
                    try:
                        anio = input("Año de publicación: ")
                        if not anio.isdigit():
                            raise ValueError("El año debe ser un número")
                        anio = int(anio)
                        break
                    except ValueError as e:
                        print(f"Error: {str(e)}")
                
                while True:
                    try:
                        volumen = input("Número de volumen: ")
                        if not volumen.isdigit():
                            raise ValueError("El volumen debe ser un número")
                        volumen = int(volumen)
                        break
                    except ValueError as e:
                        print(f"Error: {str(e)}")

                libro = Libro(titulo, autor, anio, volumen)
                biblioteca.agregar_libro(libro)
                print("Libro registrado exitosamente")

            elif opcion == 2:
                nombre = input("Nombre del usuario: ")
                while True:
                    try:
                        id_str = input("ID de usuario: ")
                        if not id_str.isdigit():
                            raise ValueError("El ID debe ser un número")
                        id_usuario = int(id_str)
                        usuario = Usuario(nombre, id_usuario)
                        biblioteca.registrar_usuario(usuario)
                        print("Usuario registrado exitosamente")
                        break
                    except ValueError as e:
                        print(f"Error: {str(e)}")
                        print("Intente con otro ID")

            elif opcion == 3:
                titulo = input("Título del libro a prestar: ")
                while True:
                    try:
                        id_str = input("ID del usuario: ")
                        if not id_str.isdigit():
                            raise ValueError("El ID debe ser un número")
                        id_usuario = int(id_str)
                        biblioteca.prestar_libro(titulo, id_usuario)
                        print("Libro prestado exitosamente")
                        break
                    except ValueError as e:
                        print(f"Error: {str(e)}")

            elif opcion == 4:
                titulo = input("Título del libro a devolver: ")
                while True:
                    try:
                        id_str = input("ID del usuario: ")
                        if not id_str.isdigit():
                            raise ValueError("El ID debe ser un número")
                        id_usuario = int(id_str)
                        biblioteca.devolver_libro(titulo, id_usuario)
                        print("Libro devuelto exitosamente")
                        break
                    except ValueError as e:
                        print(f"Error: {str(e)}")

            elif opcion == 5:
                biblioteca.mostrar_libros_disponibles()

            elif opcion == 6:
                biblioteca.mostrar_usuarios()

            elif opcion == 7:
                biblioteca.guardar_datos()
                print("¡Hasta luego!")
                break

            else:
                print("Opción no válida")

        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()