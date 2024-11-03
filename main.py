from interfaz import *
from libros import *

def incio():
    while True:
         try:
            opciones = ["REGISTRARSE", "INGRESAR", "SALIR"]
            print("------------------------------------")
            print("\tBIBLIOTECA")
            print("------------------------------------")
            for i, opcion in enumerate(opciones,1):
                print(f"({i}) =>> {opcion}")
            print("------------------------------------")
            opcion = int(input("INGRESA OPCION: "))
            print("------------------------------------")
            if opcion == 1:
                menu_registro()
            elif opcion == 2:
                menu_ingreso()
            elif opcion == 3:
                print("------------------------------------")
                print("SALIENDO...")
                print("------------------------------------")
                break
            else:
                print("------------------------------------")
                print("INGRESA OPCION VALIDA. ")
                print("------------------------------------")
         except Exception:
             print("------------------------------------")
             print(f"ENTRADA NO VALIDA. ")
             print("------------------------------------")
        

if __name__ == '__main__':
    incio()
