"""
Una lista comprehension combina el for lopp
y la creacion de nuevos elementos en una sola linea y automaticamente
agrega cada nuevo a la lista es decir sin utilizar el metodo append.
"""
squares = [value**2 for value in range(1, 11)] 
print(squares)

names = ["Renata","sebas","luis","peter","leo"]

names_upv =[name+"upv" for name in names]
print(names_upv)