import pytz
import datetime
asd = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
       2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, "2022: "]
no = ['no', 'nop', 'claro que no', 'obviamante, no', 'obvio no', 'no se', 'jan', 'negativo', 'nopi' ]

años = None
sexo = None
guapo = None


try:
    nombre = input("Como te llamas? ").lower()
    sexo = input("Como te identificas?: ").lower()
    años = int(input("Cuando naciste? "+(', '.join(map(str, asd)))))
    guapo = input("Eres guapo? ").lower()
    altura = float(input("Dime tu altura: "))
    vivir = input("Donde vives? ")

except ValueError:
    print("No puedes poner letras tonto.")

finally:
    pass


def Atractivo():
    if any(response in guapo for response in no):
        print("Eres feo. ")
    else:
        print("Eres guapo. ")


def Sexo():
    print(f"Te identificas como {sexo}")


resultado = 2022-años


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
        if altura >= 190:
            print(f"Mides {altura} cm, puta torre.")
        elif altura <= 189:
            print(f"Mides {altura} cm.")
    except ValueError:
        print("Por favor ingresa un número válido.")
    finally:
        pass

def Vivir():
    try:
        print(f"Vives en {vivir}.")
    except TypeError:
        pass
    finally:
        pass


if nombre.find("jan") != -1:
    print("-------------------------------------------\nHola"+ nombre.capitalize()+" guapoo")
else:
    print("-------------------------------------------\nHola " + nombre.capitalize())
Sexo()
Edad()
Altura()
Atractivo()
Vivir()

my_date = datetime.datetime.now(pytz.timezone('EUROPE/MADRID'))
data = str(my_date)
print("-------------------------------------------\nPrograma ejecutado el " + data)
