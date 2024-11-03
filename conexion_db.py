import sqlite3

class Conexion():
    try:
        def __init__(self, nombre):
            self.__conexion = sqlite3.connect(nombre)
            self.__cursor = self.__conexion.cursor()
    except sqlite3.Error as e:
        print(f"ERROR AL CONECTAR CON LA BASE DE DATOS: {e} ")

    def crear_tabla_usuarios(self):
        self.__cursor.execute(
            ''' CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                correo TEXT NOT NULL,
                contrasena TEXT NOT NULL);
            ''')
        self.guardar_conexion()
        
    def registrar_usuario(self,usuario,correo,contrasena):
        self.__conexion.execute(
            ''' INSERT INTO usuarios (usuario,correo,contrasena)
                VALUES (?,?,?)
            ''', (usuario,correo,contrasena))
        self.guardar_conexion()
        print("------------------------------------")
        print("USUARIO REGISTRADO EXITOSAMENTE. ")
        print("------------------------------------")
        self.cerrar_conexion()

    def obtener_usuario(self,usuario):
        self.__cursor.execute(
            ''' SELECT * FROM usuarios
                WHERE usuario = ?;
            ''',(usuario,))
        usuario_obtenido = self.__cursor.fetchone()
        if usuario_obtenido:
            return usuario_obtenido
        elif not usuario_obtenido:
            return False
        self.cerrar_conexion()

    def crear_tabla_libros(self,usuario):
        self.__cursor.execute(
            f'''CREATE TABLE IF NOT EXISTS libros_{usuario}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                paginas INTEGER);
            ''')
        self.guardar_conexion()

    def guardar_libro(self,usuario,titulo,autor,paginas):
        self.__cursor.execute(
        f'''INSERT INTO libros_{usuario} (titulo,autor,paginas)
            VALUES (?,?,?)
        ''', (titulo,autor,paginas))
        self.guardar_conexion()
        self.cerrar_conexion()

    def obtener_libros(self,usuario):
        self.__cursor.execute(
            f'''SELECT * FROM libros_{usuario};
            ''')
        libros = self.__cursor.fetchall()
        if not libros:
            return False
        elif libros:
            return libros
        self.cerrar_conexion()

    def eliminar_libro(self,usuario,id):
        self.__cursor.execute(
            f'''DELETE FROM libros_{usuario}
                WHERE id = ?;
            ''',(id,))
        self.guardar_conexion()
        print("------------------------------------")
        print("LIBRO ELIMINADO CON EXITO")
        print("------------------------------------")
        self.guardar_conexion()
        self.cerrar_conexion()
    
    def crear_tablas(self,usuario):
        self.crear_tabla_usuarios()
        self.crear_tabla_libros(usuario)

    def obtener_conexion(self):
        return self.__conexion
    
    def obtener_cursor(self):
        return self.__cursor

    def cerrar_conexion(self):
        self.__conexion.close()

    def guardar_conexion(self):
        self.__conexion.commit()