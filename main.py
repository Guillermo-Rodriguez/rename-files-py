import os
import util
import time

def main():
    print("--Eliminar caracteres especiales en los archivos de un directorio--")
    directorio = input("Ingrese la ruta del directorio: ")
    directorio = directorio.replace('\\', '/')
    os.chdir(directorio)
    archivos = os.listdir(directorio)
    for archivo in archivos:
        nombre, ext = os.path.splitext(archivo)
        nombre = util.quitar_tildes(nombre)
        nombre_nuevo = f"{nombre}{ext}"
        os.rename(archivo, nombre_nuevo)
        time.sleep(0.500)
        print("#", end='')
    print("--Archivos renombrados con exito--")    

     
if __name__ == "__main__":
    main()