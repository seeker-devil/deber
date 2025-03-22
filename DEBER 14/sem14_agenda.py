import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime

class Agenda:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x600")

        contenedor_principal = tk.Frame(self.root)
        contenedor_principal.pack(pady=10, fill="both", expand=True)

        self.menu_paneles = ttk.Treeview(contenedor_principal, columns=("Fecha", "Hora", "Descripcion"), show="headings")
        self.menu_paneles.heading("Fecha", text="Fecha")
        self.menu_paneles.heading("Hora", text="Hora")
        self.menu_paneles.heading("Descripcion", text="Descripción")
        self.menu_paneles.pack(fill="both", expand=True)

        panel_cajas_texto = tk.Frame(self.root)
        panel_cajas_texto.pack(pady=10)

        tk.Label(panel_cajas_texto, text="Fecha").grid(row=0, column=0, pady=5, sticky="e")
        self.calendario_fechas = DateEntry(panel_cajas_texto, date_pattern="yyyy-mm-dd")
        self.calendario_fechas.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(panel_cajas_texto, text="Hora").grid(row=0, column=2, pady=5, sticky="e")
        self.calendario_horas = tk.Entry(panel_cajas_texto)
        self.calendario_horas.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(panel_cajas_texto, text="Descripción").grid(row=0, column=4, pady=5, sticky="e")
        self.descripcion = tk.Entry(panel_cajas_texto)
        self.descripcion.grid(row=0, column=5, padx=5, pady=5)

        panel_botones = tk.Frame(self.root)
        panel_botones.pack(pady=10)

        tk.Button(panel_botones, text="Agregar Evento", command=self.evento).grid(row=0, column=0, padx=10)

        # Botón para eliminar eventos seleccionados
        tk.Button(panel_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1, padx=10)

        # Botón para salir de la aplicación
        tk.Button(panel_botones, text="Salir", command=self.root.quit).grid(row=0, column=2, padx=10)

    def evento(self):
        fecha = self.calendario_fechas.get()
        hora = self.calendario_horas.get()
        descripcion = self.descripcion.get()

        # Agregada validación de la hora en la función evento
        try:
            datetime.datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Formato de hora incorrecto. Usa HH:MM")
            return

        self.menu_paneles.insert("", "end", values=(fecha, hora, descripcion))
        messagebox.showinfo("Éxito", "Se guardó el evento con éxito")

    def eliminar_evento(self):
        seleccion = self.menu_paneles.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un evento para eliminar")
            return
        
        confirmacion = messagebox.askyesno("Confirmar", "¿Seguro que quieres eliminar este evento?")
        if confirmacion:
            for item in seleccion:
                self.menu_paneles.delete(item)
            messagebox.showinfo("Éxito", "Evento eliminado correctamente")

if __name__ == "__main__":
    root = tk.Tk()
    app = Agenda(root)
    root.mainloop()
