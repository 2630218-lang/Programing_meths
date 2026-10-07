#Listas de numeros
"""
Las listas tambien pueden almacenar numeros. python 
ofrece varias herramientas que ayudan a trabajar eficientemente
con listas de numeros
"""
#Metodo build-in range()
"""
El metodo range() nos ayuda a crear facilmente 
series de numeros.

Ejemplo 

"""

for value in range (1,5):
    print(value)

#Metodo range() solo imprime numeros enteros, si queremos imprimir numeros decimales
#podemos usar el metodo numpy.arange() que nos permite imprimir numeros decimales 

first_ten_numbers = range (0,10)
for value in first_ten_numbers:
    print(value)

for value in range (1,6):
    print (value)



numbers = list(range(0,10))
print(numbers)

#Lista de numeros pares
"""
el primer numero es el numero inicial, el segundo numero es el numero final y el tercer numero es el incremento
"""
even_numbers = list(range(0,11,2))

print(even_numbers)
#Ejercicio donde me gane 5 puntos 
tabladel5 = list(range(5,51,5))
print(tabladel5)

#lista de los 10 numeros cuadraticos 
squares = []
for value in range (1,11):
    squares.append(value**2)
print(squares)