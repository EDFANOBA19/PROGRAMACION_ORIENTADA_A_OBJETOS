import tkinter as tk
from tkinter import messagebox

class AplicacionGUI:
    def __init__(self, root):
        # Guardamos la referencia a la ventana principal
        self.root = root
        # Título descriptivo de la ventana
        self.root.title("Gestor Básico de Datos - GUI con tkinter")
        # Tamaño fijo para que la lista sea visible sin scroll
        self.root.geometry("450x350")

        # Etiqueta con instrucciones para el usuario
        self.etiqueta = tk.Label(root, text="Ingrese información y presione 'Agregar'")
        self.etiqueta.pack(pady=10)  # Margen vertical

        # Campo de texto para ingresar datos
        self.entrada_texto = tk.Entry(root, width=50)
        self.entrada_texto.pack(pady=5)  # Margen vertical

        # Frame que contiene los botones para alinearlos horizontalmente
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=5)  # Margen vertical

        # Botón para agregar el texto de entrada a la lista
        self.boton_agregar = tk.Button(frame_botones, text="Agregar", command=self.agregar_elemento)
        self.boton_agregar.pack(side=tk.LEFT, padx=10)  # Separación horizontal

        # Botón "Limpiar" que hace doble función: limpiar campo y eliminar elemento seleccionado
        self.boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=self.limpiar_y_eliminar)
        self.boton_limpiar.pack(side=tk.LEFT, padx=10)  # Separación horizontal

        # Listbox para mostrar los datos que ingresa el usuario
        self.lista_datos = tk.Listbox(root, width=60, height=15)
        self.lista_datos.pack(pady=15)  # Margen vertical para que se vea la lista claramente

    def agregar_elemento(self):
        """
        Obtiene el texto ingresado, si no está vacío:
        - Lo añade al final de la lista.
        - Limpia el campo de texto para nueva entrada.
        Si está vacío muestra advertencia.
        """
        texto = self.entrada_texto.get().strip()  # Eliminar espacios extras
        if texto:  # Si no está vacío
            self.lista_datos.insert(tk.END, texto)  # Añadir texto al final de la lista
            self.entrada_texto.delete(0, tk.END)    # Limpiar campo entrada
        else:
            # Mensaje para avisar que es necesario ingresar texto
            messagebox.showwarning("Campo vacío", "Por favor ingrese algún texto antes de agregar.")

    def limpiar_y_eliminar(self):
        """
        Limpia el campo de texto y elimina el elemento seleccionado de la lista:
        - Siempre limpia la caja de texto.
        - Elimina el item seleccionado si hay alguno.
        """
        self.entrada_texto.delete(0, tk.END)  # Limpiar campo

        seleccion = self.lista_datos.curselection()  # Obtener índice(s) seleccionado(s)
        if seleccion:
            self.lista_datos.delete(seleccion[0])  # Eliminar el primer elemento seleccionado

if __name__ == "__main__":
    ventana = tk.Tk()             # Crear ventana principal Tkinter
    app = AplicacionGUI(ventana) # Instanciar la aplicación con esa ventana
    ventana.mainloop()            # Empezar la escucha de eventos (mostrar ventana)
