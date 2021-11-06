import os
import util
import time

def main():
    print("--Eliminar caracteres especiales en los archivos de un directorio--")
    directorio = input("Ingrese la ruta del directorio: ")
    directorio = directorio.replace('\\', '/')
    os.chdir(directorio)
    archivos = os.listdir(directorio)
    total_archivos = len(archivos)
    archivo_actual = 0
    for archivo in archivos:
        nombre, ext = os.path.splitext(archivo)
        nombre = util.quitar_tildes(nombre)
        nombre_nuevo = f"{nombre}{ext}"
        os.rename(archivo, nombre_nuevo)
        time.sleep(0.400)
        print(f"{archivo_actual} de {total_archivos} archivos renombrados con éxito", end="\r")  
        archivo_actual += 1

     
if __name__ == "__main__":
    main()