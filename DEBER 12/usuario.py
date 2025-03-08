class Usuario:
    def __init__(self, nombre, id_usuario):
        try:
            self.nombre = nombre
            self.id_usuario = id_usuario
            self.libros_prestados = []  # Lista de libros prestados
        except Exception as e:
            import traceback
            print(f"Error al crear el usuario: {e}")
            traceback.print_exc()

    def agregar_libro(self, libro):
        try:
            self.libros_prestados.append(libro)
        except Exception as e:
            import traceback
            print(f"Error al agregar el libro: {e}")
            traceback.print_exc()

    def devolver_libro(self, libro):
        try:
            if libro in self.libros_prestados:
                self.libros_prestados.remove(libro)
            else:
                print(f"El libro '{libro.titulo}' no está en los libros prestados.")
        except Exception as e:
            import traceback
            print(f"Error al devolver el libro: {e}")
            traceback.print_exc()

    def listar_libros(self):
        return self.libros_prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

    def __repr__(self):
        return self.__str__()
