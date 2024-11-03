import bcrypt

def encriptacion(contrasena):
    contrasena_bytes = contrasena.encode("utf-8")
    salt = bcrypt.gensalt()
    contrasena_cifrada = bcrypt.hashpw(contrasena_bytes, salt)
    return contrasena_cifrada

def comparacion_contrasena(contrasena,contrasena_bd):
    contrasena = contrasena.encode("utf-8")
    if not bcrypt.checkpw(contrasena, contrasena_bd):
        return False
    else:
        return True