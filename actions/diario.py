import datetime
import os
def diario():
    escribir_ver = input("Quieres escribir o ver el tu diario? ") #aquí pregunta para decidir si escribir o leer el diario
    if escribir_ver == "escribir":
        escribir_diario()
    elif escribir_ver == "leer" or escribir_ver == "ver":
        leer_diario()

def escribir_diario(): #función de escribir en el diario
    fecha = datetime.datetime.now()
    texto = input("¿Qué quieres escribir para el día de hoy: ") #input para el texto que se pondrá en el diario
    with open('diario.txt', 'a') as f:
        f.write("\n"+fecha.strftime('Dia %Y-%m-%d a las %H:%M:%S') + f": {texto}") #se escribe el texto en el diario



def leer_diario(): #función de leer en el diario
    pagina = input("¿Qué página quieres leer? ") #input para saber la pagian
    with open('diario.txt', 'r') as f:
        contenido = f.read()
        lineas = contenido.splitlines()
        if len(lineas) < int(pagina):
            print("La página no existe.") #si la pagina no existe pondrá este print
        else:
            print(lineas[int(pagina)-1]) #si existe hará print(la pagina dicha)


