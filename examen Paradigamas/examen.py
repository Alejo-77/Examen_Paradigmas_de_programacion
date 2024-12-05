# Clase base Usuario
class Usuario:
    def __init__(self, nombre, edad, direccion):
        self._nombre = nombre  # Atributo encapsulado
        self._edad = edad  # Atributo encapsulado
        self._direccion = direccion  # Atributo encapsulado

    # Método getter para obtener el nombre (acceso al atributo encapsulado)
    def obtener_nombre(self):
        return self._nombre

    # Método setter para modificar el nombre
    def establecer_nombre(self, nombre):
        self._nombre = nombre

# Clase Catálogo
class Catalogo:
    def __init__(self):
        self.libros = []

    # Método para agregar libros al catálogo
    def agregar_libro(self, libro):
        self.libros.append(libro)

    # Método para mostrar los libros disponibles
    def mostrar_libros_disponibles(self):
        print("Libros disponibles para préstamo:")
        disponibles = [libro for libro in self.libros if libro.disponible]
        if disponibles:
            for index, libro in enumerate(disponibles, 1):
                print(f"{index}. {libro.nombre} - Autor: {libro.autor}")
        else:
            print("No hay libros disponibles actualmente.")

    # Método para obtener un libro disponible por índice
    def obtener_libro_por_indice(self, indice):
        disponibles = [libro for libro in self.libros if libro.disponible]
        if 0 < indice <= len(disponibles):
            return disponibles[indice - 1]
        else:
            print("Índice inválido. El libro no está disponible.")
            return None

    # Método para actualizar el catálogo después de un préstamo
    def actualizar_catalogo(self, libro):
        print(f"Actualizando catálogo: {libro.nombre} ya no está disponible.")

# Clase Libros Disponibles
class LibrosDisponibles:
    def __init__(self, nombre, autor, disponible=True):
        self.nombre = nombre
        self.autor = autor
        self.disponible = disponible

    # Método para mostrar información del libro disponible
    def mostrar_info(self):
        print(f"Libro: {self.nombre}, Autor: {self.autor}, Disponible: {self.disponible}")

# Clase Préstamo
class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.prestado = False

    # Método para realizar un préstamo (polimorfismo)
    def realizar_prestamo(self):
        try:
            if not self.libro.disponible:
                raise ValueError(f"El libro {self.libro.nombre} no está disponible para préstamo.")
            self.prestado = True
            self.libro.disponible = False
            print(f"{self.usuario.obtener_nombre()} ha prestado exitosamente el libro: {self.libro.nombre}")
            # Actualizar catálogo después del préstamo
            catalogo.actualizar_catalogo(self.libro)
            # Imprimir recibo
            self.imprimir_recibo()
        except ValueError as e:
            print(f"Error: {e}")

    # Método para devolver un libro
    def devolver_libro(self):
        try:
            if self.prestado:
                self.prestado = False
                self.libro.disponible = True
                print(f"{self.usuario.obtener_nombre()} ha devuelto el libro: {self.libro.nombre}")
            else:
                raise ValueError("Este libro no ha sido prestado.")
        except ValueError as e:
            print(f"Error: {e}")

    # Método para imprimir recibo
    def imprimir_recibo(self):
        print(f"--- Recibo ---\nUsuario: {self.usuario.obtener_nombre()}\nLibro: {self.libro.nombre}\nAutor: {self.libro.autor}\nFecha: Préstamo realizado")

# Crear objetos de ejemplo
usuario1 = Usuario("Juan Pérez", "22", "Calle Falsa 123")
libro1 = LibrosDisponibles("Programación en Python", "Juan Gómez", disponible=True)
libro2 = LibrosDisponibles("Java para Principiantes", "Carlos López", disponible=True)
libro3 = LibrosDisponibles("Introducción a C++", "Ana Martínez", disponible=False)  # Este libro no está disponible

# Crear catálogo y agregar libros
catalogo = Catalogo()
catalogo.agregar_libro(libro1)
catalogo.agregar_libro(libro2)
catalogo.agregar_libro(libro3)

# Mostrar los libros disponibles
catalogo.mostrar_libros_disponibles()

# El usuario elige un libro para préstamo
try:
    eleccion = int(input("Elige el número del libro que deseas tomar en préstamo: "))
    libro_elegido = catalogo.obtener_libro_por_indice(eleccion)

    if libro_elegido:
        prestamo1 = Prestamo(usuario1, libro_elegido)
        prestamo1.realizar_prestamo()  # Préstamo exitoso
        prestamo1.devolver_libro()  # Devolver el libro
except ValueError:
    print("Por favor, ingresa un número válido.")
