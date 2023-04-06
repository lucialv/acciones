from plyer import notification
import time

def hidratacion():
    
    contador = 0
    while True:
        try:
            tiempoo = float(input("Cada cuanto tiempo quieres que te recuerde que tienes que hidratarte? (en segundos y si es decimal en .) "))
        except ValueError:
            print("No puedes usar un , o escribir letras! ")
            continue
        finally:
            break
    tiempo = tiempoo
    while True:
            notification.notify(
                title="Tomar agua",
                message="¡Recuerda tomar aguita! "+ "x"+ str(contador),
                app_name="Hidratación",
                timeout=10
            )
            time.sleep(tiempo)
            contador += 1   

