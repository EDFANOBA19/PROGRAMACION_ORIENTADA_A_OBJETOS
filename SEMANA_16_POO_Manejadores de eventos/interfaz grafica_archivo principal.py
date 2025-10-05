import tkinter as tk
from tkinter import ttk, messagebox
from inventario import Inventario
from producto import Producto

class AplicacionInventario(tk.Tk):
    """
    Ventana principal de la aplicación para gestionar el inventario.
    Contiene el menú principal y despliega la ventana de productos.
    """

    def __init__(self):
        super().__init__()

        self.title("Sistema de Gestión de Inventario_POO_UEA")
        self.geometry("700x500")

        # Inicializar inventario y cargar datos desde archivos
        self.inventario = Inventario()
        self.inventario.cargar_desde_txt("inventario.txt")
        self.inventario.cargar_archivo("inventario.json")
        self.inventario.guardar_archivo_txt("inventario.txt")

        # Mostrar la información de dos estudiantes en la ventana principal
        estudiante1 = "Nombre: EDWIN NORIEGA | Carrera: Tecnologias de la Informacion | Paralelo: A"
        estudiante2 = "Nombre: DIANA RAMON | Carrera: Tecnologias de la Informacion | Paralelo: A"
        label_estudiante1 = tk.Label(self, text=estudiante1, font=("Arial", 14))
        label_estudiante2 = tk.Label(self, text=estudiante2, font=("Arial", 14))
        label_estudiante1.pack(pady=5)
        label_estudiante2.pack(pady=5)

        # Configurar menú principal
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        menu_opciones = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Opciones", menu=menu_opciones)
        menu_opciones.add_command(label="Productos", command=self.abrir_ventana_productos)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Salir", command=self.salir_aplicacion)

        self.ventana_productos = None  # Referencia ventana modal

        # Atajo para salir con ESC
        self.bind("<Escape>", lambda e: self.salir_aplicacion())

    def abrir_ventana_productos(self):
        """
        Abre la ventana de gestión de productos.
        Si la ventana ya está abierta, la trae al frente y la bloquea modalmente.
        """
        if self.ventana_productos is None or not tk.Toplevel.winfo_exists(self.ventana_productos):
            self.ventana_productos = VentanaProductos(self, self.inventario)
            self.ventana_productos.resizable(False, False)
            self.ventana_productos.grab_set()  # Modal: fija encima y bloquea ventana principal
            self.ventana_productos.focus_set()
        else:
            self.ventana_productos.lift()
            self.ventana_productos.focus_set()

    def salir_aplicacion(self):
        """
        Guarda el inventario antes de salir con confirmación.
        """
        if messagebox.askokcancel("Salir", "¿Está seguro que desea salir? Se guardarán los cambios."):
            self.inventario.guardar_archivo("inventario.json")
            self.inventario.guardar_archivo_txt("inventario.txt")
            self.destroy()

