guisos = ["salsa verde","deshebrada","nopales"]

if "salsa verde " in guisos:
    print("si hay salsa verde")
elif "deshebrada" in guisos:
    print("Si hay deshebrada")
elif "guiso especial" in guisos:
    print("Hay guisos especiales")


#lista vacia 
guisos_2 = ["salsa verde","deshebrada","nopales"]

if guisos_2:
    for guiso in guisos_2:
        print(guiso)
    else:
        print("no hay guisos")


#guisos disponibles 

guisos_disponibles = ["salsa verde","deshebrada","picadillo","asado"]
guisos_a_ordenar = ["barbacoa","desnebrada","cabrito"]

for guiso in guisos_a_ordenar:
    if guiso in guisos_disponibles:
        print(f"si tenemos del guiso,{guiso}".title())
    else:
        print(f"no tenemos guiso,{guiso}".title())
        print("¿NO VIO EL MENU O QUE?")