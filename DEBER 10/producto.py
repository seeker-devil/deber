# producto.py
class Producto:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre
