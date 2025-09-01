import json
import os
from producto import Producto  # Importa la clase Producto

# Clase Inventario maneja la colección de productos y el almacenamiento en archivo
class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo          # Archivo donde se guarda el inventario
        self.productos = {}             # Diccionario de productos: clave=ID, valor=Producto
        self.cargar_desde_archivo()    # Carga productos desde archivo al iniciar

    def cargar_desde_archivo(self):
        # Si archivo no existe, crea uno vacío para comenzar
        if not os.path.exists(self.archivo):
            self.productos = {}
            self.guardar_en_archivo()
            return
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                contenido = f.read().strip()
                # Si archivo vacío, iniciar inventario vacío
                if not contenido:
                    self.productos = {}
                else:
                    # Cargar lista JSON y convertir a diccionario de Productos
                    lista_dicts = json.loads(contenido)
                    self.productos = {p['id']: Producto(p['id'], p['nombre'], p['cantidad'], p['precio']) for p in lista_dicts}
        except (json.JSONDecodeError, FileNotFoundError):
            # Si hay error lectura, crear inventario vacío para evitar fallo
            self.productos = {}
            self.guardar_en_archivo()

    def guardar_en_archivo(self):
        # Convierte los Productos a diccionarios y guarda como JSON indentado en archivo texto
        lista_dicts = [p.to_dict() for p in self.productos.values()]
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(lista_dicts, f, indent=4)

    def añadir_producto(self, producto):
        # Agrega un nuevo producto si su ID no existe
        if producto.id in self.productos:
            raise KeyError(f"Producto con ID '{producto.id}' ya existe.")
        self.productos[producto.id] = producto
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        # Elimina producto por su ID si existe
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
        else:
            raise KeyError(f"No existe producto con ID '{id_producto}'.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualiza cantidad o precio del producto indicado
        if id_producto not in self.productos:
            raise KeyError(f"No existe producto con ID '{id_producto}'.")
        if cantidad is not None:
            self.productos[id_producto].cantidad = cantidad
        if precio is not None:
            self.productos[id_producto].precio = precio
        self.guardar_en_archivo()

    def buscar_por_nombre(self, nombre):
        # Busca productos cuyo nombre contiene el texto indicado (case insensitive)
        nombre_lower = nombre.lower()
        return [p for p in self.productos.values() if nombre_lower in p.nombre.lower()]

    def mostrar_todos(self):
        # Muestra todos los productos presentes en el inventario
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("Productos en inventario:")
            for p in self.productos.values():
                print(p)
