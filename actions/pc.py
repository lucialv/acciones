def pc():
    frase_random = "hola"
    frase = input(f"Escribe esta frase lo más rápido que puedas: {frase_random}")
    tiempo = None
    if frase == frase_random:
        print(f"Has escrito la frase en {tiempo}")
    else:
        print("No creo que hayas escrito la frase correctamente!")