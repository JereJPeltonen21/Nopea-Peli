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
    # Jos random numerointi on liian vaikea niin voi vaihtaa "random.randint(1,100)" tilalle numeron joka toimii vastauksena
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
            return pisteet
        if yritykset >= 5:
            print(f"Yritykset loppu, vastaus oli {vastaus}")
            pisteet += 20
            return pisteet
            
        print(f"Yrityksiä käytetty {yritykset}")

# Peli jossa kirjoitetaan mitä ruudulla lukee, idea on että sana tai teksti otetaan satunnaisesti listasta tai tekstitiedostosta.
def kirjoitus(pisteet, bonus):
    print("Kirjoita Hello World")
    oikea = "Hello World"
    vastaus = str(input("Kirjoita: "))

    if oikea == vastaus:
        print("Osaat kirjoittaa :)")
        pisteet += 50
        return pisteet
    
    print("Et osaa kirjoittaa :(")
    return pisteet

def numerojärjestys(pisteet, bonus):
    numerot = random.randint(1,10)
    print()
    return pisteet

def lasku(pisteet, bonus):
    print("Nopeasti, Mikä on 2 + 2")
    vastaus = 4
    kysymys = int(input("Kirjoita vastaus: "))
    if kysymys == vastaus:
        print("Osaat laskea :)")
        pisteet += 50
        return pisteet
    
    print("Et osaa laskea :()")
    return pisteet

def peli5(pisteet, bonus):
    numerot = random.randint(1,10)
    print()
    return pisteet


def peli(pisteet, bonus):
    pelit = [prosentti, kirjoitus, lasku]
    random.shuffle(pelit)

    for pelifunktio in pelit:
        pisteet = pelifunktio(pisteet, bonus)
        
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

    return pisteet

while True:
    kysymys = input("Haluatko aloittaa pelin, Kyllä = k, Ei = e: ")
    if kysymys == "e":
        print(f"Peli päättyi! Sait yhteensä {pisteet} pistettä.")
        print("Nähdään seuraavan kerran")
        break
    elif kysymys == "k":
        print("Aloitetaan peli")
        pisteet = peli(pisteet, bonus)
    else:
        print("Vastaa, Kyllä = k tai Ei = e")
