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
        ("ú" , "u"),
        ("Á" , "A"),
        ("É" , "E"),
        ("Í" , "I"),
        ("Ó" , "O"),
        ("Ú" , "U"),
        ("ñ" , "n"),
        ("Ñ" , "N"),
        ("_" , "-"),
        (" " , "-")
    )

    for a, b in reemplazar:
        nombre = nombre.replace(a, b)
    return nombre  