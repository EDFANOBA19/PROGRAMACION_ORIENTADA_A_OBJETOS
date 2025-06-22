class Producto:
    """
    Clase que representa un producto en la tienda.
    Atributos:
        nombre (str): nombre del producto
        precio (float): precio unitario del producto
        stock (int): cantidad disponible en inventario
    Métodos:
        mostrar_info(): imprime información del producto
        actualizar_stock(cantidad): actualiza el stock tras una venta
    """
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}")

    def actualizar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            print(f"No hay suficiente stock de {self.nombre}.")
            return False
