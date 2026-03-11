heroes = [
    {"nombre": "Spider-Man", "universo": "Marvel", "poder": "Agilidad", "nivel": 85},
    {"nombre": "Iron Man", "universo": "Marvel", "poder": "Tecnologia", "nivel": 90},
    {"nombre": "Batman", "universo": "DC", "poder": "Inteligencia", "nivel": 88},
    {"nombre": "Superman", "universo": "DC", "poder": "Fuerza", "nivel": 98}
]

equipo = []

Salir = "si"
poder_total = 0
cuantos_dc = 0
cuantos_marvel = 0

while Salir != "no":
 for i ,c in enumerate(heroes,start=1):
        print(f"Heroe numero: {i}. Nombre = {c["nombre"]} | universo = {c["universo"]} | poder = {c["poder"]} | nivel = {c["nivel"]} ")

 heroe_seleccionado = int(input("\nQue heroe vas a seleccionar?: "))
 if heroe_seleccionado > len(heroes):
    print("Escoge uno de los que sale ahi\n")
 else:
    equipo.append(heroes[heroe_seleccionado-1])
    heroes.pop(heroe_seleccionado-1)
    Salir = input("\nQuieres seguir agregando heroes al equipo? si/no: ")


print(f""" 
---------------------------------------------------
              Heroes de tu equipo
---------------------------------------------------
""")

for i,c in enumerate(equipo,start=1):
 
 print(f"Heroe numero: {i}. Nombre = {c["nombre"]} | universo = {c["universo"]} | poder = {c["poder"]} | nivel = {c["nivel"]} ")

 poder_total += c["nivel"]
 
 if c["universo"] == "Marvel":
     cuantos_marvel += 1
 else:
     cuantos_dc +=1

print(f""" 
---------------------------------------------------
Poder total de tu equipo = {poder_total}
cuantos superheroes hay de Marvel? = {cuantos_marvel}
cuantos superheroes hay de DC? = {cuantos_dc}
""")
