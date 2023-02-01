import pytz
import datetime
asd = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
       2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, "2022: "]
no = ['no', 'nop', 'claro que no', 'obviamante, no', 'obvio no', 'no se']

años = None
sexo = None
guapo = None


try:
    nombre = input("Como te llamas? ").capitalize()
    sexo = input("Como te identificas?: ").lower()
    años = int(input("Cuando naciste? "+(', '.join(map(str, asd)))))
    guapo = input("Eres guapo? ").lower()
    resultado1 = int(input("Dime tu altura: "))
    vivir = input("Donde vives? ")

except ValueError:
    print("No puedes poner letras tonto.")
    pass

finally:
    pass


def Atractivo():
    if guapo.find("no") != -1:
        print("Eres feo. ")
    elif guapo.find("no") == -1:
        print("Eres guapo. ")
    else:
        print("No te entiendo gilipollas")


resultado = 2022-años


def Sexo():
    print(f"Te identificas como {sexo}")


def Edad():

    try:
        if resultado >= 40:
            print(f"Tienes {resultado} años, puto viejo!")
        elif resultado <= 39:
            print(f"Tienes {resultado} años.")
    except TypeError:
        pass
    finally:
        pass


def Altura():
    try:
        if resultado1 >= 190:
            print(f"Mides {resultado1} cm, puta torre.")
        elif resultado1 <= 189:
            print(f"Mides {resultado1} cm.")
    except TypeError:
        pass
    finally:
        pass


def Vivir():
    try:
        print(f"Vives en {vivir}")
    except TypeError:
        pass
    finally:
        pass


print("Hola "+nombre)
Sexo()
Edad()
Altura()
Atractivo()
Vivir()

my_date = datetime.datetime.now(pytz.timezone('EUROPE/MADRID'))
data = str(my_date)
print("Programa ejecutado el " + data)
