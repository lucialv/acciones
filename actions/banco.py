def leer_dinero():
    with open('dinero.txt', 'r') as f:
        dinero_actual = f.read()
        print(dinero_actual)
        return int(dinero_actual)
        
leer_dinero()