class VentanaProductos(tk.Toplevel):
    """
    Ventana para gestionar productos: agregar, modificar, eliminar y listar.
    """

    def __init__(self, padre, inventario):
        super().__init__(padre)
        self.inventario = inventario
        self.title("Gestión de Productos")
        self.geometry("650x450")

        # Campos de entrada para productos
        self.label_id = tk.Label(self, text="ID Producto:")
        self.entry_id = tk.Entry(self)
        self.label_nombre = tk.Label(self, text="Nombre:")
        self.entry_nombre = tk.Entry(self)
        self.label_cantidad = tk.Label(self, text="Cantidad:")
        self.entry_cantidad = tk.Entry(self)
        self.label_precio = tk.Label(self, text="Precio:")
        self.entry_precio = tk.Entry(self)

        # Ubicar campos usando grid
        self.label_id.grid(row=0, column=0, padx=5, pady=5)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)
        self.label_nombre.grid(row=1, column=0, padx=5, pady=5)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=5)
        self.entry_cantidad.grid(row=2, column=1, padx=5, pady=5)
        self.label_precio.grid(row=3, column=0, padx=5, pady=5)
        self.entry_precio.grid(row=3, column=1, padx=5, pady=5)

        # Botones para acciones
        self.boton_agregar = tk.Button(self, text="Agregar", command=self.agregar_producto)
        self.boton_modificar = tk.Button(self, text="Modificar", command=self.modificar_producto)
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_producto)
        self.boton_listar = tk.Button(self, text="Listar Productos", command=self.listar_productos)

        self.boton_agregar.grid(row=4, column=0, padx=5, pady=5)
        self.boton_modificar.grid(row=4, column=1, padx=5, pady=5)
        self.boton_eliminar.grid(row=4, column=2, padx=5, pady=5)
        self.boton_listar.grid(row=4, column=3, padx=5, pady=5)

        # Treeview para mostrar productos
        self.tree = ttk.Treeview(self, columns=("ID", "Nombre", "Cantidad", "Precio"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Precio", text="Precio")
        self.tree.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        # Scrollbar para la tabla
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=5, column=4, sticky='ns')

        # Configurar expansibilidad del grid
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # Atajo Delete para eliminar producto seleccionado
        self.bind("<Delete>", lambda e: self.eliminar_producto())

        # Mostrar productos al abrir ventana
        self.listar_productos()

    def limpiar_campos(self):
        """ Limpia todos los campos de entrada """
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)

    def agregar_producto(self):
        """ Agrega un producto con datos ingresados, validando entradas """
        try:
            id_producto = self.entry_id.get().strip()
            nombre = self.entry_nombre.get().strip()
            cantidad = int(self.entry_cantidad.get())
            precio = float(self.entry_precio.get())

            if not id_producto or not nombre:
                messagebox.showerror("Error", "ID y Nombre son obligatorios.")
                return

            if id_producto in self.inventario.productos:
                messagebox.showerror("Error", "ID ya existe en inventario.")
                return

            producto = Producto(id_producto, nombre, cantidad, precio)
            self.inventario.agregar_producto(producto)
            self.listar_productos()
            self.limpiar_campos()

            # Guardar cambios
            self.inventario.guardar_archivo("inventario.json")
            self.inventario.guardar_archivo_txt("inventario.txt")

        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser entero y Precio un número.")

    def modificar_producto(self):
        """ Modifica el producto con ID especificado con nuevos datos """
        try:
            id_producto = self.entry_id.get().strip()
            nombre = self.entry_nombre.get().strip()
            cantidad = int(self.entry_cantidad.get())
            precio = float(self.entry_precio.get())

            if not id_producto:
                messagebox.showerror("Error", "ID es obligatorio para modificar.")
                return

            modificado = self.inventario.modificar_producto(id_producto, nombre, cantidad, precio)
            if modificado:
                self.listar_productos()
                self.limpiar_campos()

                # Guardar cambios
                self.inventario.guardar_archivo("inventario.json")
                self.inventario.guardar_archivo_txt("inventario.txt")
            else:
                messagebox.showerror("Error", "Producto no encontrado.")
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser entero y Precio un número.")

    def eliminar_producto(self):
        """ Elimina el producto seleccionado en la tabla """
        try:
            id_producto = self.tree.item(self.tree.selection()[0])['values'][0]
        except IndexError:
            messagebox.showerror("Error", "Seleccione un producto para eliminar.")
            return

        confirmado = messagebox.askyesno("Confirmar", f"¿Eliminar producto {id_producto}?")
        if confirmado:
            eliminado = self.inventario.eliminar_producto(id_producto)
            if eliminado:
                self.listar_productos()
                self.limpiar_campos()

                # Guardar cambios
                self.inventario.guardar_archivo("inventario.json")
                self.inventario.guardar_archivo_txt("inventario.txt")
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto.")

    def listar_productos(self):
        """ Lista los productos en la tabla """
        for item in self.tree.get_children():
            self.tree.delete(item)
        for prod in self.inventario.productos.values():
            self.tree.insert("", tk.END, values=(prod.get_id(), prod.get_nombre(), prod.get_cantidad(), prod.get_precio()))

if __name__ == "__main__":
    app = AplicacionInventario()
    app.mainloop()
