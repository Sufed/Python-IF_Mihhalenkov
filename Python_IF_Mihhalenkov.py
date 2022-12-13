from math import *
from random import *
#13/12/22
print("Составить алгоритм вывода количества урокав каждый день определяя его порядковому номеру (1 – понедельник, 2 – вторник, 3 – среда, 4 – четверг, 5 – пятница, 6 – суббота, 7 – воскресенье).")
try:
    päev=int(input("Mis päev täna on? "))
    if päev:=("esmaspäev"):
except:
    print("MIS PÄEV TÄNA ON???")




print("Распорядок дня. (Выходные)")
try:
    aeg=int(input("Mis aeg praegu on? "))
except:
    print("da")
try:
    if aeg==(12):
        print("Сплю")
    elif aeg==(13):
        print("Сплю")
    elif aeg==(14):
        print("Сплю")
    elif aeg==(15):
        print("Просыпаюсь, умываюсь, ем.")
    elif aeg==(16):
        print("Играю в компьюктере")
    elif aeg==(17):
        print("Играю в компьюктере")
    elif aeg==(18):
        print("Играю в компьюктере")
    elif aeg==(19):
        print("Играю в компьюктере")
    elif aeg==(20):
        print("Играю в компьюктере")
    elif aeg==(21):
        print("Играю в компьюктере")
    elif aeg==(22):
        print("Играю в компьюктере")
    elif aeg==(23):
        print("Играю в компьюктере")
    elif aeg==(0):
        print("За 5 минут делаю уроки и спать")
    elif aeg==(1):
        print("Сплю")
    elif aeg==(2):
        print("Сплю")
    elif aeg==(3):
        print("Сплю")
    elif aeg==(4):
        print("Сплю")
    elif aeg==(5):
        print("Сплю")
    elif aeg==(6):
        print("Сплю")
    elif aeg==(7):
        print("Сплю")
    elif aeg==(8):
        print("Сплю")
    elif aeg==(9):
        print("Сплю")
    elif aeg==(10):
        print("Сплю")
    elif aeg==(11):
        print("Сплю")
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
