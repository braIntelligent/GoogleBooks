from usuario import Usuario
from libros import Administracion
from conexion_db import Conexion

def menu_registro():
    usuario = input("INGRESE NOMBRE DE USUARIO: ")
    correo = input("INGRESE EMAIL: ")
    contrasena = input("INGRESE CONTRASEÑA: ")
    contrasena_2 = input("INGRESE CONTRASEÑA NUEVAMENTE: ")
    conexion = Conexion("usuarios.db")
    conexion.crear_tablas(usuario)
    if len(usuario) >= 6 and "@" in correo and contrasena == contrasena_2:
        datos_usuario = Usuario(usuario,correo,contrasena,contrasena_2)
        usuario_db = datos_usuario.comparacion_usuario(usuario)
        if usuario_db is None:
            datos_usuario.registro_usuarios()
        else:
            print("------------------------------------")
            print("EL USUARIO YA ESTA REGISTRADO. ")
            print("------------------------------------")
    else:
        print("------------------------------------")
        print("INGRESA USUARIO MAYOR A 6 CARACTERES. ")
        print("INGRESA EMAIL VALIDO. ")
        print("INGRESA CONTRASEÑA VALIDA")
        print("------------------------------------")

def menu_ingreso():
    usuario = input("INGRESE NOMBRE DE USUARIO: ")
    contrasena = input("INGRESE CONTRASEÑA: ")
    conexion = Conexion("usuarios.db")
    conexion.crear_tablas(usuario)
    instancia = Usuario()
    usuario_db = instancia.ingreso_usuario(usuario,contrasena)
    if usuario_db:
        print("------------------------------------")
        print("AUTENTICACION EXITOSA")
        print("------------------------------------")
        menu_biblioteca(usuario.upper())
    else:
        print("------------------------------------")
        print("CREDENCIALES INVALIDAS. ")
        print("------------------------------------")

def menu_biblioteca(usuario_db):
    while True:
        try:
            print("------------------------------------")
            print(f"\tBIENVENIDO {usuario_db}")
            print("------------------------------------")
            opciones = ["BUSCAR LIBRO", "VER FAVORITOS", "CERRAR SESION"]
            for i, opcion in enumerate(opciones,1):
                print(f"({i}) =>> {opcion}")
            print("------------------------------------")
            option = int(input("INGRESA OPCION: "))
            print("------------------------------------")
            if option == 1:
                buscar_libro(usuario_db)
            elif option == 2:
                favoritos = Administracion()
                id = favoritos.ver_favoritos(usuario_db)
                if id:
                    favoritos.eliminar_favorito(usuario_db,id)
            elif option == 3:
                print("------------------------------------")
                print("CERRANDO SESION... ")
                print("------------------------------------")
                break
            else:
                print("------------------------------------")
                print("INGRESA OPCION VALIDA. ")
                print("------------------------------------")
        except ValueError as e:
            print("------------------------------------")
            print(f"ENTRADA NO VALIDA. ")
            print("------------------------------------")


def buscar_libro(usuario_db):
    nombre_libro = input("INGRESE NOMBRE LIBRO: ")
    administracion_libro = Administracion(nombre_libro)
    data = administracion_libro.obtener_data()
    lista_libros = administracion_libro.extaer_informacion_libro(data)
    resultado = administracion_libro.listar_libros(lista_libros)
    if resultado:
        indice_2, titulo, autor, paginas = resultado
        administracion_libro.agregar_favoritos(usuario_db,titulo,autor,paginas)