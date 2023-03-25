import os

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
        food = input("""
  _   _ ________      ________ _____            
 | \ | |  ____\ \    / /  ____|  __ \     /\    
 |  \| | |__   \ \  / /| |__  | |__) |   /  \   
 | . ` |  __|   \ \/ / |  __| |  _  /   / /\ \  
 | |\  | |____   \  /  | |____| | \ \  / ____ \ 
 |_| \_|______|   \/   |______|_|  \_\/_/    \_\ 
                                                
                                               \n\n Que comida quieres añadir?: """).lower()
        if food == "salir" or food == "s":
            os.system("cls")
            break
        comidas.append(food)
    save_foods(comidas)
    os.system("cls")
    


def comer():
    comidas = load_foods()
    comidas_str = [str(comida) for comida in comidas]
    comer = None
    if len(comidas) <= 0:
        print("No hay comida para comer, volviendo al menú principal 😓")
    else:
        while comer != "salir" or comer == "s":
            comer = input("""
   _____ ____  __  __ ______ _____  
  / ____/ __ \|  \/  |  ____|  __ \ 
 | |   | |  | | \  / | |__  | |__) |
 | |   | |  | | |\/| |  __| |  _  / 
 | |___| |__| | |  | | |____| | \ \ 
  \_____\____/|_|  |_|______|_|  \_\ \n\nComida: 🍱\n""" +
                          "\n".join(comidas_str) + "\nQuiero comer: ").lower()
            try:
                if len(comidas) > 0:
                    comidas.remove(comer)
                    comidas_str.remove(comer)
                    os.system("cls")
                    print(f"\nHas comido {comer} 🍴")
                    save_foods(comidas)
            except ValueError:
                if comer == "salir" or comer == "s":
                    os.system("cls")
                    break
                else:
                    print("\nNo existe esa comida en la nevera ❌")
                    continue
            finally:
                if len(comidas) <= 0:
                    print("\n" + "Se ha acabado la comida 🚩")
                    break
