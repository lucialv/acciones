comidas = list()

# while True:
#     comida = input("Que comida quieres: ")
#     if comida == "salir":
#         break
#     comidas.append(comida)

while food := input("Que comida te gusta?: ") != "salir":
    comidas.append(food)
