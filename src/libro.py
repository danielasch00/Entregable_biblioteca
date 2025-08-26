class Libro:
    def __init__(self, titulo, autor, editorial, anio_publicacion, cant_ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_publicacion = int(anio_publicacion)
        self.cant_ejemplares = int(cant_ejemplares) 

    def MostrarTitulo(self):
        return self.titulo
    
    def MostrarAutor(self):
        return self.autor
     
    def MostrarEditorial(self):
        return self.editorial
     
    def MostrarDatos(self):
        return f"- {self.titulo} || {self.autor}"
