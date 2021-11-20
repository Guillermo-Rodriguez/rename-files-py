import os
import util
import time
import unicodedata

def main():
    print("--Eliminar caracteres especiales en los archivos de un directorio--")
    directorio = input("Ingrese la ruta del directorio: ")
    directorio = directorio.replace('\\', '/')
    os.chdir(directorio)
    archivos = os.listdir(directorio)
    total_archivos = len(archivos)
    archivo_actual = 1
    for archivo in archivos:
        nombre_nuevo = gen_nombre_nuevo(archivo)
        os.rename(archivo, nombre_nuevo)
        time.sleep(0.100)
        fin_de_linea = "\n" if archivo_actual == total_archivos else "\r" 
        print(f"{archivo_actual} de {total_archivos} archivos renombrados con éxito", end=fin_de_linea)  
        archivo_actual += 1

def gen_nombre_nuevo(archivo):
    nombre, ext = os.path.splitext(archivo)
    nombre = unicodedata.normalize(u'NFKD', nombre).encode('ascii', 'ignore').decode('utf8')
    nombre = util.quitar_tildes(nombre)
    nombre_nuevo = f"{nombre}{ext}"
    return nombre_nuevo 

     
if __name__ == "__main__":
    main()

