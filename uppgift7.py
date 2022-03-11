#moduler
import time

#Funktioner
def area_cirkel():
    a = int(input("Ange cirkelns radie i cm! "))
    sum = a * a * 3.14 
    return sum
def omkrets_cirkel():
    a = int(input("Ange cirkelns diameter i cm!"))
    sum = a*3.14
    return sum
def volym_klot():
    a = int(input("Ange Klotets radie! "))
    sum = (4*3.14*a**3)/3
    return sum
def volym_rätblock():
    a = int(input("Ange höjden i cm! "))
    b = int(input("Ange djupet i cm! "))
    c = int(input("Ange längden i cm! "))
    sum = a*b*c
    return sum

fraga = ""
while fraga != "5":
    #huvudfråga!
    print("Vad vill du göra?")
    print("1. Beräkna arean på en cirkel")
    print("2. Beräkna omkretsen på en cirkel")
    print("3. Beräkna volymen på ett klot")
    print("4. Beräkna volymen på ett rätblock")
    print("5. Avsluta")
    fraga = input()
    fraga = fraga.lower()
    #if-satser
    if fraga == "1":
        summa = area_cirkel()
        print(f"Cirkelns area är: {summa} cm2!")
        time.sleep(3)
    if fraga == "2":
        summa = omkrets_cirkel()
        print(f"Cirkelns omkrets är: {summa} cm!")
        time.sleep(3)
    if fraga == "3":
        summa = volym_klot()
        print(f"Klotets volym är: {summa} cm3!")
        time.sleep(3)
    if fraga == "4":
        summa = volym_rätblock()
        print(f"Rätblockets volym är: {summa} cm3!")
        time.sleep(3)

print("HEJDÅÅÅÅÅÅÅÅÅÅ!!!")