# producto.py

class Producto:
    """
    Clase que representa un producto con ID, nombre, cantidad y precio.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Inicializa un nuevo producto.
        :param id_producto: Identificador único del producto (string o int).
        :param nombre: Nombre del producto (string).
        :param cantidad: Cantidad disponible en inventario (int).
        :param precio: Precio unitario del producto (float).
        """
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Métodos para obtener los atributos
    def get_id(self):
        return self._id_producto

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Métodos para modificar los atributos
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad):
        self._cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self._precio = nuevo_precio

    def __str__(self):
        """
        Representación en forma de cadena del producto, útil para mostrar en listas o impresiones.
        """
        return f"ID: {self._id_producto}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"
