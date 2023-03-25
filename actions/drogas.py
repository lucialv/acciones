import random

def drogas():
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
