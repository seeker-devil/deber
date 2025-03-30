import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

class aplicacion_tareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de tareas")
        self.root.geometry("400x500")

        self.tareas = []  # lista para guardar las tareas

        # Diseño de ventana
        self.frame_principal = ttk.Frame(self.root, padding="10")
        self.frame_principal.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Caja de texto para nueva tarea
        self.entrada_tarea = ttk.Entry(self.frame_principal, width=40)
        self.entrada_tarea.grid(row=0, column=0, columnspan=2, pady=5)
        self.entrada_tarea.bind('<Return>', self.crear_tarea)

        # Botón para crear tarea
        self.btn_crear_tarea = ttk.Button(self.frame_principal, text="Crear Tarea", command=self.crear_tarea)
        self.btn_crear_tarea.grid(row=0, column=2, padx=5, pady=5)

        # Lista de tareas
        self.lista = tk.Listbox(self.frame_principal, width=50, height=20)
        self.lista.grid(row=1, column=0, columnspan=3, pady=10)

        # Botones adicionales
        self.boton_completado = ttk.Button(self.frame_principal, text="Marcar como completada", command=self.marca_completada)
        self.boton_completado.grid(row=2, column=0, padx=5, pady=5)

        self.eliminar = ttk.Button(self.frame_principal, text="Eliminar", command=self.eliminar_tarea)
        self.eliminar.grid(row=2, column=2, padx=5, pady=5)

    def crear_tarea(self, event=None):
        tarea = self.entrada_tarea.get().strip()
        if tarea:
            self.tareas.append({"texto": tarea, "Completada": False})
            texto = tarea
            self.lista.insert(tk.END, texto)
            self.entrada_tarea.delete(0, tk.END)

    def marca_completada(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            self.tareas[index]["Completada"] = not self.tareas[index]["Completada"]
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["Completada"]:
                texto = "✔ " + texto
            self.lista.insert(tk.END, texto)

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            del self.tareas[index]
            self.actualizar_lista()

root = tk.Tk()
app = aplicacion_tareas(root)
root.mainloop()
