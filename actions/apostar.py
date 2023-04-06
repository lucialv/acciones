import os


def apostar():
    while True:
        if not os.path.exists('dinero.txt') or os.path.getsize('dinero.txt') == 0:
            with open('dinero.txt', 'w') as f:
                f.write('0')

        with open('dinero.txt', 'r') as f:
            saldo = int(f.read())

        while True:
            apuesta = int(input("Ingrese la cantidad que deseas apostar (0 para salir): "))
            if apuesta == 0:
                break
            elif apuesta > saldo:
                print("No tienes suficiente dinero para apostar esa cantidad.")
            else:
                break
        if apuesta == 0:
            return
        
        import random
        escoger = input("Quieres cara o cruz? ")

        resultado = random.choice(["cruz", "cara"])
        if resultado == "cara" and escoger == "cara":
            premio = apuesta
            print(f"Ganaste la apuesta! Recibes un premio de {premio * 2}")
            saldo += premio
        elif resultado == "cruz" and escoger == "cruz":
            premio = apuesta
            print(f"Ganaste la apuesta! Recibes un premio de {premio * 2}")
            saldo += premio
        else:
            print("Perdió la apuesta!")
            saldo -= apuesta
        otra_vez = input("Quieres volver a apostar? ")
        if otra_vez == "si":
            continue
        elif otra_vez == "no":
            break

        with open('dinero.txt', 'w') as f:
            f.write(str(saldo))
