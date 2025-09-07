# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        """
        Inicializa un libro con título y autor como tupla inmutable,
        categoría e ISBN.
        La tupla (titulo, autor) es inmutable porque estos datos no cambian.
        """
        self.titulo_autor = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        """
        Representación amigable del libro para impresión y debugging.
        """
        return f"'{self.titulo_autor[0]}' por {self.titulo_autor[1]} (ISBN: {self.isbn}, Categoría: {self.categoria})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        """
        Inicializa un usuario con un nombre, un ID único, y una lista vacía para los libros prestados.
        """
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista que guarda objetos Libro prestados

    def listar_libros_prestados(self):
        """
        Devuelve una lista con la representación en string de los libros prestados.
        Si no hay libros prestados, notifica que el usuario no tiene ninguno.
        """
        if not self.libros_prestados:
            return f"{self.nombre} no tiene libros prestados."
        return [str(libro) for libro in self.libros_prestados]

    def __str__(self):
        """
        Representación amigable del usuario para impresión y debugging.
        """
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        """
        Inicializa la biblioteca con:
        - Un diccionario libros donde clave es ISBN y valor es el objeto Libro
        - Un conjunto usuarios_ids para asegurar unicidad de IDs
        - Un diccionario usuarios con clave ID y valor objeto Usuario
        """
        self.libros = {}        # Diccionario para almacenar libros {isbn: Libro}
        self.usuarios_ids = set()  # Conjunto para IDs únicos de usuarios
        self.usuarios = {}      # Diccionario para usuarios {id_usuario: Usuario}

    # Gestión de libros
    def añadir_libro(self, libro):
        """
        Añade un libro al diccionario de libros si no existe ya.
        Retorna mensaje informativo.
        """
        if libro.isbn in self.libros:
            return f"El libro con ISBN {libro.isbn} ya existe."
        self.libros[libro.isbn] = libro
        return f"Libro '{libro.titulo_autor[0]}' añadido a la biblioteca."

    def quitar_libro(self, isbn):
        """
        Quita un libro identificándolo por ISBN.
        Solo permite quitarlo si no está prestado a algún usuario.
        """
        if isbn not in self.libros:
            return f"No existe un libro con ISBN {isbn}."
        # Verificar si libro está prestado
        for usuario in self.usuarios.values():
            if any(libro.isbn == isbn for libro in usuario.libros_prestados):
                return f"El libro con ISBN {isbn} está actualmente prestado y no puede ser eliminado."
        del self.libros[isbn]
        return f"Libro con ISBN {isbn} eliminado de la biblioteca."

    # Gestión de usuarios
    def registrar_usuario(self, usuario):
        """
        Registra un usuario si su ID no está ya en uso.
        """
        if usuario.id_usuario in self.usuarios_ids:
            return f"El ID de usuario {usuario.id_usuario} ya está registrado."
        self.usuarios_ids.add(usuario.id_usuario)
        self.usuarios[usuario.id_usuario] = usuario
        return f"Usuario '{usuario.nombre}' registrado con ID {usuario.id_usuario}."

    def dar_baja_usuario(self, id_usuario):
        """
        Da de baja a un usuario si existe y no tiene libros prestados.
        """
        if id_usuario not in self.usuarios_ids:
            return f"No existe un usuario con ID {id_usuario}."
        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            return f"El usuario tiene libros prestados y no puede ser dado de baja."
        self.usuarios_ids.remove(id_usuario)
        del self.usuarios[id_usuario]
        return f"Usuario con ID {id_usuario} dado de baja."

    # Préstamos y devoluciones
    def prestar_libro(self, id_usuario, isbn):
        """
        Presta un libro identificado por ISBN a un usuario identificado por ID.
        Verifica que el usuario y libro existan y que el libro no esté actualmente prestado.
        """
        if id_usuario not in self.usuarios_ids:
            return f"No existe un usuario con ID {id_usuario}."
        if isbn not in self.libros:
            return f"No existe un libro con ISBN {isbn} en la biblioteca."

        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]

        # Verificar si el libro ya está prestado a cualquier usuario
        for u in self.usuarios.values():
            if libro in u.libros_prestados:
                return f"El libro con ISBN {isbn} ya está prestado a otro usuario."

        usuario.libros_prestados.append(libro)
        return f"Libro '{libro.titulo_autor[0]}' prestado a usuario {usuario.nombre}."

    def devolver_libro(self, id_usuario, isbn):
        """
        Permite la devolución de un libro por parte de un usuario.
        Verifica que el usuario tenga ese libro prestado.
        """
        if id_usuario not in self.usuarios_ids:
            return f"No existe un usuario con ID {id_usuario}."

        usuario = self.usuarios[id_usuario]

        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                return f"Libro '{libro.titulo_autor[0]}' devuelto por usuario {usuario.nombre}."
        return f"El usuario no tiene prestado el libro con ISBN {isbn}."

    # Métodos de búsqueda
    def buscar_por_titulo(self, titulo):
        """
        Retorna una lista de libros cuyo título contenga el texto buscado (no sensible a mayúsculas).
        """
        resultados = [libro for libro in self.libros.values() if titulo.lower() in libro.titulo_autor[0].lower()]
        if not resultados:
            return "No se encontraron libros con ese título."
        return [str(libro) for libro in resultados]

    def buscar_por_autor(self, autor):
        """
        Retorna una lista de libros cuyo autor contenga el texto buscado (no sensible a mayúsculas).
        """
        resultados = [libro for libro in self.libros.values() if autor.lower() in libro.titulo_autor[1].lower()]
        if not resultados:
            return "No se encontraron libros con ese autor."
        return [str(libro) for libro in resultados]

    def buscar_por_categoria(self, categoria):
        """
        Retorna una lista de libros cuya categoría coincida exactamente (no sensible a mayúsculas).
        """
        resultados = [libro for libro in self.libros.values() if libro.categoria.lower() == categoria.lower()]
        if not resultados:
            return "No se encontraron libros en esa categoría."
        return [str(libro) for libro in resultados]

    # Listar libros prestados de un usuario
    def listar_libros_prestados_usuario(self, id_usuario):
        """
        Muestra los libros que tiene prestados un usuario dado su ID, o mensaje si no tiene.
        """
        if id_usuario not in self.usuarios_ids:
            return f"No existe un usuario con ID {id_usuario}."
        usuario = self.usuarios[id_usuario]
        return usuario.listar_libros_prestados()

# Pruebas del Sistema de Biblioteca con salidas claras

# Crear la instancia de la biblioteca
biblioteca = Biblioteca()

# Crear algunos libros (título, autor, categoría, ISBN)
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "1234567890")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "1234567891")
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", "1234567892")

# Añadir libros a la biblioteca
print("---- Añadir Libros ----")
print(biblioteca.añadir_libro(libro1))
print(biblioteca.añadir_libro(libro2))
print(biblioteca.añadir_libro(libro3))
print(biblioteca.añadir_libro(libro1))  # Intento de añadir libro duplicado
print()

# Mostrar todos los libros disponibles (estado)
print("---- Libros Disponibles en Biblioteca ----")
for libro in biblioteca.libros.values():
    # Verifica si el libro está prestado a algún usuario
    prestado = any(libro in u.libros_prestados for u in biblioteca.usuarios.values())
    estado = "Prestado" if prestado else "Disponible"
    print(f"{libro} - {estado}")
print()

# Registrar usuarios
print("---- Registrar Usuarios ----")
usuario1 = Usuario("Ana Pérez", "user001")
usuario2 = Usuario("Juan López", "user002")

print(biblioteca.registrar_usuario(usuario1))
print(biblioteca.registrar_usuario(usuario2))
print(biblioteca.registrar_usuario(usuario1))  # Intento con ID repetido
print()

# Prestar libros a usuarios
print("---- Préstamos de Libros ----")
print(biblioteca.prestar_libro("user001", "1234567890"))  # Ana presta Cien Años de Soledad
print(biblioteca.prestar_libro("user002", "1234567890"))  # Juan intenta préstamo ya ocupado
print(biblioteca.prestar_libro("user002", "1234567891"))  # Juan presta El Principito
print()

# Mostrar libros prestados por usuario
print("---- Libros Prestados por Usuario ----")
for id_user in biblioteca.usuarios_ids:
    libros = biblioteca.listar_libros_prestados_usuario(id_user)
    if isinstance(libros, list):
        print(f"Usuario {biblioteca.usuarios[id_user].nombre} tiene prestados:")
        for l in libros:
            print("  -", l)
    else:
        print(libros)
print()

# Búsquedas en la biblioteca
print("---- Búsqueda de Libros ----")
print("Buscar por título 'Don':", biblioteca.buscar_por_titulo("Don"))
print("Buscar por autor 'Gabriel':", biblioteca.buscar_por_autor("Gabriel"))
print("Buscar por categoría 'Novela':", biblioteca.buscar_por_categoria("Novela"))
print()

# Devolver libros
print("---- Devolución de Libros ----")
print(biblioteca.devolver_libro("user001", "1234567890"))  # Ana devuelve su libro
print(biblioteca.devolver_libro("user002", "1234567890"))  # Juan intenta devolver libro no prestado
print()

# Dar de baja usuarios
print("---- Dar de Baja Usuarios ----")
print(biblioteca.dar_baja_usuario("user001"))  # Ana se puede dar de baja sin libros prestados
print(biblioteca.dar_baja_usuario("user002"))  # Juan aún tiene libro prestado, no puede darse de baja
print()

# Intentar quitar libros prestados y no prestados
print("---- Quitar Libros ----")
print(biblioteca.quitar_libro("1234567891"))  # El Principito está prestado a Juan, no se elimina
print(biblioteca.devolver_libro("user002", "1234567891"))  # Juan devuelve el libro
print(biblioteca.quitar_libro("1234567891"))  # Ahora sí se puede eliminar
print()

# Estado final de libros y usuarios
print("---- Estado Final de Libros en Biblioteca ----")
for libro in biblioteca.libros.values():
    prestado = any(libro in u.libros_prestados for u in biblioteca.usuarios.values())
    estado = "Prestado" if prestado else "Disponible"
    print(f"{libro} - {estado}")
print()

print("---- Usuarios Registrados Actualmente ----")
for usuario in biblioteca.usuarios.values():
    print(f"{usuario} con libros prestados: {len(usuario.libros_prestados)}")
