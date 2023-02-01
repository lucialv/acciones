lunes = ["tecno", "mates", "catalan", "castellano", "sociales", "informatica"]


while len(lunes) > 0:
    pregunta = input("Haré el lunes... (0, 1, 2, 3, 4 y 5): ")
    if int(pregunta) <= 5:
        print(f"El lunes si harás {lunes[int(pregunta)]}")
        continue
    elif int(pregunta) >= 6:
        print(f"El lunes no harás {lunes[int(pregunta)]}")
        continue
