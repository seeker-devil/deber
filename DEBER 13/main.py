from tkinter import Tk
from gym_app import GymApp

def main():
    # Crear una ventana principal
    root = Tk()
    root.title("Lista de Ejercicios para el Gimnasio")

    # Crear la aplicación
    app = GymApp(root)
    
    # Iniciar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
