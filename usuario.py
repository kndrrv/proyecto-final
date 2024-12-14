class Usuario: # se crea la clase usuario con sus atributos 
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # lista de libros prestados

def to_dict(self):  # convierte el objeto a un diccionario para guardarlo en un archivo json
        return {
            "nombre": self.nombre,
            "id_usuario": self.id_usuario,
            "libros_prestados": [libro.consecutivo for libro in self.libros_prestados]
        }

@classmethod
def from_dict(cls, datos, biblioteca):  # crea un objeto usuario desde un diccionario
    usuario = cls(datos["nombre"], datos["id_usuario"])
    for consecutivo in datos["libros_prestados"]:
        for libro in biblioteca.libros:
            if libro.consecutivo == consecutivo:
                usuario.libros_prestados.append(libro)
                break
    return usuario