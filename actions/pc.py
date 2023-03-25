from timeit import default_timer as timer
import random
import time
import os

def generar_frase(num_palabras):
    sustantivos = ["gato", "perro", "elefante", "mesa", "computadora", "jirafa", "televisor", "coche", "libro", "pelota", "árbol", "teléfono", "casa", "planta", "pantalla", "piso", "ciudad", "bicicleta", "reloj", "puerta", "ventana", "pared", "avión", "café", "comida", "ropa", "playa", "parque", "lago", "río", "montaña", "bosque", "campo", "telescopio", "microscopio", "guitarra", "piano", "batería", "violín", "flauta", "trompeta", "tambor", "helicóptero", "barco", "tren", "autobús", "metro", "taxi"]

    verbos = ["corre", "salta", "come", "duerme", "trabaja", "estudia", "habla", "escribe", "lee", "piensa", "escucha", "observa", "baila", "canta", "nada", "vuela", "conduce", "camina", "sube", "baja", "entra", "sale", "viaja", "juega", "ayuda", "ama", "odia", "aprende", "enseña", "respira", "come", "bebe", "traga", "mastica", "besa", "abraza", "saluda", "despide", "tritura", "mezcla", "hornea", "cocina", "limpia", "organiza", "compra", "vende", "busca", "encuentra"]

    adjetivos = ["hermoso", "pequeño", "inteligente", "feliz", "valiente", "gigante", "sabroso", "frío", "caliente", "grande", "pequeño", "rápido", "lento", "alto", "bajo", "ancho", "estrecho", "grueso", "fino", "redondo", "cuadrado", "ovalado", "rectangular", "azul", "verde", "amarillo", "rojo", "morado", "naranja", "negro", "blanco", "gris", "rosa", "marrón", "dorado", "plateado", "brillante", "opaco", "suave", "áspero", "duro", "blando", "húmedo", "seco", "sucio", "limpio", "bonito", "feo", "simpático", "antipático", "divertido", "aburrido"]
    articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas", "lo", "al", "del"]
    determinantes = ["este", "esta", "estos", "estas", "ese", "esa", "esos", "esas", "aquel", "aquella", "aquellos", "aquellas", "mi", "mis", "tu", "tus", "su", "sus", "nuestro", "nuestra", "nuestros", "nuestras", "cualquier", "algun", "ningun"]
    preposiciones = ["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "sobre", "tras"]

    frase = ""
    for i in range(num_palabras):
        palabra = random.choice([random.choice(sustantivos), random.choice(verbos), random.choice(articulos), random.choice(preposiciones), random.choice(determinantes), random.choice(adjetivos)])
        frase += palabra + " "
    return frase.strip()

def meca():
    estado = True
    while estado:
        min_palabras = 5 # Establece el mínimo de palabras permitidas
        max_palabras = 50 # Establece el máximo de palabras permitidas
        os.system("cls")
        while True:
            try:
                num_palabras = int(input(f"""
  __  __ ______ _____          
 |  \/  |  ____/ ____|   /\    
 | \  / | |__ | |       /  \   
 | |\/| |  __|| |      / /\ \  
 | |  | | |___| |____ / ____ \ 
 |_|  |_|______\_____/_/    \_\ 
                               
                               \n\nCuantas palabras quieres escribir (entre {min_palabras} y {max_palabras})?: """))
                try:
                    if num_palabras < min_palabras or num_palabras > max_palabras:
                        raise ValueError
                    break
                except ValueError:
                    print(f"Por favor ingresa un número entre {min_palabras} y {max_palabras}")
            except ValueError:
                print("No puedes poner letras!")
        frase = generar_frase(num_palabras)
        frase = generar_frase(num_palabras)
        frase_random = frase
        os.system("cls")
        print(f"Escribe esta frase lo más rápido que puedas: \n--> {frase}\n Comienzas en 5 segundos...")
        time.sleep(1)
        os.system("cls")
        print(f"Escribe esta frase lo más rápido que puedas: \n--> {frase}\n Comienzas en 4 segundos...")
        time.sleep(1)
        os.system("cls")
        print(f"Escribe esta frase lo más rápido que puedas: \n--> {frase}\n Comienzas en 3 segundos...")
        time.sleep(1)
        os.system("cls")
        print(f"Escribe esta frase lo más rápido que puedas: \n--> {frase}\n Comienzas en 2 segundos...")
        time.sleep(1)
        os.system("cls")
        print(f"Escribe esta frase lo más rápido que puedas: \n--> {frase}\n Comienzas en 1 segundo...")
        time.sleep(1)
        os.system("cls")
        print(f"Escribe esta frase lo más rápido que puedas: \n--> {frase}\n ¡Empieza! \n\n")
        start = timer()
        frase_usuario = input("Escribe la frase: ")
        end = timer()
        tiempo = end - start
        palabras_usuario = frase_usuario.split()
        palabras_random = frase_random.split()
        palabras_incorrectas = []
        for i in range(len(palabras_random)):
            if i >= len(palabras_usuario) or palabras_usuario[i] != palabras_random[i]:
                palabras_incorrectas.append(palabras_random[i])
        if len(palabras_incorrectas) == 0:
            print(f"\nHas escrito la frase en {tiempo:.2f} segundos")
            while True:
                jugar_otra_vez = input("Quieres jugar otra vez? (si/no): ")
                if jugar_otra_vez == "si":
                    break
                elif jugar_otra_vez == "no":
                    estado = False
                    break
        else:
            print(f"\nNo escribiste las siguientes palabras correctamente: {', '.join(palabras_incorrectas)}.")
            print(f"\nTu tiempo total fue de {tiempo:.2f} segundos.")
            if tiempo is not None and tiempo >= 40 and tiempo < 50:
                print(f"\nPodrías mejorar tus dotes con el teclado")
            elif tiempo is not None and tiempo >= 50:
                print(f"\nTe recomiendo un curso de mecanografía")
            while True:
                jugar_otra_vez = input("Quieres jugar otra vez? (si/no): ")
                if jugar_otra_vez == "si":
                    break
                elif jugar_otra_vez == "no":
                    estado = False
                    break

