from libro import Libro
from usuario import Usuario
from prestamo import Prestamo

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    # ============ Libros ============

    def agregar_libro(self, titulo, autor, editorial, anio_publicacion, cant_ejemplares):
        libro = Libro(titulo, autor, editorial, anio_publicacion, cant_ejemplares)
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        # no elimino si hay préstamos activos del mismo título
        encontrado = False
        for libro in list(self.libros):
            if libro.titulo.lower().split() == titulo.lower().split():
                for prestamo in self.prestamos:
                    if prestamo.libro.titulo.lower().split() == titulo.lower().split():
                        print(">>> No se puede eliminar porque hay préstamos activos de este libro.")
                        return
                self.libros.remove(libro)
                print(">>> Libro eliminado.")
                encontrado = True
                break
        if not encontrado:
            print(">>> Libro no encontrado.")

    def buscar_por_titulo(self, texto):
        # título exacto normalizado
        encontrado = False
        for libro in self.libros:
            if libro.titulo.lower().split() == texto.lower().split():
                encontrado = True
                print(f"{libro.titulo} por {libro.autor} - Editorial: '{libro.editorial}' - Año: {libro.anio_publicacion} - {libro.cant_ejemplares} ejemplares.")
        if not encontrado:
            print(">>> No hay libros disponibles.")

    def buscar_por_autor(self, texto):
        # autor exacto normalizado
        encontrado = False
        for libro in self.libros:
            if libro.autor.lower().split() == texto.lower().split():
                encontrado = True
                print(f"{libro.titulo} por {libro.autor} - Editorial: '{libro.editorial}' - Año: {libro.anio_publicacion} - {libro.cant_ejemplares} ejemplares.")
        if not encontrado:
            print(">>> No hay libros disponibles.")

    def buscar_por_editorial(self, texto):
        # editorial exacta normalizada
        encontrado = False
        for libro in self.libros:
            if libro.editorial.lower().split() == texto.lower().split():
                encontrado = True
                print(f"{libro.titulo} por {libro.autor} - Editorial: '{libro.editorial}' - Año: {libro.anio_publicacion} - {libro.cant_ejemplares} ejemplares.")
        if not encontrado:
            print(">>> No hay libros disponibles.")

    def disponibilidad(self, texto_titulo):
        # devuelve el primer libro cuyo título normalizado coincida y tenga stock
        for libro in self.libros:
            if libro.titulo.lower().split() == texto_titulo.lower().split():
                if libro.cant_ejemplares > 0:
                    return libro
                print(">>> No hay ejemplares disponibles.")
                return False
        print(">>> No se encontró ese título.")
        return False

    # ============ Usuarios ============

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_usuario(self, nombre, apellido, dni, direccion, telefono):
        usuario = Usuario(nombre, apellido, dni, direccion, telefono)
        self.usuarios.append(usuario)

    def eliminar_usuario(self, dni):
        # no elimino si tiene préstamos activos
        encontrado = False
        for usuario in list(self.usuarios):
            if usuario.dni == dni.strip():
                for prestamo in self.prestamos:
                    if prestamo.usuario.dni == dni.strip():
                        print(">>> No se puede eliminar: el usuario tiene préstamos activos.")
                        return
                self.usuarios.remove(usuario)
                print(">>> Usuario eliminado.")
                encontrado = True
                break
        if not encontrado:
            print(">>> No existe el usuario.")

    def buscar_usuario_nombre(self, texto):
        # nombre exacto normalizado
        encontrado = False
        for usuario in self.usuarios:
            if usuario.nombre.lower().split() == texto.lower().split():
                encontrado = True
                usuario.mostrar_datos()
        if not encontrado:
            print(">>> No existe el usuario.")

    def buscar_usuario_apellido(self, texto):
        # apellido exacto normalizado
        encontrado = False
        for usuario in self.usuarios:
            if usuario.apellido.lower().split() == texto.lower().split():
                encontrado = True
                usuario.mostrar_datos()
        if not encontrado:
            print(">>> No existe el usuario.")

    def buscar_usuario_dni(self, dni):
        for usuario in self.usuarios:
            if usuario.dni == dni.strip():
                usuario.mostrar_datos()
                return usuario
        print(">>> No existe el usuario.")
        return False

    # ============ Préstamos ============

    def listar_prestamos(self):
        if len(self.prestamos) == 0:
            print(">>> No hay préstamos.")
            return
        for prestamo in self.prestamos:
            print(f"{prestamo.usuario.nombre} {prestamo.usuario.apellido} DNI {prestamo.usuario.dni} -> {prestamo.libro.titulo}")


    def prestar_libro(self, dni, texto_titulo):
        usuario = self.buscar_usuario_dni(dni)
        if not usuario:
            print(">>> No existe el usuario.")
            return
        libro = self.disponibilidad(texto_titulo)
        if not libro:
            return
        prestamo = Prestamo(usuario, libro)
        self.prestamos.append(prestamo)
        usuario.libros_prestados.append(libro)
        libro.cant_ejemplares -= 1
        print(">>> Libro prestado.")

    def devolver_libro(self, dni, texto_titulo):
        # devuelve por dni y por título exacto normalizado
        usuario = self.buscar_usuario_dni(dni)
        if not usuario:
            print(">>> No existe el usuario.")
            return

        encontrado = False
        for prestamo in list(self.prestamos):
            if prestamo.usuario.dni == dni.strip():
                if prestamo.libro.titulo.lower().split() == texto_titulo.lower().split():
                    prestamo.libro.cant_ejemplares += 1
                    i = 0
                    while i < len(usuario.libros_prestados):
                        if usuario.libros_prestados[i].titulo.lower().split() == texto_titulo.lower().split():
                            usuario.libros_prestados.pop(i)
                            break
                        i += 1
                    self.prestamos.remove(prestamo)
                    print(">>> Libro devuelto.")
                    encontrado = True
                    break
        if not encontrado:
            print(">>> No se encontró un préstamo con esos datos.")
