def matar():
    armas = ["cuchillo", "ak-47", "pistola", "metralleta", "llaves","katana", ""]
    persona_o_cosa_para_matar = None
    while persona_o_cosa_para_matar != "salir":
        persona_o_cosa_para_matar = input("Que quieres matar hoy? ").lower()

        #Si la persona que queremos matar es igual a salir entonces nos saldremos del programa
        if persona_o_cosa_para_matar == "salir":
            break

        #Si la persona que queremos matar no es igual a salir entonces seguira el programa y me preguntará con que arma lo queremos matar
        arma = input(f"Con que arma quieres matar a {persona_o_cosa_para_matar.capitalize()}? ")


        #Si el arma está en armas se ejecuta esto
        if arma in armas:
            if arma == "cuchillo":
                print(f"Has rebanado hasta la muerte a {persona_o_cosa_para_matar.capitalize()} con un {arma}")
            elif arma == "pistola":
                print(f"Has disparado hasta no dejar nada de {persona_o_cosa_para_matar.capitalize()} con un {arma}")
            elif arma == "katana":
                print(f"Has rebanado hasta la muerte a {persona_o_cosa_para_matar.capitalize()} con un {arma}")
            else:
                print(f"Has matado a {persona_o_cosa_para_matar.capitalize()} con {arma}.")
        elif arma == "salir":
            break
        #si el arma no está en armas se ejecuta esto
        else:
            print(f"No estoy seguro que {arma} sea un arma pero, has matado a {persona_o_cosa_para_matar} con {arma}.")