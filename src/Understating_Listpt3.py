print("El dia de hoy voy a trabajar con listas".upper())

magicans = ['harry','ron','hermione','snape','voldemort']

print(magicans)

print("imprimir a la mala")

print(magicans[0],magicans[1],magicans[2],magicans[3],magicans[4])

#ciclo for
#for tiene salto de linea 
print("imprimir con un for")
for magican in magicans:
    #se agrega el end para que se imprima en una sola lineal 
    #y se le agrega end y comillias mas espacio para que no 
    #este junto 
    print(magican, end= " ")

"""
a esto se le conoce como un looping 

magicans = ['harry','ron','hermione','snape','voldemort']
ahora cada mago imprimira un mensaje
"""


for magican in magicans:
    print(f"{magican.title()} ese fue un gran echizo " )


for magican in magicans:
    print(f"No puedo esperar a ver el siguiente echizo ,{magican.upper()}\n" )

