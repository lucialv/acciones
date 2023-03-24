def drogas():
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