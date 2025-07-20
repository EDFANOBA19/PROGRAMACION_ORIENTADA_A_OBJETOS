# SISTEMA DE GESTION DE INVENTARIOS

# Clase Producto que representa un producto individual en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Uso atributos “privados” con _ para promover encapsulación
        self._id = id_producto          # ID único del producto, se asume que es string para mayor flexibilidad
        self._nombre = nombre           # Nombre descriptivo del producto
        self._cantidad = cantidad       # Cantidad disponible en inventario (int)
        self._precio = precio           # Precio unitario del producto (float)

    # Métodos getters para acceder a atributos privados
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Métodos setters para modificar atributos (excepto ID que es único e inmutable)
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    # Método especial para presentar el producto en forma legible (útil para mostrar en consola)
    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"

# Clase Inventario que agrupa y gestiona una colección de objetos Producto
class Inventario:
    def __init__(self):
        self.productos = []  # Lista que almacenará objetos Producto

    # Añadir producto al inventario siempre que el ID no exista (para evitar duplicados)
    def agregar_producto(self, producto):
        if self.buscar_producto_por_id(producto.get_id()) is not None:
            return False  # No se añade si ya existe un producto con dicho ID
        self.productos.append(producto)
        return True

    # Eliminar producto mediante identificador único
    def eliminar_producto(self, id_producto):
        producto = self.buscar_producto_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            return True
        return False

    # Actualizar cantidad y/o precio del producto identificado por su ID
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = self.buscar_producto_por_id(id_producto)
        if producto:
            # Solo actualizamos si se pasa un nuevo valor válido para cada atributo
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            return True
        return False

    # Buscar producto por ID único (retorna objeto Producto o None si no existe)
    def buscar_producto_por_id(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None

    # Buscar productos que contengan un texto en su nombre (búsqueda insensible a mayúsculas)
    def buscar_productos_por_nombre(self, nombre):
        nombre = nombre.lower()
        return [p for p in self.productos if nombre in p.get_nombre().lower()]

    # Devuelve lista con todos los productos almacenados para mostrar
    def mostrar_productos(self):
        return self.productos

# Función para mostrar menú interactivo de opciones disponibles al usuario
def mostrar_menu():
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto")
    print("4. Buscar producto(s) por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

# Función para pedir un número entero positivo al usuario con validación
def pedir_entero(mensaje, permitir_cero=False):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0 or (valor == 0 and not permitir_cero):
                print("Por favor, ingresa un número válido.")
                continue
            return valor
        except ValueError:
            print("Error: debes ingresar un número entero.")

# Función para pedir un número flotante positivo, con validación, para precios por ejemplo
def pedir_flotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor, ingresa un número positivo.")
                continue
            return valor
        except ValueError:
            print("Error: debes ingresar un número válido.")

def main():
    inventario = Inventario()

    # Agrego productos de ejemplo para facilitar pruebas sin entrada constante del usuario
    productos_ejemplo = [
        Producto("P001", "Manzanas", 50, 0.5),
        Producto("P002", "Naranjas", 75, 0.75),
        Producto("P003", "Leche", 30, 1.25),
        Producto("P004", "Pan", 100, 0.8),
        Producto("P005", "Huevos", 200, 0.1),
    ]
    for p in productos_ejemplo:
        inventario.agregar_producto(p)

    print("Sistema iniciado con productos de ejemplo.\n")

    # Bucle principal que muestra el menú y atiende la opción seleccionada
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Añadir nuevo producto, confirmando que el ID es único para mantener integridad
            print("\n--- Añadir nuevo producto ---")
            id_producto = input("Ingresa ID único: ").strip()
            if inventario.buscar_producto_por_id(id_producto):
                print("Error: ya existe un producto con ese ID.")
                continue
            nombre = input("Nombre del producto: ").strip()
            cantidad = pedir_entero("Cantidad: ")
            precio = pedir_flotante("Precio: $")
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            print("Producto agregado correctamente.")

        elif opcion == '2':
            # Eliminar producto por su ID único, mostrando mensaje según resultado
            print("\n--- Eliminar producto ---")
            id_producto = input("Ingresa el ID del producto a eliminar: ").strip()
            if inventario.eliminar_producto(id_producto):
                print("Producto eliminado correctamente.")
            else:
                print("No se encontró un producto con ese ID.")

        elif opcion == '3':
            # Actualizar cantidad y/o precio, permitiendo dejar campos vacíos para no actualizar
            print("\n--- Actualizar producto ---")
            id_producto = input("ID del producto a actualizar: ").strip()
            producto = inventario.buscar_producto_por_id(id_producto)
            if producto is None:
                print("No se encontró un producto con ese ID.")
                continue
            print(f"Producto actual: {producto}")
            print("Deja en blanco el campo que no deseas actualizar.")
            cantidad_input = input("Nueva cantidad: ")
            precio_input = input("Nuevo precio: $")
            cantidad = None
            precio = None
            if cantidad_input != "":
                try:
                    cantidad = int(cantidad_input)
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa.")
                        continue
                except ValueError:
                    print("Cantidad inválida.")
                    continue
            if precio_input != "":
                try:
                    precio = float(precio_input)
                    if precio < 0:
                        print("El precio no puede ser negativo.")
                        continue
                except ValueError:
                    print("Precio inválido.")
                    continue
            if cantidad is None and precio is None:
                print("No actualizaste ningún dato.")
                continue
            inventario.actualizar_producto(id_producto, cantidad, precio)
            print("Producto actualizado correctamente.")

        elif opcion == '4':
            # Búsqueda parcial por nombre para permitir encontrar varios productos similares
            print("\n--- Buscar productos por nombre ---")
            nombre_busqueda = input("Ingresa parte o todo el nombre: ").strip()
            resultados = inventario.buscar_productos_por_nombre(nombre_busqueda)
            if resultados:
                print(f"Se encontraron {len(resultados)} producto(s):")
                for prod in resultados:
                    print(prod)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            # Mostrar todo el inventario, o notificar que está vacío
            print("\n--- Lista de todos los productos ---")
            productos = inventario.mostrar_productos()
            if productos:
                for prod in productos:
                    print(prod)
            else:
                print("El inventario está vacío.")

        elif opcion == '6':
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

# Punto de entrada del programa, garantiza que main() se ejecute solo si este archivo corre directamente
if __name__ == "__main__":
    main()
