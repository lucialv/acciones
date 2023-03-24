def drogas():
    pregunta = input(f"¿Que substancia ilegal quieres cultivar?: ")
    drogas_naturales = ["Marihuana","Crack","Opio"]
    drogas_quimicas = ["Cocaina","Metanfetamina","Heroina","Extasis","PCP","Barbituricos"]
    plantaciones = ["Laboratorio","Subterraneo","Atico","Bunker","Isla privada","Invernadero"]
    if pregunta in drogas_naturales or pregunta in drogas_quimicas:
        print(f"¿Donde quieres plantar tu {plantaciones}?")
    elif pregunta in plantaciones:
        print(f"")
    