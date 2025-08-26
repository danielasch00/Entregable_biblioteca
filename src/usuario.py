class Usuario:
    def __init__(self, nombre, apellido, dni, direccion, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.libros_prestados = []

    def mostrar_datos(self):
        print(f"{self.nombre} {self.apellido} DNI {self.dni}")
