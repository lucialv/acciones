import random

def drogas():
<<<<<<< HEAD
    pregunta = input("¿Qué droga quieres cultivar?: ")
    drogas_naturales = ["Marihuana", "Crack", "Opio"]
    drogas_quimicas = ["Cocaina", "Metanfetamina", "Heroina", "Extasis", "PCP", "Barbituricos"]
    plantaciones_naturales = ["Atico", "Isla privada", "Invernadero"]
    plantaciones_quimicas = ["Laboratorio", "Subterraneo", "Bunker"]
    
    while pregunta not in drogas_naturales and pregunta not in drogas_quimicas:
        pregunta = input("Esa droga no está en la lista. Por favor, elige una droga de la lista: ")
    
    lugar = input(f"¿Dónde quieres plantar tu {pregunta}? ")
    
    while lugar not in plantaciones_naturales and lugar not in plantaciones_quimicas:
        lugar = input("Ese lugar no es válido. Por favor, elige un lugar de la lista: ")
        
    cantidad_plantada = random.randint(1, 100) # cantidad aleatoria de droga plantada
    cantidad_ganada = cantidad_plantada * random.randint(50, 200) # cantidad aleatoria de dinero ganado
    
    if lugar in plantaciones_naturales:
        print(f"Has plantado {cantidad_plantada} gramos de {pregunta} en {lugar} y has ganado ${cantidad_ganada}.")
    elif lugar in plantaciones_quimicas:
        print(f"Has plantado {cantidad_plantada} gramos de {pregunta} en {lugar} y has ganado ${cantidad_ganada}.")
    else:
        print(f"No puedes plantar {pregunta} en {lugar}")

while True:
    drogas()
    respuesta = input("¿Quieres seguir plantando drogas? (si o no): ")
    if respuesta.lower() == "no":
        break
=======
    pregunta = input(f"¿Que substancia ilegal quieres cultivar?: ").capitalize()
    drogas_naturales = ["Marihuana","Crack","Opio"]
    drogas_quimicas = ["Cocaina","Metanfetamina","Heroina","Extasis","PCP","Barbituricos"]
    
    plantaciones_quimicas = ["Laboratorio","Subterraneo","Atico","Bunker","Isla privada","Invernadero"] #separar la lista en 2, una para naturales y otra para quimicas
    
    plantaciones_naturales = ["adsa"] #Completa la lista

    if pregunta in drogas_naturales or pregunta in drogas_quimicas: # si pregunta (la droga) está en drogas naturales o quimicas se ejecutará este codigo
        lugar = input(f"¿Donde quieres plantar tu {pregunta}?")


    elif lugar in plantaciones_naturales and pregunta in drogas_naturales: #si lugar es en plantaciones naturales y ademas pregunta es una droga natural pasará esto
        print(f"Has plantado {pregunta} en {lugar}.")
    elif lugar in plantaciones_naturales and pregunta in drogas_quimicas: #si lugar es en plantiaciones naturales y ademas pregunta es una droga quimica pasará esto
        print(f"No puedes plantar {pregunta} en {lugar}.")



    elif lugar in plantaciones_quimicas:
        print(f"Has plantado {pregunta} en {lugar}.")
    
drogas()
>>>>>>> 3a06bbbc222db0b2a125463d6fb2a7e402fca1c7
