import random
import os
import time

# Tämä komento tyhjentää terminaalin
# os.system('cls' if os.name == 'nt' else 'clear')

pisteet = 0
bonus = 0

# Peli jossa arvataan numero 1-100 asti, mitä lähellä on tuulee joko viesti "Liian suuri" tai "Liian pieni", pisteet tulee miten lähelle saa oikein ja jos yrityksiä jäi jäljelle
def prosentti(pisteet, bonus):
    yritykset = 0
    vastaus = random.randint(1,100)
    while True:
        summa = int(input("Anna numero 1 - 100: "))
        yritykset += 1

        if summa > vastaus:
            print("Liian suuri")
        if summa < vastaus:
            print("Liian pieni")
        if summa >= 100:
            print("Anna numero 1-100")
        if summa == vastaus:
            print(f"Oikein vastaus on {vastaus}")
            bonustulos = 6 - yritykset 
            pisteet += 20 * bonustulos
            print(pisteet)
            break
        if yritykset >= 5:
            print(f"Yritykset loppu, vastaus oli {vastaus}")
            pisteet += 20
            print(pisteet)
            break
            
        print(f"Yrityksiä käytetty {yritykset}")

# Peli jossa kirjoitetaan mitä ruudulla lukee, idea on että sana tai teksti otetaan satunnaisesti listasta tai tekstitiedostosta.
def kirjoitus():
    print("Kirjoita Hello World")
    oikea = "Hello World"
    vastaus = str(input("Kirjoita: "))
    if oikea == vastaus:
        print("Osaat kirjoittaa :)")
        return
    print("Et osaa kirjoittaa :(")

def numerojärjestys():
    numerot = random.randint(1,10)
    print()

def peli(pisteet, bonus):
    pelit = [prosentti, kirjoitus]
    random.shuffle(pelit)
    for pelifunktio in pelit:
        pelifunktio()
        os.system('cls' if os.name == 'nt' else 'clear')

while True:
    kysymys = input("Haluatko aloittaa pelin, Kyllä = k, Ei = e: ")
    #os.system('cls' if os.name == 'nt' else 'clear')
    if kysymys == "e":
        print("Nähdään seuraavan kerran")
        break
    elif kysymys == "k":
        print("Aloitetaan peli")
        peli(pisteet, bonus)
    else:
        print("Vastaa, Kyllä = k tai Ei = e")
