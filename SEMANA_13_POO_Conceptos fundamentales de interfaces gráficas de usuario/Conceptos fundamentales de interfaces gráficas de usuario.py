import tkinter as tk                   # Importar la librería Tkinter para GUI
from tkinter import messagebox        # Importar módulo para cuadros de diálogo

class AplicacionGUI:
    def __init__(self, root):
        # Configuración ventana principal
        self.root = root
        self.root.title("Gestor Básico de Datos – GUI con Tkinter")  # Título ventana
        self.root.geometry("400x300")                               # Tamaño fijo ventana

        # Crear una etiqueta para instrucciones al usuario
        self.etiqueta = tk.Label(root, text="Ingrese información y agregue a la lista:")
        self.etiqueta.pack(pady=10)  # Empaquetar etiqueta con espacio vertical (padding) de 10

        # Crear un campo de texto para que el usuario escriba la información
        self.entrada_texto = tk.Entry(root, width=40)   # Definir ancho del campo
        self.entrada_texto.pack(pady=5)                  # Empaquetar con padding vertical de 5

        # Crear un frame para colocar los botones en línea horizontal
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=5)                       # Separar verticalmente

        # Botón que activa la función para agregar texto a la lista
        self.boton_agregar = tk.Button(frame_botones,
                                      text="Agregar",
                                      command=self.agregar_elemento)
        self.boton_agregar.pack(side=tk.LEFT, padx=5)   # Empaquetar a la izquierda con margen horizontal

        # Botón que activa la función para limpiar el campo de texto
        self.boton_limpiar = tk.Button(frame_botones,
                                      text="Limpiar",
                                      command=self.limpiar_entrada)
        self.boton_limpiar.pack(side=tk.LEFT, padx=5)   # Al lado del botón anterior

        # Crear la lista que mostrará los datos añadidos por el usuario
        self.lista_datos = tk.Listbox(root, width=50, height=10)
        self.lista_datos.pack(pady=10)                   # Empaquetar la lista con espacio vertical

        # Crear scrollbar y asociarla a la lista para manejar muchos elementos
        self.scrollbar = tk.Scrollbar(self.lista_datos)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)    # Empaquetar scrollbar al lado derecho, llena verticalmente
        self.lista_datos.config(yscrollcommand=self.scrollbar.set)  # Conectar scroll con lista
        self.scrollbar.config(command=self.lista_datos.yview)       # Control de scroll hacia arriba/abajo

    def agregar_elemento(self):
        """
        Función que se ejecuta al presionar el botón "Agregar".
        Obtiene el texto del campo de entrada, valida que no esté vacío,
        lo añade a la lista visual y limpia el campo de texto.
        Si el texto está vacío, muestra advertencia.
        """
        texto = self.entrada_texto.get().strip()  # Extraer texto y quitar espacios al inicio y final
        if texto:
            self.lista_datos.insert(tk.END, texto)  # Agregar al final de la lista el texto ingresado
            self.entrada_texto.delete(0, tk.END)    # Limpiar entrada para próximo dato
        else:
            # Mostrar ventana emergente de advertencia si no se ingresó texto
            messagebox.showwarning("Entrada vacía", "Por favor, ingrese algún texto antes de agregar.")

    def limpiar_entrada(self):
        """
        Función que se ejecuta al presionar el botón "Limpiar".
        Limpia el contenido del campo de entrada dejando la lista intacta.
        """
        self.entrada_texto.delete(0, tk.END)  # Borra el contenido del campo texto desde el inicio hasta el final


if __name__ == "__main__":
    ventana = tk.Tk()         # Crear ventana raíz de Tkinter
    app = AplicacionGUI(ventana)  # Instanciar la clase de la aplicación con esta ventana
    ventana.mainloop()        # Ejecutar bucle principal para mostrar la ventana y responder eventos
