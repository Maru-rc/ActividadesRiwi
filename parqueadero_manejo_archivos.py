def guardar_usuarios(nombre,vehiculo,placa):
    with open("Usuarios.txt", "a") as usuarios:
        usuarios.writelines(["Nombre: ",nombre," |","Tipo de vehiculo: ",vehiculo," |","Numero de placa: ",placa," |","\n"])

def leer_usuarios():
    with open("Usuarios.txt", "r") as usuarios:
        for usuario in usuarios:
            print(usuario.strip())

salir_bucle = "no"
variable_placas = ""
while salir_bucle != "si":
 print(""" 
-----------------------------------------------------------
                    Sistema parqueadero
-----------------------------------------------------------
1. Ingresa vehiculo parqueadero
2. Ver vehiculos en el parqueadero
3. sacar vehiculo del parqueadero
4. Salir del programa
 """)

 opciones = input("Por favor escoge una opcion: ")

 match(opciones):
     
     case"1":
         nombre = input("Ingresa tu nombre: ")
         vehiculo = input("Ingresa tipo de vehiculo: ")
         placa = input("Ingresa la placa: ")
         try:
            with open("Usuarios.txt","r") as placas:
             contenido = placas.read()
             if placa in contenido:
                 print("\nESta placa ya esta en el sistema")
             else:
                guardar_usuarios(nombre,vehiculo,placa)
         except:
            guardar_usuarios(nombre,vehiculo,placa)

     case"2":
         try: 
            print("\nUsuarios en el parqueadero: ")
            leer_usuarios()
         except:
             print("No hay ningun vehiculo")
     case"3":
       with open("Usuarios.txt","r") as placas:
        placasguardadas = placas.read()
        nombre = input("Ingresa tu nombre: ")
        vehiculo = input("Ingresa el tipo de vehiculo: ")
        placa = input("Ingresa la placa de tu vehiculo: ")
        variable_placas = placasguardadas
        if nombre and vehiculo and placa in variable_placas:
          variable_placas = variable_placas.replace(nombre,"",1).replace(vehiculo,"",1).replace(placa,"")
          print("Vuelve pronto!")
          with open("Usuarios.txt","w") as usuarios:
             usuarios.write(variable_placas)

     case"4":
         print("Adios")
         salir_bucle = "si"