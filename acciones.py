import os
import time
os.system("cls")
from sexo import *
from comer import *
from dormir import *
from vestir import *
from viajes import *
from examen import *
from matar import *
from sumar import *
from adivina_el_numero import *
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
    elif accion == "examen":
        os.system("cls")
        examen()
    elif accion == "desvestir":
        os.system("cls")
        desvestir()
    elif accion == "sexo":
        os.system("cls")
        sexo()
    elif accion == "viajar":
        os.system("cls")
        viajar()
    elif accion == "matar":
        os.system("cls")
        matar()
    elif accion == "calculadora":
        os.system("cls")
        calculadora()
    elif accion == "donde estoy?" or accion == "donde estoy" or accion == "ubicación" or accion == "ubicacion":
        os.system("cls")
        viajo()
    elif accion == "jugar":
        jugar = input("A que quieres jugar?")
        if jugar == "adivina el numero":
            adivina_el_numero()
        else:
            print(f"No existe el juego {jugar}")
    else:
        os.system("cls")
        print(f"No existe la función {accion}")
