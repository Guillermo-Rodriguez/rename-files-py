'''
Funcion para limpiar los caracteres tildes en un string
dado comomparametro 
'''
def quitar_tildes(nombre):
    reemplazar = (
        ("á" , "a")
        ("é" , "e")
        ("í" , "i")
        ("ó" , "o")
        ("ú" , "u")
    )

    for a, b in reemplazar:
        nombre = nombre.replace(a, b).replace(a.upper(), b.upper())
    return nombre  