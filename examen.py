def examen():
    pregunta_1 = input("¿Quien es el creador de este código? ").lower()
    pregunta_2 = input("¿Cuando nací? ")
    pregunta_3 = input("¿En que año estamos ahora mismo? ")
    
    puntuacion = 0
    respuestas_1 = ["adri", "adrian"]
    respuestas_2 = ["2007"]
    respuestas_3 = ["2023"]

    if pregunta_1 in respuestas_1:
        puntuacion = puntuacion + 1

    respuesta_correcta_2 = False

    for respuesta_valida in respuestas_2:
        if respuesta_valida in pregunta_2:
            respuesta_correcta_2 = True
            break

    if respuesta_correcta_2:
        puntuacion = puntuacion + 1

    respuesta_correcta_3 = False

    for respuesta_valida in respuestas_3:
        if respuesta_valida in pregunta_3:
            respuesta_correcta_3 = True
            break

    if respuesta_correcta_3:
        puntuacion = puntuacion + 1
    
    print(f"\n Tu puntuación es de {puntuacion} puntos")
    

