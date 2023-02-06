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
        food = input("Que comida quieres añadir?: ").lower()
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
            comer = input("\nComida: 🍱\n" +
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


def dormir():
    print(f"1 ovejita...")
    time.sleep(1)
    os.system("cls")
    for i in range(2, 11):
        print(f"{i} ovejitas...")
        time.sleep(1)
        os.system("cls")


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
        "pantalones": ["falda", "vestido", "shorts", "pantalón corto", "pantalon corto"],
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
            ropa = input("Que te quieres poner hoy?: ").lower()
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
            
            print("\nActualmente tienes puesto: \n" + "\n".join(ropitas))
            prenda = input("\n¿Qué prenda te quieres quitar?: ").lower()
            if prenda in ropitas:
                os.system("cls")
                ropitas.remove(prenda)
                print(f"Te has quitado: {prenda.capitalize()}")
                save_clothes(ropitas)
            else:
                os.system("cls")
                print(f"Creo que no tienes puesto {prenda}...")
        else:
            time.sleep(1)
            os.system("cls")
            print("No tienes ropa puesta en este momento.")
            break

def sexo():
    for i in range(1,11):
        print("Ah")
        time.sleep(1)
    os.system("cls")

pais = None
def viajar():
    viaje = None
    while True:
        viaje = input("¿A dónde quieres viajar?: ").capitalize()
        
        paises = ["Afganistán","Albania","Argelia","Andorra","Angola","Antigua y Barbuda","Argentina","Armenia","Australia","Austria","Azerbaiyán","Bahamas","Bahréin","Bangladesh","Barbados","Bielorrusia","Bélgica","Belice","Benín","Bhután","Bolivia","Bosnia y Herzegovina","Botsuana","Brasil","Brunei","Bulgaria","Burkina Faso","Burundi","Bután","Cabo Verde","Camboya","Camerún","Canadá","Catar","Chad","Chile","China","Chipre","Ciudad del Vaticano","Colombia","Comoras","Congo","Corea del Norte","Corea del Sur","Costa de Marfil","Costa Rica","Croacia","Cuba","Dinamarca","Dominica","Ecuador","Egipto","El Salvador","Emiratos Árabes Unidos","Eritrea","Eslovaquia","Eslovenia","España","Estados Unidos","Estonia","Etiopía","Filipinas","Finlandia","Fiyi","Francia","Gabón","Gambia","Georgia","Ghana","Granada","Grecia","Guatemala","Guinea","Guinea-Bisáu","Guinea Ecuatorial","Guyana","Haití","Honduras","Hungría","India","Indonesia","Irak","Irán","Irlanda","Islandia","Islas Marshall","Islas Salomón","Israel","Italia","Jamaica","Japón","Jordania","Kazajistán","Kenia","Kirguistán","Kiribati","Kuwait","Laos","Lesoto","Letonia","Líbano","Liberia","Libia","Liechtenstein","Lituania","Luxemburgo","Macedonia del Norte","Madagascar","Malasia","Malaui","Maldivas","Malí","Malta","Marruecos","Mauricio","Mauritania","México","Micronesia","Moldavia","Mónaco","Mongolia","Montenegro","Mozambique","Myanmar (Birmania)","Namibia","Nauru","Nepal","Nicaragua","Níger","Nigeria","Noruega","Nueva Zelanda","Omán","Países Bajos","Pakistán","Palaos","Panamá","Papúa Nueva Guinea","Paraguay","Perú","Polonia","Portugal","Reino Unido","República Centroafricana","República Checa","República de Macedonia","República del Congo","República Democrática del Congo","República Dominicana","República Sudafricana","Ruanda","Rumanía","Rusia","Samoa","San Cristóbal y Nieves","San Marino","San Vicente y las Granadinas","Santa Lucía","Santo Tomé y Príncipe","Senegal","Serbia","Seychelles","Sierra Leona","Singapur","Siria","Somalia","Sri Lanka","Suazilandia","Sudán","Sudán del Sur","Suecia","Suiza","Surinam","Tailandia","Tanzania","Tayikistán","Timor Oriental","Togo","Tonga","Trinidad y Tobago","Túnez","Turkmenistán","Turquía","Tuvalu","Ucrania","Uganda","Uruguay","Uzbekistán","Vanuatu","Venezuela","Vietnam","Yemen","Yibuti","Zambia","Zimbabue"]
        if viaje in paises:
            os.system("cls")
            print(f"Has viajado a: {viaje}")
            global pais
            pais = viaje
            break
        if viaje == "S" or viaje == "Salir":
            os.system("cls")
            break
        else:
            os.system("cls")
            print(f"No creo el país {viaje} exista...")
            continue
def viajo():
    os.system("cls")
    print(f"Ahora mismo estás en {pais}")

while True:
    
    accion = input("Que quieres hacer?: ").lower()
    if accion == "salir" or accion == "s":
        os.system("cls")
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
    elif accion == "desvestir":
        os.system("cls")
        desvestir()
    elif accion == "sexo":
        os.system("cls")
        sexo()
    elif accion == "viajar":
        os.system("cls")
        viajar()
    elif accion == "donde estoy?" or accion == "donde estoy" or accion == "ubicación" or accion == "ubicacion":
        os.system("cls")
        viajo()
    else:
        os.system("cls")
        print(f"No existe la función {accion}")
