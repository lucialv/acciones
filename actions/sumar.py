def sumar():
    x = int(input("Dime el primer numero: "))
    y = int(input("Dime el segundo numero: "))
    resultado = x + y
    print(f"La suma entre {x} y {y} es {resultado}")

def multiplicar():
    x = int(input("Dime el primer numero: "))
    y = int(input("Dime el segundo numero: "))
    resultado = x * y
    print(f"La multiplicación entre {x} y {y} es {resultado}")

def restar():
    x = int(input("Dime el primer numero: "))
    y = int(input("Dime el segundo numero: "))
    resultado = x - y
    print(f"La resta entre {x} y {y} es {resultado}")

def dividir():
    x = int(input("Dime el primer numero: "))
    y = int(input("Dime el segundo numero: "))
    resultado = x / y
    print(f"La división entre {x} y {y} es {resultado}")


def calculadora():
    calculo = None
    while calculo != "salir":
        calculo = input("""
   _____          _      _____ _    _ _               _____   ____  _____            
  / ____|   /\   | |    / ____| |  | | |        /\   |  __ \ / __ \|  __ \     /\    
 | |       /  \  | |   | |    | |  | | |       /  \  | |  | | |  | | |__) |   /  \   
 | |      / /\ \ | |   | |    | |  | | |      / /\ \ | |  | | |  | |  _  /   / /\ \  
 | |____ / ____ \| |___| |____| |__| | |____ / ____ \| |__| | |__| | | \ \  / ____ \ 
  \_____/_/    \_\______\_____|\____/|______/_/    \_\_____/ \____/|_|  \_\/_/    \_\ 
                                                                                     
                                                                                     \n\nQue quieres? ¿Sumar, multiplicar, restar o dividir? """).lower()
        if calculo == "sumar":
            sumar()
        elif calculo == "restar":
            restar()
        elif calculo == "dividir":
            dividir()
        elif calculo == "multiplicar":
            multiplicar()
        elif calculo == "salir":
            break
        else:
            print(f"Creo que no tengo {calculo}, por favor intentelo de nuevo. ")
