vuelos = {
        'riwi232' : ["Pereira",10, 150000],
        'riwi897' : ["Manizales",5, 300000],
        'riwi145' : ["Nuqi", 3, 100000],
        'riwi666' : ["Medellin", 0 , 20000]
}
reservas = []

salir_bucle = "si"
dinero_recaudado = 0
while salir_bucle == "si":

    print(f"Vuelos disponibles: \n{vuelos}")
    nombre_pasajero = input("\nIngresa tu nombre: ")
    codigo_vuelo = input("Ingresa el codigo del vuelo: ")

    if vuelos.get(codigo_vuelo):

        if vuelos[codigo_vuelo][1]>0:

            print(f"solo hay: {vuelos[codigo_vuelo][1]} asientos disponibles")
            cantidad_asientos = int(input("Ingresa la cantidad de asientos que vas a comprar: "))

            if cantidad_asientos > vuelos[codigo_vuelo][1]:
                print("No se completo la compra, cantidad de asientos mayor a la disponible")

            print("Vuelos comprados\n")
            reservas.append((nombre_pasajero,codigo_vuelo,cantidad_asientos))
            vuelos[codigo_vuelo][1] -= cantidad_asientos

        else:
            print("No hay sillas\n")    

    else:
        print("No se encontro el vuelo\n")

    print(reservas)
    salir_bucle = input("Desea realizar otra compra? si/no: ")
    
precio_vuelo_232 = vuelos["riwi232"][2]
precio_vuelo_897 = vuelos["riwi897"][2]
precio_vuelo_145 = vuelos["riwi145"][2]
precio_vuelo_666 = vuelos["riwi666"][2]
