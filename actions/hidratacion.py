from plyer import notification
import time

def hidratacion():
    tiempo = int(input("Cada cuanto tiempo quieres que te recuerde que tienes que hidratarte? (en segundos) "))
    while True:
        notification.notify(
            title="Tomar agua",
            message="¡Recuerda tomar aguita!",
            app_name="Hidratación",
            timeout=10
        )
        time.sleep(tiempo)
        

