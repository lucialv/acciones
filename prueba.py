import pytz
import datetime
asd = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
       2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, "2022: "]
no = ['no', 'nop', 'claro que no', 'obviamante, no', 'obvio no', 'no se']

años = None
sexo = None
guapo = None


try:
    nombre = str(input("Como te llamas? ")).capitalize()
    sexo = str(input("Eres masculino o femenino?: ")).lower()
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


def sexo():
    if sexo.find("masculino"):
        print("Te identificas como un chico")
    elif sexo.find("femenino"):
        print("Te identificas como una chica")
    else:
        print("Te identificas como otra cosa")


def Edad():

    try:
        if resultado >= 40:
            print("Tienes "+str(resultado)+" años, puto viejo!")
        elif resultado <= 39:
            print("Tienes "+str(resultado)+" años.")
    except TypeError:
        pass
    finally:
        pass


def Altura():
    try:
        if resultado1 >= 190:
            print("Mides "+str(resultado1)+"cm, puta torre.")
        elif resultado1 <= 189:
            print("Mides "+str(resultado1)+"cm.")
    except TypeError:
        pass
    finally:
        pass
# tz_NY = pytz.timezone('America/New_York')
# datetime_NY = datetime.now(tz_NY)
# print("NY time:", datetime_NY.strftime("%H:%M:%S"))


def Vivir():
    try:
        if vivir:
            print("Mides "+str(resultado1)+"cm, puta torre.")
        elif vivir <= 189:
            print("Mides "+str(resultado1)+"cm.")
    except TypeError:
        pass
    finally:
        pass


print("Hola "+nombre)
sexo()
Edad()
Altura()
Atractivo()

my_date = datetime.datetime.now(pytz.timezone('EUROPE/MADRID'))
data = str(my_date)
print("Programa ejecutado el " + data)
