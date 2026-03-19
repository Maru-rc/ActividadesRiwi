from datetime import datetime
import funciones
excluidos = []
puntaje = 0
respuestas_correctas = 0
correcta = False
hora = str(datetime.now())
nombre = input("Ingresa tu nombre: ")
for i in range(5):
    correcta = funciones.pregunta_aleatoria(excluidos,correcta)
    if correcta == True:
        puntaje += 20
        respuestas_correctas += 1
print(puntaje)
print(respuestas_correctas)
funciones.guardar_resultados(nombre,puntaje,hora)
