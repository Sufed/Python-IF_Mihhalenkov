from math import *
from random import *
#14/12/22
a=6
b=4
a=2*a+3*b
b=a/2*b
print({a})

x=17
y=23
y=x+y+1
x=y+x
print({x})

name=input("Nimi ")
print("Привет,",{name})

m=int(input("Введи длину в метрах: "))
km=m/1000
print("Длина в километрах: ", {km})

t=type(9**(1/2))
print({t})











print()
print()
print()
try:
    päev=int(input("Mis päev ja mitu tundi täna on? "))
    if päev==1:
        n="esmaspäev"
        n="6 tundi"
    elif päev==2:
        n="teisipäev"
        n="8 tundi"
    elif päev==3:
        n="kolmapäev"
        n="6 tundi"
    elif päev==4:
        n="neljapäev"
    elif päev==5:
        n="laupäev"
        n="0 tundi"
    else:
        n="vale number"
    print(n)
except:
    print("!!!!!!")
print()
print()
print()
#13/12/22
print("Sisselogimine tahvel")
try:
    vanus=int(input("Kui vana sa oled? "))
    if vanus>=18:
        print("Kas te annate vanematele loa oma Tahvelit vaadata?")
        o=(input("Jah või ei. "))
        if o.lower()=="jah": #upper() будет делать все буквы большими
            print({o})
            print("See on ligipääs teie vanematele.")
            print("Tahvel on kinni.")
        elif o.upper()=="EI":
             print("Sissepääs puudub.")
             print("Tahvel on kinni.")
    if vanus<18:
        print("Juurdepääs vanematele on automaatselt antud.")
except:
    print("Tahvel on kinni.")
print()
print()
print()
try:
    päev=(input("Mis päeva täna on."))
    if päev==("esmaspäev") and päev.isdigit:
        print("Sobib")
    else:
        print("välju või vähe")
except:
    print("Da")
print() 
print()
print()
print("Распорядок дня. (Выходные)")
try:
    aeg=int(input("Mis aeg praegu on? "))
    if aeg==(12):
        print("Magan")
    elif aeg==(13):
        print("Magan")
    elif aeg==(14):
        print("Magan")
    elif aeg==(15):
        print("Просыпаюсь, умываюсь, ем.")
    elif aeg==(16):
        print("Arvuti mängida")
    elif aeg==(17):
        print("Arvuti mängida")
    elif aeg==(18):
        print("Arvuti mängida")
    elif aeg==(19):
        print("Arvuti mängida")
    elif aeg==(20):
        print("Arvuti mängida")
    elif aeg==(21):
        print("Arvuti mängida")
    elif aeg==(22):
        print("Arvuti mängida")
    elif aeg==(23):
        print("Arvuti mängida")
    elif aeg==(0):
        print("За 5 минут делаю уроки и спать")
    elif aeg==(1):
        print("Magan")
    elif aeg==(2):
        print("Magan")
    elif aeg==(3):
        print("Magan")
    elif aeg==(4):
        print("Magan")
    elif aeg==(5):
        print("Magan")
    elif aeg==(6):
        print("Magan")
    elif aeg==(7):
        print("Magan")
    elif aeg==(8):
        print("Magan")
    elif aeg==(9):
        print("Magan")
    elif aeg==(10):
        print("Magan")
    elif aeg==(11):
        print("Magan")
except:
    print("Vale andmetüüp")
print()
print()
print()
r=randint(-100,100)
a=randint(-100,100)
print(f"r={r}\na={a}")
if r>0 and a>0:
    Skv=a**2 #с помощью pass можно проверять работоспособность программы.
    Skr=pi*r**2
    if Skv>Skr:
        print(f"Ruudu pindala {Skv} on suurem ringi pindala {Skr}")
    elif Skr>Skv:
        print(f"Ringi pindala {Skr} on suurem ruudu pindala {Skv}")
    else:
        print("Pindalad on võrdsed. {Skr} m^2")
else:
    print(f"{a} ja {r} peavad > kui 0 olla")
