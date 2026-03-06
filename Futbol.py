partidos_jugados = int(input("Cuantos partidos se van a jugar?: "))
goles_favor = 0
goles_contra = 0
ganados = 0
empatados = 0
perdidos = 0
puntos = 0

for i in range(partidos_jugados):
    equipo_rival = input(f"\nIngresa el nombre del equipo rival: ")
    goles_junior = int(input("Cuantos goles metio el Junior?: "))
    goles_favor += goles_junior
    goles_rival = int(input(f"Cuantos goles metio el {equipo_rival}?: "))
    goles_contra += goles_rival

    if goles_junior > goles_rival:
        print("Partido ganado por el JuJu")
        ganados += 1
        puntos += 3

    elif goles_rival > goles_junior:
        print(f"Este lo gano el {equipo_rival}")
        perdidos += 1

    else:
        print("Partido empatado")
        empatados += 1
        puntos += 1
    
    diferencia_goles = goles_favor - goles_contra

print(f""" 
-------------------------------------------
          Como va el Junior?
-------------------------------------------
Cuantos partidos jugo el junior?: {partidos_jugados}
Cuantos gano?: {ganados}
Cuantos empato?: {empatados}
cuantos perdio?: {perdidos}
cuantos puntos tiene?: {puntos}
cuantos goles a favor tiene?: {goles_favor}
cuantos goles en contra tiene?: {goles_contra}
Cual es la diferencia de goles?: {diferencia_goles}
""")