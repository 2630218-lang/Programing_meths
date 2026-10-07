players = ["Peter","Mercado","Aaron","Fatima","renata"]
print("lista original",players)

#slicing
print(players [3:5]) #imprime la lista solo con los ultimos dos elementos 
#si quiero imprimir el primer elemento de la lista debo poner 0:1
# si quiero imprimir el segundo elemento de la lista debo poner 1:2
print(players [1:2]) #imprime solo el segundo elemento de la lista


#El slicing nos permite trabajar con un grupo 
#especifico de una lista al resultado se le conoce como 
#"un slice"

print("1:4",players[1:4]) # ['Mercado', 'Aaron', 'Fatima']
print(":3",players[:3]) # ['Peter', 'Mercado', 'Aaron']
print("2:",players[2:]) # ['Aaron', 'Fatima', 'renata']
print("[-3:]",players[-3:]) # ['Aaron', 'Fatima', 'renata']

#Casos especiales
print("casos especiales")
#Al imprimir un slice que va mas alla del tamaño de la lista no se genera un error 
#se imprime la lista hasta el final de la misma
players = ["Peter","Mercado","Aaron","Fatima","renata"]
print(players[0:10]) # = ['Peter', 'Mercado', 'Aaron', 'Fatima', 'renata']
print(players[1:10]) # = ['Mercado', 'Aaron', 'Fatima', 'renata']
#inicio mayor que el final 
print(players[10:1]) # = [] Lista  vacia 
###
print(players[:0]) # = [] Lista vacia

