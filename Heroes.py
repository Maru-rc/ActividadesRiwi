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

    print(f""" 
---------------------------------------------------
              Heroes Disponibles
---------------------------------------------------
1. Nombre = {heroes[0]["nombre"]} | universo = {heroes[0]["universo"]} | poder = {heroes[0]["poder"]} | nivel = {heroes[0]["nivel"]}
2. Nombre = {heroes[1]["nombre"]} | universo = {heroes[1]["universo"]} | poder = {heroes[1]["poder"]} | nivel = {heroes[1]["nivel"]}
3. Nombre = {heroes[2]["nombre"]} | universo = {heroes[2]["universo"]} | poder = {heroes[2]["poder"]} | nivel = {heroes[2]["nivel"]}
4. Nombre = {heroes[3]["nombre"]} | universo = {heroes[3]["universo"]} | poder = {heroes[3]["poder"]} | nivel = {heroes[3]["nivel"]}
""")
    
    heroe_seleccionado = input("Que heroe vas a seleccionar?: ")

    if heroe_seleccionado == "1":
        equipo.append(heroes[0])

    elif heroe_seleccionado == "2":
        equipo.append(heroes[1])

    elif heroe_seleccionado == "3":
        equipo.append(heroes[2])

    elif heroe_seleccionado == "4":
        equipo.append(heroes[3])
    
    Salir = input("Quieres seguir agregando heroes al equipo? si/no: ")

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