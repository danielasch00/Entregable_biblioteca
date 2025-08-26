from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario
import sys

def seed_demo_data(biblioteca):
    # datos de prueba
    biblioteca.agregar_libro("Ficciones", "Jorge Luis Borges", "Sur", 1944, 3)
    biblioteca.agregar_libro("El Aleph", "Jorge Luis Borges", "Sur", 1949, 2)
    biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez", "Sudamericana", 1967, 5)
    biblioteca.agregar_libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Sudamericana", 1985, 4)
    biblioteca.agregar_libro("Rayuela", "Julio Cortázar", "Sudamericana", 1963, 3)

    biblioteca.agregar_usuario("Lucía", "Pérez", "30111222", "Av. Siempre Viva 123, Paraná", "343-555-1001")
    biblioteca.agregar_usuario("Lucía", "Gómez", "30111333", "Bv. Racedo 456, Paraná", "343-555-1002")
    biblioteca.agregar_usuario("Martín", "Pérez", "28111222", "Mitre 789, Paraná", "343-555-1003")
    biblioteca.agregar_usuario("Ana", "García", "27111222", "Urquiza 321, Paraná", "343-555-1004")
    biblioteca.agregar_usuario("Juan", "García", "26111222", "Gualeguaychú 654, Paraná", "343-555-1005")

def main():
    biblioteca = Biblioteca()
    seed_demo_data(biblioteca)

    while True:
        print("\nSistema de Gestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Listar libros")
        print("4. Buscar libro")
        print("5. Sección préstamos")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            editorial = input("Ingrese la editorial del libro: ")

            while True:
                dato = input("Ingrese el año de publicación: ")
                try:
                    anio_publicacion = int(dato)
                    break
                except ValueError:
                    print(">>> Valor inválido. Ingrese un número entero para el año.")

            while True:
                dato = input("Ingrese la cantidad de ejemplares: ")
                try:
                    cant_ejemplares = int(dato)
                    break
                except ValueError:
                    print(">>> Valor inválido. Ingrese un número entero para la cantidad.")

            biblioteca.agregar_libro(titulo, autor, editorial, anio_publicacion, cant_ejemplares)
        
        elif opcion == "2":
            titulo = input("Ingrese el título del libro a eliminar: ")
            biblioteca.eliminar_libro(titulo)
        
        elif opcion == "3":
            if len(biblioteca.libros) == 0:
                print(">>> No hay libros cargados.")
            for libro in biblioteca.libros:
                print(libro.MostrarDatos())
        
        elif opcion == "4":
            while True:
                print("1. Buscar por título exacto normalizado")
                print("2. Buscar por autor exacto normalizado")
                print("3. Buscar por editorial exacta normalizada")
                print("4. Volver atrás")
                print("5. Salir")
                opcion2 = input("\nIngresá una opción:")

                if opcion2 == "1":
                    busqueda = input("Ingresá el título: ")
                    biblioteca.buscar_por_titulo(busqueda)

                if opcion2 == "2":
                    busqueda = input("Ingresá el autor: ")
                    biblioteca.buscar_por_autor(busqueda)

                if opcion2 == "3":
                    busqueda = input("Ingresá la editorial: ")
                    biblioteca.buscar_por_editorial(busqueda)

                if opcion2 == "4":
                    break

                if opcion2 == "5":
                    print("¡Hasta luego!")
                    sys.exit()

        elif opcion == "5":
            while True:
                print("1. Registrar usuario")
                print("2. Eliminar usuario")
                print("3. Listar usuarios")
                print("4. Buscar usuario")
                print("5. Prestar libro")
                print("6. Devolución libro")
                print("7. Listar préstamos")  # <- agregado
                print("8. Volver")
                print("9. Salir")                        

                opcion2 = input("\nIngresá una opción:")

                if opcion2 == "1":
                    nombre = input("Ingrese el nombre: ")
                    apellido = input("Ingrese el apellido: ")
                    dni = input("Ingrese el DNI: ").strip()
                    direccion = input("Ingrese la dirección: ")
                    telefono = input("Ingrese el teléfono: ")
                    biblioteca.agregar_usuario(nombre, apellido, dni, direccion, telefono)

                if opcion2 == "2":
                    dni = input("Ingrese el DNI: ").strip()
                    biblioteca.eliminar_usuario(dni)

                if opcion2 == "3":
                    if len(biblioteca.usuarios) == 0:
                        print(">>> No hay usuarios cargados.")
                    for persona in biblioteca.usuarios:
                        persona.mostrar_datos()

                if opcion2 == "4":                            
                    while True:
                        print("1. Buscar por nombre exacto normalizado")
                        print("2. Buscar por apellido exacto normalizado")
                        print("3. Buscar por DNI exacto")
                        print("4. Volver atrás")
                        print("5. Salir")

                        sub = input("\nIngresá una opción:")

                        if sub == "1":
                            busqueda = input("Ingresá el nombre: ")
                            biblioteca.buscar_usuario_nombre(busqueda)

                        if sub == "2":
                            busqueda = input("Ingresá el apellido: ")
                            biblioteca.buscar_usuario_apellido(busqueda)

                        if sub == "3":
                            busqueda = input("Ingresá el DNI: ").strip()
                            biblioteca.buscar_usuario_dni(busqueda)

                        if sub == "4":
                            break

                        if sub == "5":
                            print("¡Hasta luego!")
                            sys.exit()

                if opcion2 == "5":
                    dni = input("Ingrese el DNI del usuario: ").strip()
                    titulo = input("Ingrese el título del libro: ")
                    biblioteca.prestar_libro(dni, titulo)

                if opcion2 == "6":
                    dni = input("Ingrese el DNI del usuario: ").strip()
                    titulo = input("Ingrese el título del libro: ")
                    biblioteca.devolver_libro(dni, titulo)

                if opcion2 == "7":
                    biblioteca.listar_prestamos()

                if opcion2 == "8":
                    break
    
                if opcion2 == "9":
                    print("¡Hasta luego!")
                    sys.exit()
        
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
