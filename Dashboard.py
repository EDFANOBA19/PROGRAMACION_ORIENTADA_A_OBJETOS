import os
import subprocess

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/c', 'start', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    # Ruta base EXACTA a tu carpeta principal
    ruta_base_proyecto = r"C:\Users\hp\PycharmProjects\PROGRAMACION_ORIENTADA_A_OBJETOS"

    # Carpetas/semanas según tu estructura
    semanas = {
        "1": "EJERCICIO EN CLASE SEMANA 07",
        "2": "SEMANA_2_POO_PILARES DE PROGRAMACION ORIENTADA A OBJETOS",
        "3": "SEMANA_3_POO_Comparación_de_Programación_Tradicional_y_POO_en_Python",
        "4": "SEMANA_4_POO_EJEMPLOMUNDOREAL",
        "5": "SEMANA_5_POO_Tipos de datos, Identificadores",
        "6": "SEMANA_6_POO_Clases, objetos, herencia, encapsulamiento y polimorfismo",
        "7": "SEMANA_7_POO_Constructores y Destructores",
        "8": "CAPTURAS SEMANA 8"
    }

    while True:
        print("\nMenú Principal - Navegación por Semanas")
        for key, value in semanas.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion = input("Elige una semana (por su número) o '0' para salir: ")

        if eleccion == '0':
            print("Saliendo del programa.")
            break
        elif eleccion in semanas:
            nombre_carpeta_semana = semanas[eleccion]
            ruta_carpeta_semana = os.path.join(ruta_base_proyecto, nombre_carpeta_semana)

            if os.path.isdir(ruta_carpeta_semana):
                mostrar_scripts(ruta_carpeta_semana)
            else:
                print(f"Error: La carpeta '{nombre_carpeta_semana}' no se encontró en:\n  {ruta_base_proyecto}")
                print("Verifica que la ruta sea correcta (puedes modificar ruta_base_proyecto al inicio del script si es necesario).")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    if not scripts:
        print(f"No se encontraron scripts Python (.py) en '{ruta_sub_carpeta}'.")
        input("Presiona Enter para regresar al menú principal.")
        return

    while True:
        print(f"\nScripts en {os.path.basename(ruta_sub_carpeta)} - Selecciona un script para ver y ejecutar")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al menú principal")

        eleccion_script = input("Elige un script o '0' para regresar al menú principal: ")
        if eleccion_script == '0':
            break
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
