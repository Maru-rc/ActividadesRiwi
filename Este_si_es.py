cantidad_estudiantes = int(input("Ingresa la cantidad de estudiantes: "))
salir = 0
notas = 0
while salir != cantidad_estudiantes:
    estudiante = input("Ingresa el nombre del estudiante: ")
    for i in range(3):
        nota = int(input(f"Ingresa la {i+ 1} nota: "))
        convertir =  float(nota)
        notas += convertir
        promedio = notas / 3 
        print(promedio)