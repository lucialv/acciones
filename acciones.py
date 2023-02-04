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


while True:
    pregunta = input("Que quieres hacer?: ")
    if pregunta == "salir":
        break
    elif pregunta == "comer":
        os.system("cls")
        comer()
    elif pregunta == "nevera":
        os.system("cls")
        nevera()
    elif pregunta == "dormir":
        os.system("cls")
        dormir()
    else:
        print("No existe esa función")
