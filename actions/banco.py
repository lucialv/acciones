def leer_dinero():
    with open('dinero.txt', 'r') as f:
        dinero_actual = f.read()
        print(f"Actualmente tines {dinero_actual}$")
        return int(dinero_actual)
        
