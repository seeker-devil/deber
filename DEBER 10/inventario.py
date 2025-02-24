# inventario.py
import traceback
import os
from producto import Producto

class Inventario:
    def __init__(self, nombrearchivo="inventario"):
        self.productos = []
        self.nombrearchivo = nombrearchivo
        self.cargar_inventario()

    def cargar_inventario(self):
        """Cargar el inventario desde el archivo de texto"""
        try:
            if os.path.exists(self.nombrearchivo + ".txt"):  # Verificamos si el archivo existe
                with open(self.nombrearchivo + ".txt", "r") as archivo:
                    for line in archivo:
                        id, nombre = line.strip().split(",")  # ID y nombre del producto
                        producto = Producto(id, nombre)
                        self.productos.append(producto)
                print("Inventario cargado exitosamente.")
            else:
                print(f"El archivo {self.nombrearchivo}.txt no existe, se creará uno nuevo.")
        except FileNotFoundError:
            print(f"Error: El archivo {self.nombrearchivo}.txt no fue encontrado.")
        except PermissionError:
            print(f"Error: No se tienen permisos suficientes para leer el archivo {self.nombrearchivo}.txt.")
        except Exception as e:
            print(f"Error al intentar leer el archivo: {e}")
            traceback.print_exc()

    def guardar_inventario(self):
        """Guardar el inventario actual en el archivo de texto"""
        try:
            with open(self.nombrearchivo + ".txt", "w") as archivo:
                for producto in self.productos:
                    archivo.write(f"{producto.get_id()},{producto.get_nombre()}\n")  # Guardar ID y nombre
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print(f"Error: No se tienen permisos suficientes para escribir en el archivo {self.nombrearchivo}.txt.")
        except Exception as e:
            print(f"Error al intentar escribir en el archivo: {e}")
            traceback.print_exc()

    def agregar_producto(self, id, nombre):
        """Agregar un producto al inventario y actualizar el archivo"""
        try:
            if any(p.get_id() == id for p in self.productos):
                print(f"Error: Ya existe un producto con el ID {id}. No se puede agregar.")
                return
            nuevo_producto = Producto(id, nombre)
            self.productos.append(nuevo_producto)
            print(f"Producto {nombre} agregado al inventario.")
            self.guardar_inventario()  # Guardamos los cambios en el archivo
        except Exception as e:
            print(f"Error al agregar el producto: {e}")
            traceback.print_exc()

    def eliminar_producto(self, id):
        """Eliminar un producto del inventario por ID y actualizar el archivo"""
        try:
            producto_a_eliminar = None
            for producto in self.productos:
                if producto.get_id() == id:
                    producto_a_eliminar = producto
                    break
            if producto_a_eliminar:
                self.productos.remove(producto_a_eliminar)
                print(f"Producto con ID {id} eliminado.")
                self.guardar_inventario()  # Guardamos los cambios en el archivo
            else:
                print(f"No se encontró un producto con ID {id}.")
        except Exception as e:
            print(f"Error al eliminar el producto: {e}")
            traceback.print_exc()

    def buscar_producto(self, nombre):
        """Buscar productos por nombre (puede haber coincidencias parciales)"""
        try:
            productos_encontrados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
            if productos_encontrados:
                print("Productos encontrados:")
                for producto in productos_encontrados:
                    print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}")
            else:
                print("No se encontraron productos con ese nombre.")
        except Exception as e:
            print(f"Error al buscar el producto: {e}")
            traceback.print_exc()

    def mostrar_inventario(self):
        """Mostrar todos los productos en el inventario"""
        try:
            if self.productos:
                print("\nInventario de productos:")
                for producto in self.productos:
                    print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}")
            else:
                print("El inventario está vacío.")
        except Exception as e:
            print(f"Error al mostrar el inventario: {e}")
            traceback.print_exc()
