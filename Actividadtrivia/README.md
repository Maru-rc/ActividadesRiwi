# Historia de Usuario

## Juego de Trivias con Ranking

**Como** jugador  
**Quiero** ingresar mi nombre, responder preguntas de trivia y ver mi puntaje al final  
**Para** evaluar mis conocimientos y compararme con otros jugadores

---

## Criterios de Aceptación

### Inicio del juego

- El sistema debe solicitar el nombre del jugador antes de iniciar la partida.
- El nombre del jugador debe ser obligatorio para continuar.

---

### Preguntas

- El sistema debe cargar las preguntas desde un archivo JSON.
- El sistema debe seleccionar **5 preguntas aleatorias sin repetirse** en cada partida.
- Cada pregunta debe mostrar:
  - El enunciado
  - 4 opciones de respuesta: A, B, C y D
- El jugador debe poder seleccionar una única respuesta por pregunta.

---

### Puntaje

- Cada respuesta correcta debe otorgar **20 puntos**.
- Las respuestas incorrectas no suman puntos.
- Al finalizar las 5 preguntas, el sistema debe mostrar:
  - Puntaje total obtenido
  - Cantidad de respuestas correctas

---

### Persistencia de resultados

- Al finalizar la partida, el sistema debe registrar los resultados en un archivo CSV.
- Cada fila del CSV debe contener:
  - Nombre del jugador
  - Puntaje obtenido
  - Fecha y hora de la partida

---

### Ranking

- El sistema debe permitir consultar un ranking de jugadores.
- El ranking debe mostrar los **10 jugadores con mayor puntaje**.
- El ranking debe ordenarse de mayor a menor puntaje.

---

## Definition of Done

- El juego funciona correctamente (consola o interfaz).
- Las preguntas se cargan correctamente desde el JSON.
- No se repiten preguntas en una misma partida.
- El archivo CSV se crea automáticamente si no existe.
- Los resultados se guardan correctamente en el CSV.
- El ranking muestra correctamente el top 10 ordenado.
- El sistema ha sido probado con múltiples partidas.
