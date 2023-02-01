import pyautogui
import time

intervalo = float(
    input("Ingresa el tiempo de espera entre mensajes (en segundos): "))
contador = 0

while True:
    contador += 1
    mensaje = "{} día diciendo que la conxita es más fea que un culo".format(
        contador)
    pyautogui.write(mensaje)
    pyautogui.press("enter")
    time.sleep(intervalo)
