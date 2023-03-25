import random

def drogas():
    # Carga el saldo actual desde el archivo de texto
    with open('dinero.txt', 'r') as f:
        saldo = int(f.read().strip())

    droguitas = True
    while droguitas:
        drogas_naturales = ["Marihuana", "Crack", "Opio", "Maria"]
        drogas_quimicas = ["Cocaina", "Coca", "Metanfeta", "Meta", "Metanfetamina", "Heroina", "Extasis", "PCP", "Barbituricos"]
        plantaciones_naturales = ["Atico", "Isla privada", "Invernadero"]
        plantaciones_quimicas = ["Laboratorio", "Subterraneo", "Bunker"]

        pregunta = input("¿Qué droga quieres cultivar?: ").capitalize()

        while pregunta not in drogas_naturales and pregunta not in drogas_quimicas:
            pregunta = input("Esa droga no está en la lista. Por favor, elige una droga de la lista: ").capitalize()

        cantidad_plantada = random.randint(1, 100)
        cantidad_ganada = cantidad_plantada * random.randint(50, 200)
        plantando = True
        while plantando:
            lugar = input(f"¿Dónde quieres plantar tu {pregunta}? ").capitalize()

            while lugar not in plantaciones_naturales and lugar not in plantaciones_quimicas:
                lugar = input("Ese lugar no es válido. Por favor, elige un lugar de la lista: ").capitalize()
            if lugar in plantaciones_naturales and pregunta in drogas_naturales:
                print(f"Has plantado {cantidad_plantada} gramos de {pregunta} en {lugar} y has ganado ${cantidad_ganada}.")
                # Agrega la cantidad ganada al saldo y actualiza el archivo de texto
                saldo += cantidad_ganada
                with open('dinero.txt', 'w') as f:
                    f.write(str(saldo))
                while True:
                    respuesta = input("¿Quieres seguir plantando drogas? (si o no): ").lower()
                    if respuesta == "no":
                        plantando = False
                        droguitas = False
                        break
                    elif respuesta == "si":
                        plantando = False
                        break
            elif lugar in plantaciones_quimicas and pregunta in drogas_quimicas:
                print(f"Has plantado {cantidad_plantada} gramos de {pregunta} en {lugar} y has ganado ${cantidad_ganada}.")
                # Agrega la cantidad ganada al saldo y actualiza el archivo de texto
                saldo += cantidad_ganada
                with open('dinero.txt', 'w') as f:
                    f.write(str(saldo))
                while True:
                    respuesta = input("¿Quieres seguir plantando drogas? (si o no): ").lower()
                    if respuesta == "no":
                        plantando = False
                        droguitas = False
                        break
                    elif respuesta == "si":
                        plantando = False
                        break
            elif lugar in plantaciones_naturales and pregunta in drogas_quimicas:
                print(f"No puedes plantar droga quimica en una plantación natural!")
                continue
            elif lugar in plantaciones_quimicas and pregunta in drogas_naturales:
                print(f"No puedes plantar droga natural en una plantación quimica!")
                continue

