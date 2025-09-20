import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame para la lista de eventos
        frame_lista = tk.Frame(root)
        frame_lista.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

        # TreeView con columnas fecha, hora y descripcion
        columnas = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(frame_lista, columns=columnas, show='headings')
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Frame para campos de entrada
        frame_entrada = tk.Frame(root)
        frame_entrada.pack(fill=tk.X, padx=10, pady=5)

        # Etiquetas y campos de entrada
        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=2)
        self.entry_fecha = DateEntry(frame_entrada, date_pattern='dd/mm/yyyy')
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=2)
        self.entry_hora = tk.Entry(frame_entrada)
        self.entry_hora.grid(row=0, column=3, padx=5, pady=2)

        tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=2)
        self.entry_descripcion = tk.Entry(frame_entrada, width=40)
        self.entry_descripcion.grid(row=1, column=1, columnspan=3, padx=5, pady=2)

        # Frame para botones
        frame_botones = tk.Frame(root)
        frame_botones.pack(fill=tk.X, padx=10, pady=10)

        # Botones
        btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.pack(side=tk.LEFT, padx=5)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        btn_eliminar.pack(side=tk.LEFT, padx=5)

        btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
        btn_salir.pack(side=tk.RIGHT, padx=5)

    def agregar_evento(self):
        """Agrega un evento nuevo a la lista desde los campos de entrada."""
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get().strip()
        descripcion = self.entry_descripcion.get().strip()

        # Validar campos
        if not hora or not descripcion:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
            return

        # Validar formato hora HH:MM simple
        if len(hora) != 5 or hora[2] != ':' or not (hora[:2].isdigit() and hora[3:].isdigit()):
            messagebox.showwarning("Hora inválida", "Formato de hora debe ser HH:MM (ej. 14:30).")
            return

        # Agregar al TreeView
        self.tree.insert('', 'end', values=(fecha, hora, descripcion))

        # Limpiar campos (excepto fecha)
        self.entry_hora.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)

    def eliminar_evento(self):
        """Elimina el evento seleccionado tras confirmación."""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Seleccione evento", "No ha seleccionado ningún evento para eliminar.")
            return

        respuesta = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar el evento seleccionado?")
        if respuesta:
            for item in seleccion:
                self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
