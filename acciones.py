import os
import time
os.system("cls")
from actions.sexo import *
from actions.comer import *
from actions.dormir import *
from actions.vestir import *
from actions.viajes import *
from actions.examen import *
from actions.pc import *
from actions.matar import *
from actions.sumar import *
from actions.help import *
from actions.adivina_el_numero import *
while True:
    accion = input("""        
           _____ _____ _____ ____  _   _ ______  _____ 
     /\   / ____/ ____|_   _/ __ \| \ | |  ____|/ ____|
    /  \ | |   | |      | || |  | |  \| | |__  | (___  
   / /\ \| |   | |      | || |  | | . ` |  __|  \___ \ 
  / ____ \ |___| |____ _| || |__| | |\  | |____ ____) |
 /_/    \_\_____\_____|_____\____/|_| \_|______|_____/ 
                                                       
                                                       \n(`help` para ver todos las acciones)\n\n-> Que quieres hacer?\n\nAccion: """).lower()
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
    elif accion == "help" or accion == "ayuda":
        os.system("cls")
        ayuda()
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
    elif accion == "meca":
        os.system("cls")
        meca()
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
