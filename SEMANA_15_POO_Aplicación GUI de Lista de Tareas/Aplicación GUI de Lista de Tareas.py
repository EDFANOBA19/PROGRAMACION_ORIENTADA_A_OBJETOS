import tkinter as tk  # Importa la biblioteca Tkinter para interfaz gráfica
from tkinter import messagebox  # Importa el módulo para cuadros de diálogo

class ListaTareasApp:
    def __init__(self, root):
        """
        Inicializa la ventana principal y todos los widgets de la aplicación.
        """
        self.root = root  # Guarda la referencia a la ventana principal
        self.root.title("Lista de Tareas de Edwin Noriega")  # Establece el título de la ventana

        # Campo Entry para que el usuario escriba nuevas tareas
        self.entry = tk.Entry(root, width=40)
        # Ubica el Entry en la primera fila y primera columna con espacio exterior
        self.entry.grid(row=0, column=0, padx=10, pady=10)
        # Vincula la tecla Enter para agregar tareas al presionar mientras está en el Entry
        self.entry.bind("<Return>", self.agregar_tarea)

        # Botón para añadir tarea, que ejecuta la función agregar_tarea
        self.btn_add = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        # Posición del botón junto al Entry con un pequeño hueco horizontal
        self.btn_add.grid(row=0, column=1, padx=5)

        # Botón para marcar una tarea seleccionada como completada
        self.btn_complete = tk.Button(root, text="Marcar como Completada", command=self.completar_tarea)
        # Se coloca en la segunda fila, primera columna, y ocupa todo el ancho horizontal de la celda
        self.btn_complete.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Botón para eliminar la tarea seleccionada
        self.btn_delete = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        # Ubicación: segunda fila, segunda columna, también con estiramiento horizontal
        self.btn_delete.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Listbox para mostrar la lista visible de tareas con selección simple
        self.lista = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        # Se extiende a lo ancho ocupando dos columnas en la tercera fila
        self.lista.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        # Asigna evento para que al hacer doble clic en una tarea se marque como completada
        self.lista.bind("<Double-1>", self.completar_tarea)

        # Diccionario para almacenar el estado de cada tarea (True = completada, False = pendiente)
        self.tareas = {}

    def agregar_tarea(self, event=None):
        """
        Añade la tarea desde el campo Entry a la lista si el texto no está vacío.
        Limpia el campo después de añadir y avisa si el campo está vacío.
        """
        tarea = self.entry.get().strip()  # Extraer el texto y eliminar espacios laterales
        if tarea:  # Solo si la tarea no está vacía
            self.lista.insert(tk.END, tarea)  # Insertar al final del Listbox
            self.tareas[tarea] = False  # Registrar tarea como no completada
            self.entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            # Mostrar advertencia si el usuario intenta añadir tarea vacía
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def completar_tarea(self, event=None):
        """
        Marca o desmarca la tarea seleccionada como completada.
        Cambia el símbolo y el estilo visual (color gris y texto tachado).
        Si no hay tarea seleccionada informa al usuario.
        """
        seleccion = self.lista.curselection()  # Obtener selección actual en el Listbox
        if seleccion:
            index = seleccion[0]  # Índice seleccionado
            tarea = self.lista.get(index)  # Texto de la tarea
            if not self.tareas.get(tarea, False):
                # Si no está completada, marcarla como completada
                self.tareas[tarea] = True  # Actualiza estado a True
                self.lista.delete(index)  # Borra elemento del Listbox
                texto_completado = f"✔ {tarea}"  # Agrega prefijo de completado
                self.lista.insert(index, texto_completado)  # Reinsertar con símbolo
                # Cambiar estilo visual a gris y texto tachado para claridad visual
                self.lista.itemconfig(index, fg="gray", font=("Arial", 10, "overstrike"))
            else:
                # Si ya estaba completada, revertir a no completada
                self.tareas[tarea] = False  # Estado a False
                self.lista.delete(index)
                texto_normal = tarea.replace("✔ ", "")  # Quitar símbolo
                self.lista.insert(index, texto_normal)
                # Retornar a estilo visual normal (negro y sin tachado)
                self.lista.itemconfig(index, fg="black", font=("Arial", 10, "normal"))
        else:
            # Mensaje al usuario si no seleccionó ninguna tarea
            messagebox.showinfo("Info", "Selecciona una tarea para marcarla.")

    def eliminar_tarea(self):
        """
        Elimina la tarea seleccionada de la lista y del diccionario de estados.
        Muestra mensaje si no hay una tarea seleccionada.
        """
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.lista.get(index).replace("✔ ", "")  # Quitar símbolo si existe
            if tarea in self.tareas:
                del self.tareas[tarea]  # Eliminar del diccionario de estados
            self.lista.delete(index)  # Eliminar del Listbox
        else:
            # Informar que debe seleccionar una tarea para eliminar
            messagebox.showinfo("Info", "Selecciona una tarea para eliminarla.")

if __name__ == "__main__":
    root = tk.Tk()  # Crear ventana principal Tkinter
    app = ListaTareasApp(root)  # Crear instancia de la aplicación
    root.mainloop()  # Ejecutar el bucle principal de eventos
