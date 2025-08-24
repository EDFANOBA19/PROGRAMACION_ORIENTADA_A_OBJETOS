from inventario import Inventario
from producto import Producto

def mostrar_menu():
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto")
    print("4. Buscar producto(s) por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def pedir_entero(mensaje, permitir_cero=False):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0 or (valor == 0 and not permitir_cero):
                print("Por favor, ingresa un número válido.")
                continue
            return valor
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

def pedir_flotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor, ingresa un número positivo.")
                continue
            return valor
        except ValueError:
            print("Error: Debes ingresar un número válido.")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            print("\n--- Añadir nuevo producto ---")
            id_producto = input("Ingresa ID único: ").strip()
            if inventario.buscar_producto_por_id(id_producto):
                print("Error: Ya existe un producto con ese ID.")
                continue
            nombre = input("Nombre del producto: ").strip()
            cantidad = pedir_entero("Cantidad: ")
            precio = pedir_flotante("Precio: $")
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            print("\n--- Eliminar producto ---")
            id_producto = input("Ingresa el ID del producto a eliminar: ").strip()
            if not inventario.eliminar_producto(id_producto):
                print("No se encontró un producto con ese ID.")

        elif opcion == '3':
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

        elif opcion == '4':
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
            print("\n--- Mostrar todos los productos ---")
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

if __name__ == "__main__":
    main()
