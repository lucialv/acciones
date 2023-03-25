import json
import os

def tienda():
    productos = {
        "1": ("iPhone", 1100),
        "2": ("MacBook", 8000),
        "3": ("iPad", 800),
        "4": ("AirPods", 250),
        "5": ("Pc gaming", 2000),
        "6": ("Ferrari", 100000),
        "7": ("Lamborghini", 250000),
        "8": ("Mansion", 1500000),
        "9": ("Barco", 100000),
        "10": ("Oficinas", 1000000)
    }

    # Verificar si el archivo de dinero existe y si está vacío
    if not os.path.exists('dinero.txt') or os.path.getsize('dinero.txt') == 0:
        with open('dinero.txt', 'w') as f:
            f.write('0')  # Establecer un saldo predeterminado

    with open('dinero.txt', 'r') as f:
        saldo = int(f.read().strip())

    # Cargar el inventario desde el archivo, o crear un inventario vacío si el archivo no existe o está vacío
    if not os.path.exists('inventario.txt') or os.path.getsize('inventario.txt') == 0:
        inventario = {}
    else:
        with open('inventario.txt', 'r') as f:
            inventario = json.load(f)

    while True:
        print("PRODUCTOS DISPONIBLES")
        for key, value in productos.items():
            print(f"{key}: {value[0]} (${value[1]})")

        producto = input("Ingrese el número del producto que desea comprar (0 para salir): ")
        if producto == "0":
            break

        if producto not in productos.keys():
            print("Producto no disponible")
            continue

        precio = productos[producto][1]
        print(f"El precio de {productos[producto][0]} es ${precio}")
        dinero = int(input("Ingrese el precio del producto para confirmar: "))

        if dinero < precio:
            print("Usted no tiene el dinero suficiente o no has escrito la cantidad de dinero adecuada para este objeto!")
            continue

        # Actualizar el saldo en el archivo
        with open('dinero.txt', 'w') as f:
            f.write(str(saldo - precio))

        # Actualizar el inventario
        if productos[producto][0] in inventario:
            inventario[productos[producto][0]] += 1
        else:
            inventario[productos[producto][0]] = 1

        with open('inventario.txt', 'w') as f:
            json.dump(inventario, f)

        print(f"Usted compró {productos[producto][0]} por ${precio}")

    # Mostrar el inventario al final
    print("INVENTARIO")
    for key, value in inventario.items():
        print(f"{key}: {value}")

