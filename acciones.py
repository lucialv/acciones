import os
import time
os.system("cls")


def save_foods(foods):
    with open("nevera.txt", "w") as file:
        for food in foods:
            file.write(food + "\n")


def load_foods():
    if os.path.exists("nevera.txt"):
        with open("nevera.txt", "r") as file:
            return [food.strip() for food in file.readlines()]
    return []


def nevera():
    comidas = load_foods()
    while True:
        food = input("Que comida quieres añadir?: ")
        if food == "salir":
            break
        comidas.append(food)
    save_foods(comidas)


def comer():
    comidas = load_foods()
    comidas_str = [str(comida) for comida in comidas]
    comer = None
    if len(comidas) <= 0:
        print("No hay comida para comer, volviendo al menú principal 😓")
    else:
        while comer != "salir":
            comer = input("\nComida: 🍱\n" +
                          "\n".join(comidas_str) + "\nQuiero comer: ")
            try:
                if len(comidas) > 0:
                    comidas.remove(comer)
                    comidas_str.remove(comer)
                    os.system("cls")
                    print(f"\nHas comido {comer} 🍴")
                    save_foods(comidas)
            except ValueError:
                if comer == "salir":
                    break
                else:
                    print("\nNo existe esa comida en la nevera ❌")
                    continue
            finally:
                if len(comidas) <= 0:
                    print("\n" + "Se ha acabado la comida 🚩")
                    break


def dormir():
    print(f"1 ovejita...")
    time.sleep(1)
    os.system("cls")
    for i in range(2, 11):
        print(f"{i} ovejitas...")
        time.sleep(1)
        os.system("cls")


def vestir():
    ropa = None
    ropa_valida = ["pantalones", "pantalón", "pantalon", "sudadera", "camiseta", "camiseta de manga corta", "camisa", "zapatos", "calzoncillos", "calcetines", "bambas", "collar", "falda", "vestido", "top", "sandalias", "chanclas", "blusa", "mono", "collares", "anillos",
                   "anillo", "mascarilla", "pendiente", "pendientes", "bolso", "bolsos", "mochila", "mochilas", "pantalón corto", "pantalon corto", "shorts", "short", "bragas", "bufanda", "gorra", "bandana", "capa", "chaqueta", "chaquetas", "medias", "uniforme", "gafas", "gafas de sol"]
    while ropa != "salir":
        ropa = input("Que te quieres poner hoy?: ").lower()
        if any(response in ropa for response in ropa_valida):
            print(f"Te has puesto: {ropa.capitalize()}")
        elif ropa == "salir":
            os.system("cls")
            break
        else:
            print("Creo que no existe esa ropa...")


while True:
    accion = input("Que quieres hacer?: ")
    if accion == "salir":
        break
    elif accion == "comer":
        os.system("cls")
        comer()
    elif accion == "nevera":
        os.system("cls")
        nevera()
    elif accion == "dormir":
        os.system("cls")
        dormir()
    elif accion == "vestir":
        os.system("cls")
        vestir()
    else:
        os.system("cls")
        print(f"No existe la función {accion}")
