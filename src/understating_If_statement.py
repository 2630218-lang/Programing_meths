#if statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car)

#el condicional es el corazon del if
#Para determinar igualdad ==
print("condicionales verdadero y falso")

truck = "ford"
#condicional false
print (truck == "cheyene")
#condicional true
print (truck == "ford")

# == se le llama conectores

#Condicional if para determinar desigualdad 
# != se usa para determinar desigualdad
# para que el resultado sea verdadero, la condicion no dene ser igual a la variable

print(truck!= "tacoma") #True 

print(truck!= "ford") #False

#comparaciones numericas
print("\nComparaciones numericas")
age = 34 
print(age == 34) #true 
print(age == 30) #false 
#python no distingue numeros y strings por lo que el resultado es false 
print(age == "34") #false

answer = 17
if answer != 42:
    print("Esa no es la respuesta correcta")

age = 19
# 19 es menor que 21 menor o igual que 21 y menor que 18
#Simnolo menor que 
print (age < 21) #true
print (age <= 21) #true 
print (age < 18) #false
#mayor que 
#19 es mayor o igual que 12,19 es mayor que 12
print(age >=12) #true
print(age >12) #True
print(age > 20) #false
