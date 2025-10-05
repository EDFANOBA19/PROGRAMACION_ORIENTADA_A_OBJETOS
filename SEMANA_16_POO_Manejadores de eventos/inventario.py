# inventario.py
import json
import producto  # Importa la definición de la clase Producto

class Inventario:
    """
    Clase que gestiona un conjunto de productos como inventario.
    """

    def __init__(self):
        """
        Inicializa un inventario vacío (diccionario de productos).
        """
        self.productos = {}

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario.
        :param producto: instancia de la clase Producto.
        """
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto por su ID.
        :param id_producto: ID del producto a eliminar.
        :return: True si se eliminó, False si no existía.
        """
        if id_producto in self.productos:
            del self.productos[id_producto]
            return True
        return False

    def modificar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        """
        Modifica los atributos de un producto dado su ID.
        :param id_producto: ID del producto a modificar.
        :param nombre: Nuevo nombre (opcional).
        :param cantidad: Nueva cantidad (opcional).
        :param precio: Nuevo precio (opcional).
        :return: True si se modificó, False si no existe producto.
        """
        if id_producto in self.productos:
            producto_instancia = self.productos[id_producto]
            if nombre is not None:
                producto_instancia.set_nombre(nombre)
            if cantidad is not None:
                producto_instancia.set_cantidad(cantidad)
            if precio is not None:
                producto_instancia.set_precio(precio)
            return True
        return False

    def mostrar_productos(self):
        """
        Retorna una lista de strings con la representación de todos los productos.
        """
        return [str(prod) for prod in self.productos.values()]

    def guardar_archivo(self, nombre_archivo):
        """
        Guarda el inventario en un archivo JSON.
        :param nombre_archivo: nombre del archivo.
        """
        lista_guardar = []
        for producto_instancia in self.productos.values():
            lista_guardar.append({
                "id": producto_instancia.get_id(),
                "nombre": producto_instancia.get_nombre(),
                "cantidad": producto_instancia.get_cantidad(),
                "precio": producto_instancia.get_precio()
            })
        with open(nombre_archivo, 'w') as f:
            json.dump(lista_guardar, f, indent=4)

    def cargar_archivo(self, nombre_archivo):
        """
        Carga productos desde un archivo JSON y los agrega al inventario.
        :param nombre_archivo: nombre del archivo.
        """
        try:
            with open(nombre_archivo, 'r') as f:
                lista_cargar = json.load(f)
                self.productos = {}
                for p in lista_cargar:
                    producto_instancia = producto.Producto(p['id'], p['nombre'], p['cantidad'], p['precio'])
                    self.agregar_producto(producto_instancia)
        except FileNotFoundError:
            # Si no existe el archivo, inicializa inventario vacío
            self.productos = {}

    def guardar_archivo_txt(self, nombre_archivo_txt):
        """
        Guarda el inventario en un archivo de texto legible.
        :param nombre_archivo_txt: nombre del archivo.
        """
        with open(nombre_archivo_txt, 'w') as f:
            for producto in self.productos.values():
                linea = (
                    f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, "
                    f"Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}\n"
                )
                f.write(linea)

    def cargar_desde_txt(self, nombre_archivo_txt):
        """
        Carga productos desde un archivo de texto plano con formato esperado.
        :param nombre_archivo_txt: nombre del archivo.
        """
        try:
            with open(nombre_archivo_txt, 'r') as f:
                for linea in f:
                    if linea.strip():
                        # La línea debe tener el formato: ID: ..., Nombre: ..., Cantidad: ..., Precio: ...
                        partes = linea.strip().split(',')
                        id_producto = partes[0].split(':')[1].strip()
                        nombre = partes[1].split(':')[1].strip()
                        cantidad = int(partes[2].split(':')[1].strip())
                        precio = float(partes[3].split(':')[1].strip())
                        producto_instancia = producto.Producto(id_producto, nombre, cantidad, precio)
                        self.agregar_producto(producto_instancia)
        except FileNotFoundError:
            # Si no existe archivo txt, no hace nada
            pass
