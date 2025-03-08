class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        try:
            self.titulo = titulo
            self.autor = autor
            self.categoria = categoria
            self.isbn = isbn
        except Exception as e:
            import traceback
            print(f"Error al crear el libro: {e}")
            import traceback
            traceback.print_exc()

    def __str__(self):
        return f"ISBN: {self.isbn}, Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}"

    def __repr__(self):
        return self.__str__()
