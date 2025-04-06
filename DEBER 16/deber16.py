import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class gestor_tareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("700x700")
        self.tareas = []

        self.style = ttk.Style()
        self.style.configure("Completada.TLabel", foreground="grey")

        self.frame_principal = ttk.Frame(self.root, padding="10")
        self.frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.entrada_tarea = ttk.Entry(self.frame_principal, width=40)
        self.entrada_tarea.grid(row=0, column=0, columnspan=2, pady=5)
        self.entrada_tarea.bind("<Return>", self.anadir_tarea)

        self.btn_tarea = ttk.Button(self.frame_principal, text="Nueva Tarea", command=lambda: self.anadir_tarea(None))
        self.btn_tarea.grid(row=0, column=2, padx=5, pady=5)

        self.frame_lista = ttk.Frame(self.frame_principal)
        self.frame_lista.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)

        self.scrollbar = ttk.Scrollbar(self.frame_lista)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_tareas = tk.Listbox(self.frame_lista, width=50, height=20, yscrollcommand=self.scrollbar.set)
        self.lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.lista_tareas.yview)

        self.frame_botones = ttk.Frame(self.frame_principal)
        self.frame_botones.grid(row=2, column=0, columnspan=3, pady=5)

        self.btn_completa = ttk.Button(self.frame_botones, text="Completa (C)", command=self.marcar_completa)
        self.btn_completa.pack(side=tk.LEFT, padx=5)

        self.btn_eliminar = ttk.Button(self.frame_botones, text="Eliminar (D)", command=self.eliminar_tarea)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

        self.lbl_ayuda = ttk.Label(self.frame_principal, text="Atajos: Enter = Nueva Tarea, C = Completar, D/Delete = Eliminar, Esc = Salir", font=("Arial", 8))
        self.lbl_ayuda.grid(row=3, column=1, columnspan=3, pady=5)

        self.root.bind("<c>", lambda e: self.marcar_completa())
        self.root.bind("<d>", lambda e: self.eliminar_tarea())
        self.root.bind("<Delete>", lambda e: self.eliminar_tarea())
        self.root.bind("<Escape>", lambda e: self.root.quit())

    def anadir_tarea(self, event=None):
        tarea = self.entrada_tarea.get().strip()
        if tarea:
            hora = datetime.now().strftime("%H:%M")
            self.tareas.append({"Texto": tarea, "Completada": False, "Hora": hora})
            self.actualizar_lista()
            self.entrada_tarea.delete(0, tk.END)

    def marcar_completa(self, event=None):
        try:
            index = self.lista_tareas.curselection()[0]
            self.tareas[index]["Completada"] = not self.tareas[index]["Completada"]
            self.actualizar_lista()
        except IndexError:
            pass

    def eliminar_tarea(self, event=None):
        try:
            index = self.lista_tareas.curselection()[0]
            del self.tareas[index]
            self.actualizar_lista()
        except IndexError:
            pass

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            texto = f"[{tarea['Hora']}] {tarea['Texto']}"
            self.lista_tareas.insert(tk.END, texto)
            if tarea["Completada"]:
                self.lista_tareas.itemconfig(tk.END, {'fg': 'grey'})

if __name__ == "__main__":
    root = tk.Tk()
    app = gestor_tareas(root)
    root.mainloop()
