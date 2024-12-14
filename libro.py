class Libro: # se crea la clase libro con sus atributos
    consecutivo = 1 # variable para crear consecutivos únicos

    def __init__(self, titulo, autor, anio_publicacion, numero_de_volumen):
        self.consecutivo = Libro.consecutivo # asignamos el consecutivo
        Libro.consecutivo += 1 # y se incrementa
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacio = anio_publicacion
        self.numero_de_volumen = numero_de_volumen
        self.disponible = True # inidica si el libro está disponible

    def to_dict(self):  # convierte el objeto a un diccionario para guardarlo en un archivo json
        return {
            "consecutivo": self.consecutivo,
            "titulo": self.titulo,
            "autor": self.autor,
            "anio_publicacion": self.anio_publicacion,
            "numero_de_volumen": self.numero_de_volumen,
            "disponible": self.disponible
            }
    
@classmethod
def from_dict(cls, datos):  # crea un objeto libro desde un diccionario
    libro = cls(
        datos["titulo"],
        datos["autor"],
        datos["anio_publicacion"],
        datos["numero_de_volumen"]
        )
    libro.consecutivo = datos["consecutivo"]
    libro.disponible = datos["disponible"]
    return libro