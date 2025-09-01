# Clase Producto representa un producto con ID, nombre, cantidad y precio
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto          # ID único del producto
        self.nombre = nombre           # Nombre del producto
        self.cantidad = cantidad       # Cantidad disponible
        self.precio = precio           # Precio unitario

    def to_dict(self):
        # Convierte el objeto Producto a un diccionario para serialización JSON
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    def __str__(self):
        # Representación en texto para mostrar el producto en consola
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"
