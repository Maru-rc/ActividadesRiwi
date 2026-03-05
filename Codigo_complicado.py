estudiantes = ""
notas_total = ""
salir = 0
suma_promedio = 0
promedio_conteo = 0
promedio = 0
promedio_total = 0
numero_estudiantes = 0
cuantos_ganaron = 0
cuantos_perdieron = 0

cantidad_notas = int(input("cuantas notas va a ingresar?: "))

while salir == 0:
    estudiantes += input("Por favor ingresa el nombre del estudiante: ") + f"\n"
    numero_estudiantes += 1
    print(estudiantes)
    notas_total += f"\n"
    promedio = 0
    suma_promedio = 0

    for i in range(cantidad_notas):
        nota = input(f"Ingresa la nota {i + 1}: ")
        notas_total += nota + " "
        suma_promedio += float(nota)
        promedio = suma_promedio / cantidad_notas
        if promedio >= 3:
            print("Aprobo")
            cuantos_ganaron = + 1

        elif promedio < 3:
            print("Reprobaste")
            cuantos_perdieron = + 1

        print(notas_total)
        print(promedio)
    promedio_conteo += promedio
    promedio_total = promedio_conteo / numero_estudiantes
    print(promedio_conteo)
    print(promedio_total)
    print(cuantos_ganaron)
    print(cuantos_perdieron)

    opcion = input("Quieres seguir ingresando estudiantes? (si/no): ")

    if opcion == "no":
        print("ok")
        salir = 1

print(f""" 
------------------------------------------------------------
Estudiantes        notas
{estudiantes}      {notas_total}

""")