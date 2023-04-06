import random
import webbrowser
import time

def libro():
    asd = input("Quieres que te recomiende un libro aleatoriamente o quieres leer un libro que eligas tú? ").lower()
    aleatorio = ["aleatorio", "random", "al azar", "aleatoriamente", "dimelo tú", "dimelo tu"]
    yo = ["yo", "lo eligo yo", "escojo yo"]
    if asd in aleatorio:
        libros = [
            "Don quijote",
            "El petit princep",
            "La bella durmiente",
            "Blancanieves"
        ]
        libro = random.choice(libros)
        webbrowser.open(f"https://www.google.com/search?q={libro} libro")
    elif asd in yo:
        libroyo = input("Que libro quieres leer? ")
        webbrowser.open(f"https://www.google.com/search?q={libroyo} libro")

