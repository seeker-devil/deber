from tkinter import Frame, Label, Button, Entry, Listbox, Scrollbar

class GymApp:
    def __init__(self, master):
        self.master = master
        
        # Crear el marco de la aplicación
        self.frame = Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Crear el título de la aplicación
        self.title_label = Label(self.frame, text="Lista de Ejercicios para el Gimnasio", font=("Arial", 14))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Campo de texto para ingresar ejercicios
        self.entry_label = Label(self.frame, text="Ingresar ejercicio:")
        self.entry_label.grid(row=1, column=0, padx=10, pady=5)

        self.entry = Entry(self.frame)
        self.entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón para agregar el ejercicio
        self.add_button = Button(self.frame, text="Agregar", command=self.agregar_ejercicio)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Lista para mostrar los ejercicios
        self.listbox = Listbox(self.frame, height=10, width=40, selectmode="single")
        self.listbox.grid(row=3, column=0, columnspan=2, pady=5)

        # Agregar barra de desplazamiento a la lista
        self.scrollbar = Scrollbar(self.frame, orient="vertical", command=self.listbox.yview)
        self.scrollbar.grid(row=3, column=2, sticky="ns")
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Botón para limpiar la lista de ejercicios
        self.clear_button = Button(self.frame, text="Limpiar", command=self.limpiar_lista)
        self.clear_button.grid(row=4, column=0, columnspan=2, pady=10)

    def agregar_ejercicio(self):
        """Agregar el ejercicio ingresado en la lista"""
        ejercicio = self.entry.get()
        if ejercicio != "":
            self.listbox.insert("end", ejercicio)
            self.entry.delete(0, "end")  # Limpiar el campo de texto

    def limpiar_lista(self):
        """Limpiar el campo de texto y la lista de ejercicios"""
        self.entry.delete(0, "end")
        self.listbox.delete(0, "end")
