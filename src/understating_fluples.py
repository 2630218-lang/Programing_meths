"""
Tuplas 
Las tuplas son listas de elementos que no pueden ser modificadas, es decir son inmutables.

Se definen con parentesis () y los elementos se separan por comas.


Ejemplo:
Si tenemos un rectangulo (largo,ancho) que siempre va a tener 
cierto tamaño, podemos asegurar que sus dimensiones no van a cambiar
si colocamos sus valores en una tupla.

"""

dimension = (200,50) #200 de largo y 50 de ancho
print("tupla original:",dimension)

# Vamos a imprimir elementos de una tupla 
# Se realiza de la misma manera que con las listas

print(dimension[0]) #imprime el primer elemento de la tupla
print(dimension[1]) #imprime el segundo elemento de la tupla

#Metodos que se pueden utilizar con las tuplas
print(dir(dimension)) #imprime los metodos que se pueden utilizar con la tupla

#Lista 
dimension_2 = [200,50] 
print("metodos y atributos de una lista",dir(dimension_2)) #imprime los metodos que se pueden utilizar con la lista

print("Siguiente metodo")

#String
name = "Luis" 
print(dir(name)) #imprime los metodos que se pueden utilizar con el string
print("Siguiente metodo")


#
age = 18
print(dir(age)) #imprime los metodos que se pueden utilizar con el int

names = ["carlos","charly","juan","wendy"]
print(names)

names[0] = "mercury" 
names[1] = "mercury"
names[2] = "mercury"
names[3] = "mercury"

print(names)

#dimension[0] = 500 #esta operacion no esta permitida 

#for dimension in dimension:
    #print(dimension)

#tupla con slices
tupla = (1,2,3,4,5,6,7,8,9,10)
print(tupla[2:5]) #imprime los elementos desde el indice 2 hasta el 4

dimension = (500,1000,20)
print ("tupla redefinida:",dimension)

answer = (True)
print (answer)