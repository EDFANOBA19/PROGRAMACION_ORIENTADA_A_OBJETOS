import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        # Inicializa la ventana principal
        self.root = root
        self.root.title("Agenda Personal de Edwin Noriega")
        self.root.geometry("600x400")

        # Frame para contener la lista de eventos
        frame_lista = tk.Frame(root)
        frame_lista.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

        # Crear TreeView con columnas fecha, hora y descripción
        columnas = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(frame_lista, columns=columnas, show='headings')
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Frame para contener campos de entrada
        frame_entrada = tk.Frame(root)
        frame_entrada.pack(fill=tk.X, padx=10, pady=5)

        # Etiqueta y widget DateEntry para seleccionar fecha
        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=2)
        self.entry_fecha = DateEntry(frame_entrada, date_pattern='dd/mm/yyyy')
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=2)

        # Etiqueta y campo Entry para ingresar hora
        tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=2)
        self.entry_hora = tk.Entry(frame_entrada)
        self.entry_hora.grid(row=0, column=3, padx=5, pady=2)

        # Etiqueta y campo Entry para ingresar descripción
        tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=2)
        self.entry_descripcion = tk.Entry(frame_entrada, width=40)
        self.entry_descripcion.grid(row=1, column=1, columnspan=3, padx=5, pady=2)

        # Frame para botones
        frame_botones = tk.Frame(root)
        frame_botones.pack(fill=tk.X, padx=10, pady=10)

        # Botón para agregar evento, asociado al método agregar_evento
        btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar evento seleccionado, asociado al método eliminar_evento
        btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        btn_eliminar.pack(side=tk.LEFT, padx=5)

        # Botón para salir de la aplicación
        btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
        btn_salir.pack(side=tk.RIGHT, padx=5)

    def agregar_evento(self):
        """Agrega un evento nuevo a la lista desde los campos de entrada."""
        fecha = self.entry_fecha.get()  # Obtiene la fecha seleccionada en el selector de fecha
        hora = self.entry_hora.get().strip()  # Obtiene la hora ingresada y elimina espacios extra
        descripcion = self.entry_descripcion.get().strip()  # Obtiene la descripción y elimina espacios extra

        # Validar que los campos hora y descripción no estén vacíos
        if not hora or not descripcion:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
            return

        # Validar formato simple de hora HH:MM
        if len(hora) != 5 or hora[2] != ':' or not (hora[:2].isdigit() and hora[3:].isdigit()):
            messagebox.showwarning("Hora inválida", "Formato de hora debe ser HH:MM (ej. 14:30).")
            return

        # Insertar el evento en la tabla TreeView
        self.tree.insert('', 'end', values=(fecha, hora, descripcion))

        # Limpiar los campos de entrada hora y descripción
        self.entry_hora.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)

    def eliminar_evento(self):
        """Elimina el evento seleccionado tras confirmación."""
        seleccion = self.tree.selection()  # Obtener el elemento seleccionado en el TreeView

        # Si no hay selección, mostrar mensaje informativo
        if not seleccion:
            messagebox.showinfo("Seleccione evento", "No ha seleccionado ningún evento para eliminar.")
            return

        # Confirmar la eliminación con el usuario
        respuesta = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar el evento seleccionado?")
        if respuesta:
            # Eliminar evento(s) seleccionado(s)
            for item in seleccion:
                self.tree.delete(item)

if __name__ == "__main__":
    # Crear ventana principal y ejecutar la aplicación
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
