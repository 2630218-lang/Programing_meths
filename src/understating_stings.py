"""
Un string es de manera sencilla una serie de caracteres .
En python, todo lo que se encuentre entre comillas simples' '
o dentro de comillas dobles "" es considerado un string.

Ejemplo: 
    "Esto es un string "
    'Esto tambien es un string'
    'Le dije a un amigo, "Pyhton es mi lenguaje favorito" '
    "El lenguaje 'python' lleva el nombre por monty no por la serpiente "

Ejemplo incorrecto:
(X) "Luis'
(X) 'Luis"

"""
"""
Name es variable tipo sting por el contenido que esta encerrado en dos comillas 

Las variables tipo sting tienen atributos y metodos

Metodos: Manipula el sting 

Atributos: 
"""

name = "LuIs JaSsO"

print (name)
print (name.title())

name2 = "LuuuuuuuuuuuIIIIIIIIIIIIIISSSSSSSSSSSS JAAAAAAAAAAAAAAASSSSSSSSSSSSSSOOOOOOO"

print (name2.title())

print (name)

name = name.title()

print (name)


"""
Un metodo es una accion que python puede realizar sobre una variable 

El punto despues de la variable seguido por el nombre del metodo 
en este caso title() dice que se tiene que ejecutar el metodo title()
de la variable name.

Todos los metodos son seguidos de parentesis,porque en ocasiones necesitan
informacion adicional para funcionar. En esta ocacion el metodo titie() 
no requiere info adicional para ejecutarse.

"""
print (name.upper())
print (name.lower())
