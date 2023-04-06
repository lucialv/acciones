import time
import os

def save_clothes(ropas):
    with open("ropa.txt", "w") as file:
        for ropa in ropas:
            file.write(ropa + "\n")


def load_clothes():
    if os.path.exists("ropa.txt"):
        with open("ropa.txt", "r") as file:
            return [ropa.strip() for ropa in file.readlines()]
    return []


def vestir():
    ropitas = load_clothes()
    ropa = None
    ropa_valida = ["pantalones", "pantalón", "pantalon", "sudadera", "camiseta", "camiseta manga corta", "camiseta de manga corta", "camisa", "zapatos", "calzoncillos", "calcetines", "bambas", "collar", "falda", "vestido", "top", "sandalias", "chanclas", "tacones", "blusa", "mono", "collares", "anillos",
                   "anillo", "gorro", "sombrero", "mascarilla", "pendiente", "pendientes", "bolso", "botas", "bolsos", "mochila", "mochilas", "pantalón corto", "pantalon corto", "shorts", "short", "bragas", "bufanda", "gorra", "bandana", "capa", "chaqueta", "chaquetas", "medias", "uniforme", "gafas", "gafas de sol"]
    piezas_ropa_no_permitidas = {
        "pantalones": ["falda", "vestido", "shorts", "pantalón corto", "pantalon corto"], #esto hace que si tienes puesto "pantalones", no te puedas poner lo que hay en esta lista
        "pantalón": ["falda", "vestido", "shorts", "pantalón corto", "pantalon corto"],
        "pantalon": ["falda", "vestido", "shorts", "pantalón corto", "pantalon corto"],
        "falda": ["pantalones", "vestido", "pantalón", "pantalon", "shorts", "pantalón corto", "pantalon corto"],
        "vestido": ["pantalones", "falda", "pantalón", "pantalon", "shorts", "pantalón corto", "pantalon corto"],
        "shorts": ["pantalones", "pantalón", "pantalon", "falda", "vestido", "pantalón corto", "pantalon corto"],
        "pantalón corto": ["pantalones", "pantalón", "pantalon", "falda", "vestido", "shorts"],
        "pantalon corto": ["pantalones", "pantalón", "pantalon", "falda", "vestido", "shorts"],
        "sudadera": ["chaqueta", "capa"],
        "camiseta": ["capa", "blusa", "camiseta manga corta", "top"],
        "camiseta de manga corta": ["chaqueta", "capa", "blusa", "camiseta manga corta", "top"],
        "camisa": ["vestido", "camiseta de manga corta", "camiseta manga corta", "camiseta", "top"],
        "top": ["camiseta manga corta", "camiseta de manga corta", "camiseta", "vestido"],
        "zapatos": ["bambas", "sandalias", "chanclas", "tacones", "botas"],
        "bambas": ["zapatos", "sandalias", "chanclas", "tacones", "botas"],
        "sombrero": ["gorro", "gorra"],
        "gorro": ["sombrero", "gorra"],
        "gorra": ["sombrero", "gorro"],
        "chanclas": ["zapatos", "bambas", "sandalias", "tacones", "botas"],
        "tacones": ["chanclas", "bambas", "sandalias", "zapatos", "botas"],
        "sandalias": ["chanclas", "bambas", "tacones", "zapatos", "botas"],
        "bragas": ["calzoncillos"],
        "calzoncillos": ["bragas"],
        "gafas": ["gafas de sol"],
        "gafas de sol": ["gafas"],
        "pendientes": ["pendiente"],
        "botas": ["chanclas", "bambas", "tacones", "zapatos", "sandalias"]

    }
    while ropa != "salir":

        if len(ropitas) <= 0:
            os.system("cls")
            ropa = input("""
 __      ________  _____ _______ _____ _____  
 \ \    / /  ____|/ ____|__   __|_   _|  __ \ 
  \ \  / /| |__  | (___    | |    | | | |__) |
   \ \/ / |  __|  \___ \   | |    | | |  _  / 
    \  /  | |____ ____) |  | |   _| |_| | \ \ 
     \/   |______|_____/   |_|  |_____|_|  \_\ 
                                              
                                              \n\nQue te quieres poner hoy?: """).lower()
        else:
            print("\nActualmente tienes puesto: \n" + "\n".join(load_clothes()))
            ropa = input("\nQuieres ponerte algo más?: ").lower()

        for prenda_actual, prendas_no_permitidas in piezas_ropa_no_permitidas.items():
            if prenda_actual in ropitas and ropa in prendas_no_permitidas:
                os.system("cls")
                print("No te puedes poner esa ropa si ya tienes puesto: " + prenda_actual)
                break
        else:
            if any(response in ropa for response in ropa_valida):
                if ropa not in ropitas:
                    os.system("cls")
                    print(f"Te has puesto: {ropa.capitalize()}")
                    ropitas.append(ropa)
                    save_clothes(ropitas)
                else:
                    os.system("cls")
                    print(f"Ya te has puesto: {ropa.capitalize()}")

        if ropa == "no" or ropa == "salir" or ropa == "s":
            os.system("cls")
            break
        elif not any(response in ropa for response in ropa_valida):
            os.system("cls")
            print("Creo que no existe esa ropa...")




def desvestir():
    ropitas = load_clothes()
    prenda = None
    while prenda != "salir" or prenda != "s":
        if len(ropitas) > 0:
            
            print("""
  _____  ______  _______      ________  _____ _______ _____ _____  
 |  __ \|  ____|/ ____\ \    / /  ____|/ ____|__   __|_   _|  __ \ 
 | |  | | |__  | (___  \ \  / /| |__  | (___    | |    | | | |__) |
 | |  | |  __|  \___ \  \ \/ / |  __|  \___ \   | |    | | |  _  / 
 | |__| | |____ ____) |  \  /  | |____ ____) |  | |   _| |_| | \ \ 
 |_____/|______|_____/    \/   |______|_____/   |_|  |_____|_|  \_\ 
                                                                   
                                                                   
                                                                \n\nActualmente tienes puesto: \n""" + "\n".join(ropitas))
            prenda = input("\n¿Qué prenda te quieres quitar?: ").lower()
            if prenda in ropitas:
                os.system("cls")
                ropitas.remove(prenda)
                print(f"Te has quitado: {prenda.capitalize()}")
                save_clothes(ropitas)
            elif prenda == "salir":
                os.system("cls")
                break
            else:
                os.system("cls")
                print(f"Creo que no tienes puesto {prenda}...")
        else:
            time.sleep(1)
            os.system("cls")
            print("No tienes ropa puesta en este momento.")
            break