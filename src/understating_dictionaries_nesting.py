#Nesting 
#CADA ELEMENTO EN LA LISTA ES UN DICCIONARIO
#Listas de diccionarios 

coveant_elite = {"name":"elite","color":"blue","points":10,"shield":"true"}
coveant_jackal = {"name":"jackal","color":"gray","points":6,"shield":"true"}
coveant_grunt = {"name":"grunt","color":"orange","points":3,"shield":"false"}

coveants = []
coveants.append(coveant_elite)
coveants.append(coveant_jackal)
coveants.append(coveant_grunt)

print(coveants)

#flotilla de enemigos

coveants_fleet = []

for _ in range (2):
    coveants_fleet.append(coveant_elite)

for _ in range (5):
    coveants_fleet.append(coveant_jackal)

for _ in range (10):
    coveants_fleet.append(coveant_grunt)

    print("\n flotilla")
print(coveants_fleet)

#Lista en un diccionario 
#Menu 

print("\n Nesting:Listas en los diccionarios")

tacos = {
    "tortillas":["maiz","harina"],
    "Guisos":["bisteck","tripa","pastor"]
}

print(f"tu has ordenado unos tacos de {tacos['Guisos'][0]}")

print(f"tu has ordenado unos tacos de {tacos['tortillas'][1]}")