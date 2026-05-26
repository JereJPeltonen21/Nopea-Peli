import random
import os
import time
import csv

# Tämä komento tyhjentää terminaalin
# os.system('cls' if os.name == 'nt' else 'clear')

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
            print(" ")
        if summa < vastaus:
            print("Liian pieni")
            print(" ")
        if summa >= 100:
            print("Anna numero 1-100")
            print(" ")
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
    numerot = [random.randint(0, 9) for n in range(5)]
    print(f"Laita numerot {numerot}, oikeaan järjestykseen")
    for n in sorted(numerot):
        pelaaja = int(input("Anna seuraava numero: "))
        if pelaaja == n:
            print("Oikein")
        else:
            print("Väärin")
            return pisteet

    print("Kaikki oikein!")
    pisteet += 50
    return pisteet

def peli4(pisteet, bonus):
    numero = random.randint(1,100)
    print(f"Onko {numero} parillinen vai pariton")
    vastaus = int(input("Vastaus (0 = parillinen, 1 = pariton): "))
    if numero % 2 == vastaus:
        print("Oikein")
        pisteet += 50
    else:
        print("Väärin")
        pisteet += 10
    
    return pisteet

def lasku(pisteet, bonus):
    numero1 = random.randint(1,9)
    numero2 = random.randint(1,9)

    print(f"Nopeasti, Mikä on {numero1} + {numero2}")

    vastaus = numero1 + numero2
    kysymys = int(input("Kirjoita vastaus: "))
    if kysymys == vastaus:
        print("Osaat laskea :)")
        pisteet += 50
        return pisteet
    
    print("Et osaa laskea :(")
    return pisteet

def peli5(pisteet, bonus):
    pelaaja_voitto = 0
    ai_voitto = 0

    while True:
        pelaaja = str(input("Vastaa, k = kivi, s = sakset tai p = paperi: "))
        print(" ")
        ksp = ["kivi", "saksi", "paperi"]
        ai = random.choice(ksp)

        print(f"Valitsit {pelaaja}, ai valitsi {ai}")
        print(" ")
        pelaaja = pelaaja.lower().strip()

        if pelaaja == ai:
            print(f"Tasapeli, AI valitsi {ai}")

        elif pelaaja.startswith("k"):
            if ai == "saksi":
                print("Kivi päihittää sakset, voitit!")
                print(" ")
                pelaaja_voitto += 1
            else:
                print("Paperi päihittää kiven, hävisit!")
                print(" ")
                ai_voitto += 1

        elif pelaaja.startswith("p"):
            if ai == "kivi":
                print("Paperi päihittää kiven, voitit!")
                print(" ")
                pelaaja_voitto += 1
            else:
                print("Sakset päihittää paperin, hävisit!")
                print(" ")
                ai_voitto += 1

        elif pelaaja.startswith("s"):
            if ai == "paperi":
                print("Sakset päihittää paperin, voitit!")
                print(" ")
                pelaaja_voitto += 1
            else:
                print("Kivi päihittää sakset, hävisit!")
                print(" ")
                ai_voitto += 1

        if pelaaja_voitto >= 3:
            print("Voitit")
            pisteet += 50
            break

        elif ai_voitto >= 3:
            print("Hävisit, Ai voitti :(")
            pisteet += 25
            break

        print(f"Pelaaja {pelaaja_voitto} - AI {ai_voitto}")
        print(" ")

    return pisteet

# Runko uusille pelille
"""
def pelinimi(pisteet, bonus):
    # Pelikoodi

    pisteet += 50
    return pisteet
"""


def peli(pisteet, bonus):
    pelit = [prosentti, kirjoitus, lasku, peli5, peli4, numerojärjestys]
    random.shuffle(pelit)

    for pelifunktio in pelit:
        pisteet = pelifunktio(pisteet, bonus)
        
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

    return pisteet
    
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    pisteet = 0
    bonus = 0

    menu1 = "Aloita peli = k"
    menu2 = "Leaderboard = l"
    menu3 = "Lopeta peli = e"
    menu4 = " "

    tyhjä = menu4.center(48)
    keski = menu1.center(48)
    keski2 = menu2.center(48)
    keski3 = menu3.center(48)

    print("*" * 50)
    print("*" + tyhjä + "*")
    print("* | \ | |                        |  __ \   | (_) *")
    print("* |  \| | ___  _ __   ___  __ _  | |__) |__| |_  *")
    print("* | . ` |/ _ \| '_ \ / _ \/ _` | |  ___/ _ \ | | *")
    print("* | |\  | (_) | |_) |  __/ (_| | | |  |  __/ | | *")
    print("* |_| \_|\___/| .__/ \___|\__,_| |_|   \___|_|_| *")
    print("*             | |                                *")
    print("*             |_|                                *")
    print("*" + tyhjä + "*")

    print("*" + tyhjä + "*")
    print("*" + keski + "*")
    print("*" + keski2 + "*")
    print("*" + keski3 + "*")
    print("*" + tyhjä + "*")
    print("*" * 50)
    kysymys = input("Valinta: ")

    if kysymys == "e":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Nähdään seuraavan kerran")
        break

    elif kysymys == "k":
        start = time.time()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Aloitetaan peli")
        pisteet = peli(pisteet, bonus)
        end = time.time()
        
        elapsed = end - start
        
        # pistekerroin = keskiverto_aika / kulunut_aika
        nimi = str(input("Anna nimi: "))
        lopputulos = int(60 / elapsed * pisteet)
        print(f"Sait {lopputulos} pistettä")

        f = open("leaderboard.csv", "a")
        f.write(f"\n{nimi},{lopputulos}\n")
        f.close()

    elif kysymys == "l":
        os.system('cls' if os.name == 'nt' else 'clear')
        with open('leaderboard.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            leaderboard = []
            for row in reader:
                leaderboard.append(row)
            leaderboard.sort(reverse=True, key=lambda row: row["pisteet"])
            for row in leaderboard[:10]:
                print(f"{row["nimi"]}: {row["pisteet"]}")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Vastaa, Kyllä = k, Ei = e tai Leaderboard = l")
    

