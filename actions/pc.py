from timeit import default_timer as timer
import random 

def generar_frase(num_palabras):
    sustantivos = ["gato", "perro", "elefante", "mesa", "computadora", "jirafa", "televisor", "coche", "libro", "pelota", "árbol", "teléfono", "casa", "planta", "pantalla", "piso", "ciudad", "bicicleta", "reloj", "puerta", "ventana", "pared", "avión", "café", "comida", "ropa", "playa", "parque", "lago", "río", "montaña", "bosque", "campo", "telescopio", "microscopio", "guitarra", "piano", "batería", "violín", "flauta", "trompeta", "tambor", "helicóptero", "barco", "tren", "autobús", "metro", "taxi"]

    verbos = ["corre", "salta", "come", "duerme", "trabaja", "estudia", "habla", "escribe", "lee", "piensa", "escucha", "observa", "baila", "canta", "nada", "vuela", "conduce", "camina", "sube", "baja", "entra", "sale", "viaja", "juega", "ayuda", "ama", "odia", "aprende", "enseña", "respira", "come", "bebe", "traga", "mastica", "besa", "abraza", "saluda", "despide", "tritura", "mezcla", "hornea", "cocina", "limpia", "organiza", "compra", "vende", "busca", "encuentra"]

    adjetivos = ["hermoso", "pequeño", "inteligente", "feliz", "valiente", "gigante", "sabroso", "frío", "caliente", "grande", "pequeño", "rápido", "lento", "alto", "bajo", "ancho", "estrecho", "grueso", "fino", "redondo", "cuadrado", "ovalado", "rectangular", "azul", "verde", "amarillo", "rojo", "morado", "naranja", "negro", "blanco", "gris", "rosa", "marrón", "dorado", "plateado", "brillante", "opaco", "suave", "áspero", "duro", "blando", "húmedo", "seco", "sucio", "limpio", "bonito", "feo", "simpático", "antipático", "divertido", "aburrido"]
    adverbios = ["abruptamente", "absolutamente", "aceleradamente", "activamente", "admirablemente","adversamente", "afectuosamente", "afortunadamente", "agradablemente", "alegremente","alfabéticamente", "algo", "allegadamente", "amablemente", "ambiguamente","amistosamente", "ampliamente", "analíticamente", "ancestralmente", "andando","anteriormente", "antiguamente", "apaciblemente", "aparentemente", "apasionadamente","apresuradamente", "apropiadamente", "aproximadamente", "arduamente", "artificialmente","aseadamente", "asertivamente", "asiduamente", "asombrosamente", "aspiracionalmente","astutamente", "asustadizamente", "atómicamente", "aun", "auténticamente", "automáticamente","auxiliarmente", "aventuradamente", "aversivamente", "avidamente", "aviesamente","avisadamente", "ay", "básicamente", "bien", "bimensualmente", "bipolarmente","brillantemente", "bruscamente", "brutalmente", "cada", "calmadamente", "candorosamente","caóticamente", "carezosamente", "carnalmente", "casi", "castamente", "cautamente","cediendo", "celestialmente", "censuradamente", "centralmente", "cerca", "cerradamente","certificadamente", "ciegamente", "circularmente", "civícamente", "claramente","coercitivamente", "cognitivamente", "coherente", "coincidentemente", "colateralmente","colectivamente", "coloradamente", "coléricamente", "cómicamente", "comercialmente","compasivamente", "competentemente", "completamente", "comprensivamente", "con","concienzudamente", "concretamente", "concretamente", "concurrentemente", "condensadamente","condicionalmente", "confiadamente", "conflictivamente", "confortablemente", "conscientemente","constante", "consternadamente", "constructivamente", "contemplativamente", "continuamente","contra", "contrastadamente", "contundentemente", "convencionalmente", "convulsivamente","cordialmente", "corporalmente", "correctamente", "cortésmente", "cotidianamente","crecientemente", "críticamente", "cruelmente", "cuidadosamente", "culturalmente","cumplidamente", "curiosamente", "cursi", "curtidamente", "cómodamente", "cónicamente","cuestionablemente", "da", "danzando", "decididamente", "declamatoriamente", "decorosamente","defectuosamente", "defensivamente", "deferentemente", "definitivamente"]
    articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas", "lo", "al", "del"]
    determinantes = ["este", "esta", "estos", "estas", "ese", "esa", "esos", "esas", "aquel", "aquella", "aquellos", "aquellas", "mi", "mis", "tu", "tus", "su", "sus", "nuestro", "nuestra", "nuestros", "nuestras", "cualquier", "algun", "ningun"]
    preposiciones = ["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "sobre", "tras"]

    frase = ""
    for i in range(num_palabras):
        palabra = random.choice([random.choice(sustantivos), random.choice(verbos), random.choice(adverbios), random.choice(articulos), random.choice(preposiciones), random.choice(determinantes), random.choice(adjetivos)])
        frase += palabra + " "
    return frase.strip()

def pc():
    min_palabras = 5 # Establece el mínimo de palabras permitidas
    max_palabras = 50 # Establece el máximo de palabras permitidas
    num_palabras = int(input(f"Cuantas palabras quieres escribir (entre {min_palabras} y {max_palabras})?: "))
    while num_palabras < min_palabras or num_palabras > max_palabras:
        num_palabras = int(input(f"Por favor ingresa un número entre {min_palabras} y {max_palabras}: "))
    frase = generar_frase(num_palabras)
    frase_random = frase
    input(f"Escribe esta frase lo más rápido que puedas: \n--> {frase}\n\nPresiona Enter para empezar...\n\n")
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
        print(f"Has escrito la frase en {tiempo:.2f} segundos")
    else:
        print(f"No escribiste las siguientes palabras correctamente: {', '.join(palabras_incorrectas)}.")
        print(f"Tu tiempo total fue de {tiempo:.2f} segundos.")
        if tiempo is not None and tiempo >= 40 and tiempo < 50:
            print(f"Podrías mejorar tus dotes con el teclado")
        elif tiempo is not None and tiempo >= 50:
            print(f"Te recomiendo un curso de mecanografía")

pc()
