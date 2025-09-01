from producto import Producto
from inventario import Inventario

def menu():
    inventario = Inventario()  # Crear instancia de inventario
    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto")
        print("4. Buscar productos por nombre")
        print("5. Mostrar todos los productos")
        print("0. Guardar y Salir")
        opcion = input("Seleccione opción: ").strip()

        try:
            if opcion == '1':
                id_prod = input("ID (único): ").strip()
                nombre = input("Nombre: ").strip()
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                p = Producto(id_prod, nombre, cantidad, precio)
                inventario.añadir_producto(p)
                print("Producto añadido exitosamente.")
            elif opcion == '2':
                id_prod = input("ID del producto a eliminar: ").strip()
                inventario.eliminar_producto(id_prod)
                print("Producto eliminado con éxito.")
            elif opcion == '3':
                id_prod = input("ID del producto a actualizar: ").strip()
                cantidad_input = input("Nueva cantidad (deje vacío para no modificar): ").strip()
                precio_input = input("Nuevo precio (deje vacío para no modificar): ").strip()
                cantidad = int(cantidad_input) if cantidad_input else None
                precio = float(precio_input) if precio_input else None
                inventario.actualizar_producto(id_prod, cantidad, precio)
                print("Producto actualizado.")
            elif opcion == '4':
                nombre = input("Nombre o parte del nombre para buscar: ").strip()
                resultados = inventario.buscar_por_nombre(nombre)
                if resultados:
                    print(f"Se encontraron {len(resultados)} productos:")
                    for p in resultados:
                        print(p)
                else:
                    print("No se encontraron productos.")
            elif opcion == '5':
                inventario.mostrar_todos()
            elif opcion == '0':
                print("Guardando y Saliendo del programa.")
                break
            else:
                print("Opción inválida, intente de nuevo.")
        except ValueError:
            print("Error: cantidad y precio deben ser números válidos.")
        except KeyError as e:
            print(e)

if __name__ == "__main__":
    menu()
