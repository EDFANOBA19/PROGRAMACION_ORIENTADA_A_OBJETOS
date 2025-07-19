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

class Cliente:
    """
    Clase que representa un cliente de la tienda.
    Atributos:
        nombre (str): nombre del cliente
        correo (str): correo electrónico del cliente
    Métodos:
        mostrar_info(): imprime información del cliente
    """
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def mostrar_info(self):
        print(f"Cliente: {self.nombre} | Correo: {self.correo}")

class Pedido:
    """
    Clase que representa un pedido realizado por un cliente.
    Atributos:
        cliente (Cliente): cliente que realiza el pedido
        productos (dict): diccionario con Producto como clave y cantidad como valor
    Métodos:
        agregar_producto(producto, cantidad): añade productos al pedido si hay stock
        mostrar_pedido(): muestra los detalles del pedido y total a pagar
    """
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if producto.actualizar_stock(cantidad):
            if producto in self.productos:
                self.productos[producto] += cantidad
            else:
                self.productos[producto] = cantidad
            print(f"Agregado {cantidad} unidades de {producto.nombre} al pedido.")
        else:
            print(f"No se pudo agregar {producto.nombre} al pedido.")

    def mostrar_pedido(self):
        print(f"Pedido de {self.cliente.nombre}:")
        total = 0
        for producto, cantidad in self.productos.items():
            subtotal = producto.precio * cantidad
            print(f"- {producto.nombre}: {cantidad} x ${producto.precio:.2f} = ${subtotal:.2f}")
            total += subtotal
        print(f"Total a pagar: ${total:.2f}")

# Simulación de uso
if __name__ == "__main__":
    # Crear productos
    p1 = Producto("Camisa", 20.0, 10)
    p2 = Producto("Pantalón", 35.0, 5)

    # Crear cliente
    cliente1 = Cliente("Ana Pérez", "ana.perez@email.com")

    # Crear pedido
    pedido1 = Pedido(cliente1)

    # Agregar productos al pedido
    pedido1.agregar_producto(p1, 2)
    pedido1.agregar_producto(p2, 1)
    pedido1.agregar_producto(p2, 10)  # Intento de agregar más de stock disponible

    # Mostrar pedido
    pedido1.mostrar_pedido()
