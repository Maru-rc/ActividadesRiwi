sillas_cine = [[1,2,3,4,5,6,7,8,9,10],
               [1,2,3,4,5,6,7,8,9,10],
               [1,2,3,4,5,6,7,8,9,10],
               [1,2,3,4,5,6,7,8,9,10],
               [1,2,3,4,5,6,7,8,9,10],
               [1,2,3,4,5,6,7,8,9,10],
               [1,2,3,4,5,6,7,8,9,10],
               [1,2,3,4,5,6,7,8,9,10],]
salir_while = "si"

print("Bienvenido a Royal Films!")
while salir_while !="no":
    print("\nSillas disponibles:")
    for i in sillas_cine:
        print(i[:])

    fila = int(input("Escoge la fila: "))
    if fila > len(sillas_cine):
        print("Por favor escoge una fila valida")
        fila = int(input("Escoge la fila: "))

    columna = int(input("Escoge la columna: "))
    if columna > len(sillas_cine[0]):
        print("Por favor escoge una columna valida")
        columna = int(input("Escoge la columna: "))
    try:    
        if sillas_cine[fila-1][columna-1] == "x":
            print("Asiento no disponible")
        else:
            sillas_cine[fila-1][columna-1] = "x"
    except:
        print("Error, por favor vuelve a intentar")
        continue
    
    salir_while = input("Deseas comprar otra silla? si/no: ")
