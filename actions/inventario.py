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
    print("""
  _____ _   ___      ________ _   _ _______       _____  _____ ____  
 |_   _| \ | \ \    / /  ____| \ | |__   __|/\   |  __ \|_   _/ __ \ 
   | | |  \| |\ \  / /| |__  |  \| |  | |  /  \  | |__) | | || |  | |
   | | | . ` | \ \/ / |  __| | . ` |  | | / /\ \ |  _  /  | || |  | |
  _| |_| |\  |  \  /  | |____| |\  |  | |/ ____ \| | \ \ _| || |__| |
 |_____|_| \_|   \/   |______|_| \_|  |_/_/    \_\_|  \_\_____\____/ 
                                                                     
                                                                     \n\n""")
    for key, value in inventario.items():
        print(f"{key}: {value}")