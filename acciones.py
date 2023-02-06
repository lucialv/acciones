import os
import time
os.system("cls")
from sexo import *
from comer import *
from dormir import *
from vestir import *
from viajes import *
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
