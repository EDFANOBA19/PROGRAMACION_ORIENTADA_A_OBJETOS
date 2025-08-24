class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    # Aquí deberías parsear cada línea para crear objetos producto, simplifico
                    self.productos.append(linea.strip())
            print(f"Archivo '{self.archivo}' cargado exitosamente.")
        except FileNotFoundError:
            print(f"Archivo '{self.archivo}' no encontrado. Creando archivo nuevo.")
            # Crear archivo vacío
            with open(self.archivo, 'w', encoding='utf-8') as f:
                pass
        except PermissionError:
            print(f"Sin permiso para leer el archivo '{self.archivo}'.")

    def agregar_producto(self, producto):
        self.productos.append(producto)
        try:
            with open(self.archivo, 'a', encoding='utf-8') as f:
                f.write(producto + '\n')
            print("Producto agregado y guardado correctamente.")
        except PermissionError:
            print(f"Sin permiso para escribir en el archivo '{self.archivo}'.")

# Uso
inv = Inventario()
inv.agregar_producto("P001 | Manzanas | 50 | 0.5")
