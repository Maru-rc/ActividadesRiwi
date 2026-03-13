materias = []
general = []
salir = "si"

numero_materias = int(input("Cuantas materias vas a ingresar? : "))

for i in range(numero_materias):
    nombre_materia = input(f"Ingresa el nombre de la materia numero {i+1}: ")
    materias.append(nombre_materia)

while salir != "no":
    mostrar_estudiantes = input("Quieres ver los estudiantes que hay hasta el momento? si/no: ")
    
    if mostrar_estudiantes == "si":
        
        if len(general) == 0:
            print("\nNo hay ningun estudiante ingresado")
        else:
            for i,c in enumerate(general,start=1):
                print(f"\nEstudiante numero {i} Nombre = {c["nombre"]} | Materias = {c["materias"]} | notas = {c["notas"]} | promedio = {c["promedio"]:.2f}")
            
    ingresar_estudiantes = input("\nIngresa el nombre del estudiante: ")
    notas = []
    suma = 0
    promedio = 0

    for i in materias:
        nota_materia = float(input(f"\nIngresa la nota del estudiante {ingresar_estudiantes} en la materia {i}: "))
        suma += nota_materia
        notas.append(nota_materia)

    promedio = suma / len(materias)
    general.append({"nombre":ingresar_estudiantes,"materias":materias,"notas": notas,"promedio":promedio})
    salir = input("\nDeseas seguir agregando estudiantes? si/no: ")

mejor_promedio_inicial = general[0]["promedio"]
posicion_mejor_promedio = 0

for i,c in enumerate(general):
    if c["promedio"] > mejor_promedio_inicial:
        mejor_promedio = c["promedio"]
        posicion_mejor_promedio = i
    else:
        mejor_promedio = mejor_promedio_inicial

print("""
-------------------------------------
        Estudiantes registrados
-------------------------------------
""")

for i,c in enumerate(general,start=1):
    print(f"Estudiante numero {i} Nombre = {c["nombre"]} | Materias = {c["materias"]} | notas = {c["notas"]} | promedio = {c["promedio"]:.2f}")
    
print(f"El mejor promedio lo tuvo el estudiante {general[posicion_mejor_promedio]["nombre"]} con un promedio de {mejor_promedio:.2f}")