import random
import os

def adivina_el_numero():
    print("Bienvenido al juego 'Adivina el número'")
    numero_a_adivinar = random.randint(1, 100)
    juego_activo = True

    while juego_activo:
        intento = input("Adivina el número (1-100) o escribe 'salir' para terminar: ")
        if intento == "salir":
            juego_activo = False
            print("Gracias por jugar 'Adivina el número'")
        else:
            try:
                num = int(intento)
                if num == numero_a_adivinar:
                    print("¡Felicitaciones, adivinaste el número!")
                    juego_activo = False
                elif num < numero_a_adivinar:
                    print("El número a adivinar es más grande")
                elif num > 100:
                    print("No puedes poner más de 100!")
                else:
                    print("El número a adivinar es más pequeño")
            except ValueError:
                print("Por favor, ingrese un número válido o escriba 'salir'")