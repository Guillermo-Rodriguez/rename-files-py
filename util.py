'''
Función para limpiar tildes en una cadena
dado como parámetro 
'''
def quitar_tildes(nombre):
    reemplazar = (
        ("á" , "a"),
        ("é" , "e"),
        ("í" , "i"),
        ("ó" , "o"),
        ("ú" , "u")
    )

    for a, b in reemplazar:
        nombre = nombre.replace(a, b).replace(a.upper(), b.upper())
    return nombre  