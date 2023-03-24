def pc():
    frase_random = "hola"
    frase = input(f"Escribe esta frase lo más rápido que puedas: {frase_random}")
    tiempo = None
    if frase == frase_random:
        print(f"Has escrito la frase en {tiempo}")
    elif tiempo == 10: #si han pasado de 10s sale ese mensaje
        print(f"Podrias mejorar tus dotes con el teclado")
    elif tiempo == 20:#si han pasado de 20s sale ese mensaje
        print(f"Te recomiendo un curso de mecanografía")
    else:
        print("No creo que hayas escrito la frase correctamente!")