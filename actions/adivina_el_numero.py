import random
import os

def adivina_el_numero():
    print("""     
       _ _    _  _____          _____  
      | | |  | |/ ____|   /\   |  __ \ 
      | | |  | | |  __   /  \  | |__) |
  _   | | |  | | | |_ | / /\ \ |  _  / 
 | |__| | |__| | |__| |/ ____ \| | \ \ 
  \____/ \____/ \_____/_/    \_\_|  \_\ 
                                       
                                       \n\nBienvenido al juego 'Adivina el número'""")
    numero_a_adivinar = random.randint(1, 100)
    juego_activo = True
    rondas = 0

    while juego_activo:
        intento = input("Adivina el número (1-100) o escribe 'salir' para terminar: ")
        if intento == "salir":
            juego_activo = False
            print("Gracias por jugar 'Adivina el número'")
        else:
            try:
                num = int(intento)
                if num == numero_a_adivinar:
                    rondas = rondas + 1
                    print(f"¡Felicitaciones, adivinaste el número! Lo has adivinado en {rondas} intentos.")
                    juego_activo = False
                elif num < numero_a_adivinar:
                    print("El número a adivinar es más grande")
                    rondas = rondas + 1
                elif num > 100:
                    print("No puedes poner más de 100!")
                else:
                    print("El número a adivinar es más pequeño")
                    rondas = rondas + 1
            except ValueError:
                print("Por favor, ingrese un número válido o escriba 'salir'")