import random
import os

# Tämä komento tyhjentää terminaalin
# os.system('cls' if os.name == 'nt' else 'clear')

# Peli jossa arvataan numero 1-100 asti, mitä lähellä on tuulee joko viesti "Liian suuri" tai "Liian pieni", pisteet tulee miten lähelle saa oikein ja jos yrityksiä jäi jäljelle
def prosentti():
    yritykset = 0
    vastaus = random.randint(1,100)
    while True:
        print("#" * 20)
        print(" ")
        summa = int(input("Anna numero 1 - 100: "))
        print(" ")
        yritykset += 1
        os.system('cls' if os.name == 'nt' else 'clear')

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

# Peli jossa kirjoitetaan mitä ruudulla lukee, idea on että sana tai teksti otetaan satunnaisesti listasta tai tekstitiedostosta.
def kirjoitus():
    print("Kirjoita Hello World")
    oikea = "Hello World"
    vastaus = str(input("Kirjoita: "))
    if oikea == vastaus:
        print("Osaat kirjoittaa :)")
        return
    print("Et osaa kirjoittaa :(")
    os.system('cls' if os.name == 'nt' else 'clear')

def numerojärjestys():
    numerot = random.randint(1,10)
    print()

def peli():
    pelit = [prosentti, kirjoitus]
    random.shuffle(pelit)
    for pelifunktio in pelit:
        pelifunktio()
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    kysymys = input("Haluatko aloittaa pelin, Kyllä = k, Ei = e: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if kysymys == "e":
        print("Nähdään seuraavan kerran")
        break
    elif kysymys == "k":
        print("Aloitetaan peli")
        peli()
    else:
        print("Vastaa, Kyllä = k tai Ei = e")
