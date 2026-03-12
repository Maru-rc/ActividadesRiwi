estudiantes = []
materias = []
notas = []
salir = "si"

numero_materias = int(input("Cuantas materias vas a ingresar? : "))

for i in range(numero_materias):
    nombre_materia = input(f"Ingresa el nombre de la materia numero {i+1}: ")
    materias.append(nombre_materia)

while salir != "no":
    #mostrar_estudiantes = input("Quieres ver los estudiantes que hay hasta el momento? si/no: ")
    
    #if mostrar_estudiantes == "si":
        
        #if len(estudiantes) == 0:
            #print("\nNo hay ningun estudiante ingresado")
        #else:
            #print(estudiantes)
            
    ingresar_estudiantes = input("\nIngresa el nombre del estudiante: ")
    
    for i in materias:
        nota_materia = int(input(f"\nIngresa la nota del estudiante {ingresar_estudiantes} en la materia {i}: "))
        notas.append(nota_materia)
    estudiantes.append(ingresar_estudiantes)
    salir = input("Deseas segui agregando estudiantes? si/no: ")

estudiantes_general = {"nombre_estudiantes":estudiantes,"materias":materias, "notas":notas}
print("""
-------------------------------------
        Estudiantes registrados
-------------------------------------
""")
suma = 0

for i in range(len(estudiantes_general["nombre_estudiantes"])):
    print(f"Estudiante : {estudiantes_general["nombre_estudiantes"][suma]}")
    suma += 1
