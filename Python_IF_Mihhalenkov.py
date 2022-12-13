from math import *
from random import *
#13/12/22
print("Sisselogimine tahvel")
try:
    vanus=int(input("Kui vana sa oled? "))
    if vanus>18:
        print("Kas te annate vanematele loa oma Tahvelit vaadata?")
        o=(input("Jah või ei. "))
        if o==("Jah") or ("ei"):
            print("{o}")
            if o==("Jah"):
                print("See on ligipääs teie vanematele.")
            else:
                o==("Ei")
                print("Sissepääs puudub.")
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
except:
    print("da")
try:
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
