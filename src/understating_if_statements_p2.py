print("Sistema de boletaje")

age = input("\nEscribte tu edad =")

print(age)

print(type(age))

age = int(age)

print(type(age))
"""   

if age >= 18:
    print("El costo de tu boleto es 400")
else:
    print("El costo de tu boleto es 200") 
"""

"""
if age > 18:
    cost = 500

if age >4 and age <18:
    cost =200   

if age <4:
    cost =0

print(f"El costo del boleto es:{cost}") 
"""

if age <= 4:
    cost = 0
elif age >4 and age <18:
    cost= 200
elif age>=18 and age <65:
    cost= 500
elif age >= 65:
    cost = 0   
else:
    cost= 2000
    
print("bloque if elif y esle")
print(f"El costo del boleto es:{cost}")    