import os
import json
def inventario():
 # Mostrar el inventario
     # Cargar el inventario desde el archivo, o crear un inventario vacío si el archivo no existe o está vacío
    if not os.path.exists('inventario.txt') or os.path.getsize('inventario.txt') == 0:
        inventario = {}
    else:
        with open('inventario.txt', 'r') as f:
            inventario = json.load(f)
    print("Inventario:")
    for key, value in inventario.items():
        print(f"{key}: {value}")