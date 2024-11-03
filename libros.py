from api import *
from conexion_db import Conexion

class Administracion():
    def __init__(self, libro=""):
        self.__libro = libro

    def obtener_libro(self):
        return self.__libro

    def obtener_data(self):
        consumo = Api_books(self.obtener_libro())
        data = consumo.api()
        return data
    
    def extaer_informacion_libro(self,data):
        libros = data.get("items")
        if not libros:
            print("------------------------------------")
            print("NO SE ENCONTRARON LIBROS.")
            print("------------------------------------")
            return []
        lista_libros = []
        for libro in libros:
            volume = libro.get("volumeInfo", {})
            titulo = volume.get("title", "NO HAY AUTOR DISPONIBLE. ")
            autor = volume.get("authors", "NO HAY AUTOR DISPONIBLE.")
            paginas = volume.get("pageCount", "NO HAY PAGINAS DISPONIBLES. ")
            descripcion = volume.get("description", "NO HAY DESCRIPCION DISPONIBLE. ")
            autor = ", ".join(autor) if isinstance(autor, list) else autor
            lista_libros.append({"TITULO":titulo,"AUTOR":autor,"PAGINAS":paginas,"DESCRIPCION":descripcion})
        return lista_libros

    def listar_libros(self,lista_libros):
        if lista_libros:
            print("------------------------------------")
            print(f"\t LIBROS DE {self.__libro.upper()}")
            print("------------------------------------")
            for i, libro in enumerate(lista_libros,1):
                print(f"({i}) =>> TITULO: {libro['TITULO']}, AUTOR: {libro['AUTOR']}, PAGINAS: {libro['PAGINAS']}\n")
            try:
                print("------------------------------------")
                indice = int(input("INGRESE EL ID DEL LIBRO PARA VER DESCRIPCION O [0] PARA VOLVER ATRAS: "))
                print("------------------------------------")
                if indice == 0:
                    return
                elif indice >=1 and indice <= len(lista_libros):
                    return self.mostrar_descripcion(indice, lista_libros)
                else:
                    print("------------------------------------")
                    print("INGRESA OPCION VALIDA. ")
                    print("------------------------------------")
            except ValueError:
                print("------------------------------------")
                print(f"ENTRADA NO VALIDA. ")
                print("------------------------------------")
        else:
            return

    def mostrar_descripcion(self,indice,lista_libros):
            titulo = lista_libros[indice - 1]['TITULO']
            descripcion = lista_libros[indice - 1]['DESCRIPCION']
            autor = lista_libros[indice - 1]['AUTOR']
            paginas = lista_libros[indice - 1]['PAGINAS']
            print("-------------------------------------------------")
            print(f"\tTITULO: {titulo}".upper())
            print("-------------------------------------------------")
            print(descripcion.upper())
            print("-------------------------------------------------")
            try:
                print("-------------------------------------------------")
                indice_2 = int(input("INGRESE [1] PARA AGREGAR A FAVORITOS O PRESIONE [0] PARA VOLVER ATRAS: "))
                print("-------------------------------------------------")
                if indice_2 == 0:
                    return False
                elif indice_2 >= 1 and indice_2 <= len(lista_libros):
                    return indice_2, titulo, autor, paginas
                else:
                    print("------------------------------------")
                    print("INGRESA OPCION VALIDA. ")
                    print("------------------------------------")
            except ValueError:
                print("------------------------------------")
                print(f"ENTRADA NO VALIDA. ")
                print("------------------------------------")

    def agregar_favoritos(self,usuario,titulo,autor,paginas):
        conexion = self.conectar_db()
        conexion.crear_tabla_libros(usuario)
        conexion.guardar_libro(usuario,titulo,autor,paginas)
        print("------------------------------------")
        print("LIBRO GUARDADO CON EXITO. ")
        print("------------------------------------")
    
    def ver_favoritos(self,usuario_db):
        conexion = self.conectar_db()
        libros = conexion.obtener_libros(usuario_db)
        if not libros:
            print("------------------------------------")
            print("NO TIENES LIBROS GUARDADOS. ")
            print("------------------------------------")
            return False
        elif libros:
            for i, libro in enumerate(libros,1):
                print(f"({i}) =>> TITULO: {libro[1]}, AUTOR: {libro[2]}, PAGINAS: {libro[3]}".upper())
            print("-------------------------------------------------")
            posicion = int(input("INGRESE EL ID DEL LIBRO PARA VER ELIMINAR O [0] PARA VOLVER ATRAS: "))
            print("-------------------------------------------------")
            if posicion == 0:
                print("------------------------------------")
                print("VOLVIENDO ATRAS... ")
                print("------------------------------------")
                return
            elif posicion >= 1 and posicion <= len(libros):
                id = libros[posicion - 1][0]
                return id
            else:
                print("INGRESA OPCION VALIDA. ")
    
    def eliminar_favorito(self, usuario,posicion):
        conexion = self.conectar_db()
        conexion.eliminar_libro(usuario,posicion)
    
    def conectar_db(self):
        conexion = Conexion('usuarios.db')
        return conexion