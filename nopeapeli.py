import random

def prosentti():
    yritykset = 0
    vastaus = random.randint(1,100)
    while True:
        print("#" * 20)
        print(" ")
        summa = int(input("Anna numero 1 - 100: "))
        print(" ")
        yritykset += 1

        if summa > vastaus:
            print("Liian suuri")
            print(" ")
        if summa < vastaus:
            print("Liian pieni")
            print(" ")
        if summa >= 100:
            print("Anna numero 1-100")
            print(" ")
        if summa == vastaus:
            print(f"Oikein vastaus on {vastaus}")
            print(" ")
            break
        if yritykset >= 5:
            print(f"Yritykset loppu, vastaus oli {vastaus}")
            print(" ")
            break
            
        print(f"Yrityksiä käytetty {yritykset}")
        print(" ")

def kirjoitus():
    print("Kirjoita Hello World")
    oikea = "Hello World"
    vastaus = str(input("Kirjoita: "))
    if oikea == vastaus:
        print("Osaat kirjoittaa :)")
        return
    print("Et osaa kirjoittaa :(")

def peli():
    pelit = [prosentti, kirjoitus]
    random.shuffle(pelit)
    for pelifunktio in pelit:
        pelifunktio()
    

while True:
    kysymys = input("Haluatko aloittaa pelin, Kyllä = k, Ei = e: ")
    if kysymys == "e":
        print("Nähdään seuraavan kerran")
        break
    elif kysymys == "k":
        print("Aloitetaan peli")
        peli()
    else:
        print("Vastaa, Kyllä = k tai Ei = e")
