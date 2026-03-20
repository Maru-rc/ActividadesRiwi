import random
import json

def guardar_resultados(nombre,puntaje,hora):
    with open ("Resultados.csv", "a") as archivo_resultados:
        archivo_resultados.writelines([nombre + ",",str(puntaje), ",",hora,"\n"])


def pregunta_aleatoria(excluidos):
    with open ("data.json","r") as datos:
        preguntas = json.load(datos)
        numero_aleatorio = random.randint(1,len(preguntas))
        if numero_aleatorio in excluidos:
            while numero_aleatorio in excluidos:
                numero_aleatorio = random.randint(1,len(preguntas))
        excluidos.append(numero_aleatorio)

        
        pregunta = preguntas[numero_aleatorio - 1]
        print("Pregunta:")
        print(pregunta["pregunta"])
        print("\nOpciones:")
        for i, c in pregunta["opciones"].items():
            print(f"{i}: {c}")

        respuesta_seleccionada = input("Selecciona una respuesta: ")
        if respuesta_seleccionada != pregunta["respuesta_correcta"]:
            print("Respuesta incorrecta\n")
        else:
            print("Respuesta correcta\n")
            correcta = True
            return correcta
        
def consultar_ranking ():
    try:
        with open("Resultados.csv", "r"):
            resultados = json.load
            print(resultados)
    except:
        print("Aun no hay jugadores en el ranking")

