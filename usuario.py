from conexion_db import Conexion
from password import *

class Usuario():
    def __init__(self, usuario="", correo="", contrasena="", contrasena_2=""):
        self.__usuario = usuario
        self.__correo = correo
        self.__contrasena = contrasena
        self.__contrasena_2 = contrasena_2
    
    def comparacion_usuario(self,usuario):
        conexion = self.conexion_db()
        conexion.crear_tabla_usuarios()
        conexion.crear_tabla_libros(usuario)
        is_true = conexion.obtener_usuario(usuario)
        if is_true:
            return True

    def conexion_db(self):
        conexion = Conexion("usuarios.db")
        return conexion

    def registro_usuarios(self):
        registro = self.conexion_db()
        registro.crear_tabla_usuarios()
        contrasena_cifrada = encriptacion(self.__contrasena)
        registro.registrar_usuario(self.__usuario,self.__correo,contrasena_cifrada)
    
    def ingreso_usuario(self,usuario,contrasena):
        conexion = self.conexion_db()
        datos_usuario = conexion.obtener_usuario(usuario)
        if datos_usuario:
            id,usuario_db,correo_db,contrasena_db = datos_usuario
            validacion = comparacion_contrasena(contrasena,contrasena_db)
            return validacion
