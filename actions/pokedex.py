import os
def save_foods(foods):
    with open("pokedex.txt", "w") as file:
        for food in foods:
            file.write(food + "\n")


def load_pokedex():
    if os.path.exists("pokedex.txt"):
        with open("pokedex.txt", "r") as file:
            return [food.strip() for food in file.readlines()]
    return []


def pokedex():
    while True:
        pregunta = input("Quieres añadir un pokemon a la pokedex o quieres quitar un pokemon de la pokedex?: ")
        if pregunta == "quitar" or pregunta == "remove":
            pokedex_remove()
        elif pregunta == "añadir" or pregunta == "add":
            pokedex_add()
        elif pregunta == "salir" or pregunta == "s":
            break
        else:
            print("No he entendido tu respuesta.")


def pokedex_add():
    pokemon = load_pokedex()
    asdads = True
    while asdads:
        food = input("""\n\n Que pokemon quieres añadir a la pokedex?: """).lower()
        if food == "salir" or food == "s":
            os.system("cls")
            break
        pokemon.append(food)
        jads = input(f"Has añadido a la pokedex a {food.capitalize} quieres añadir otro más? ")
        while True:
            if jads == "si":
                break
            elif jads == "no":
                asdads = False
                break
            else:
                jads = input("No he entendido tu respuesta, quieres añadir a otro más?")
    save_foods(pokemon)
    os.system("cls")

def pokedex_remove():
    pokemon = load_pokedex()
    pokemon_str = [str(comida) for comida in pokemon]
    comer = None
    if len(pokemon) <= 0:
        print("No hay pokemons para quitar de la pokedex 😓")
    else:
        while comer != "salir" or comer == "s":
            comer = input("""\n\nPokedex: \n""" +
                          "\n".join(pokemon_str) + "\nQue pokemon deseas quitar de la pokedex? ").lower()
            try:
                if len(pokemon) > 0:
                    pokemon.remove(comer)
                    pokemon_str.remove(comer)
                    os.system("cls")
                    print(f"\nHas quitado a {comer.capitalize()} de la pokedex.")
                    save_foods(pokemon)
            except ValueError:
                if comer == "salir" or comer == "s":
                    os.system("cls")
                    break
                else:
                    print("\nNo existe ese pokemon en la pokedex ❌")
                    continue
            finally:
                if len(pokemon) <= 0:
                    print("\n" + "Se han acabado los pokemon de la pokedex.")
                    break   
