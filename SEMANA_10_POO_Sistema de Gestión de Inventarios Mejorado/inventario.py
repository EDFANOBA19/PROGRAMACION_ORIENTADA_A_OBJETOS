from producto import Producto
import os

class Inventario:
    archivo = 'inventario.txt'

    def __init__(self):
        self.productos = []
        try:
            self.cargar_desde_archivo()
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print(f"Archivo '{self.archivo}' no encontrado. Creando uno nuevo.")
            with open(self.archivo, 'w', encoding='utf-8') as f:
                pass
        except PermissionError:
            print(f"No tienes permisos para acceder al archivo '{self.archivo}'.")
        except Exception as e:
            print(f"Error al cargar inventario: {e}")

    def agregar_producto(self, producto):
        if self.buscar_producto_por_id(producto.get_id()) is not None:
            return False
        self.productos.append(producto)
        if self.guardar_en_archivo():
            print("Producto agregado y guardado exitosamente.")
            return True
        else:
            print("Error al guardar producto en archivo.")
            return False

    def eliminar_producto(self, id_producto):
        producto = self.buscar_producto_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            if self.guardar_en_archivo():
                print("Producto eliminado y guardado exitosamente.")
                return True
            else:
                print("Error al guardar cambios en archivo.")
                return False
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = self.buscar_producto_por_id(id_producto)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            if self.guardar_en_archivo():
                print("Producto actualizado y guardado exitosamente.")
                return True
            else:
                print("Error al guardar cambios en archivo.")
                return False
        return False

    def buscar_producto_por_id(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                return p
        return None

    def buscar_productos_por_nombre(self, nombre):
        nombre = nombre.lower()
        return [p for p in self.productos if nombre in p.get_nombre().lower()]

    def mostrar_productos(self):
        return self.productos

    def cargar_desde_archivo(self):
        self.productos.clear()
        with open(self.archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split('|')
                if len(partes) != 4:
                    print(f"Línea ignorada por formato incorrecto en archivo: {linea}")
                    continue
                id_producto = partes[0].strip()
                nombre = partes[1].strip()
                try:
                    cantidad = int(partes[2].strip())
                    precio = float(partes[3].strip())
                except ValueError:
                    print(f"Línea ignorada por datos inválidos en cantidad o precio: {linea}")
                    continue
                self.productos.append(Producto(id_producto, nombre, cantidad, precio))

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for p in self.productos:
                    f.write(f"{p.get_id()} | {p.get_nombre()} | {p.get_cantidad()} | {p.get_precio()}\n")
            return True
        except PermissionError:
            print(f"No tienes permisos para escribir en el archivo '{self.archivo}'.")
            return False
        except Exception as e:
            print(f"Error al guardar en archivo: {e}")
            return False
