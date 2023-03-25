def leer_dinero():
    with open('dinero.txt', 'r') as f:
        dinero_actual = f.read()
        print(f"""
  ____          _   _  _____ ____  
 |  _ \   /\   | \ | |/ ____/ __ \ 
 | |_) | /  \  |  \| | |   | |  | |
 |  _ < / /\ \ | . ` | |   | |  | |
 | |_) / ____ \| |\  | |___| |__| |
 |____/_/    \_\_| \_|\_____\____/ 
                                                               
        \n\nActualmente tines {dinero_actual}$""")
        return int(dinero_actual)
        
