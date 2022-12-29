osoba = ["Sofija", 25, True]
print(osoba[0])

#kljuc : vrednost, kljuc : vrednost, kljuc : vrednost

osoba_recnik = {"ime":"Sofija", "godine":25, "plava": True}
print(osoba_recnik)
print(osoba_recnik["ime"])
print(osoba_recnik["godine"])

for i in osoba_recnik: #Nacin da prodemo kroz recnik
    print(osoba_recnik[i])

for (kljuc, vrednost) in osoba_recnik.items():
    print("Ovo je kljuc:", kljuc)
    print("Ovo je vrednost:", vrednost)

osoba2 = {}

osoba2["ime"] = "Marija"

print(osoba2)

osoba2["ime"] = "Sofija"
print(osoba2)

del osoba2["ime"]
print(osoba2)

poruke = {"en": "Hello", "sr":"Zdravo", "de": "Hallo", "es":"Hola"}
#Ako je jezik en ili sr ili de -> prikazati
# #U suprotnom prikazi gresku

# jezik = input("Unesite jezik(en, sr, de ili es): ")

# if jezik == "en" or jezik == "sr" or jezik == "de" or jezik == "es":
#     print(poruke[jezik])
# else:
#     print("Nemamo ovaj prevod...")

# ENGLESKI: Hello
#SRPSKI: Zdravo
#NEMACKI: Hallo
#SPANSKI: Hola
'''
for (kljuc,vrednost) in poruke.items():
    if kljuc == "en":
        print(f"ENGLESKI: {vrednost}")
    elif kljuc == "sr":
        print(f"SRPSKI: {vrednost}")
    elif kljuc == "de":
        print(f"NEMACKI: {vrednost}")
    elif kljuc == "es":
        print(f"SPANSKI: {vrednost}")
    else:
        print("Nemam prevod na raspolaganju.")


selekcija = {
        "drzava": "Srbija",
        "broj_pobeda": 0,
        "boje_dresova": ["Crvena", "Bela"],
        "brojevi_igraca": [9,5,13, 20]
            }
'''            
#Boja: bela
#Boja: crvena
# for (kljuc, vrednost) in selekcija.items():
    # print(f"KLJUC: {kljuc}")
    # print(f"VREDNOST: {vrednost}")
    # if kljuc == "boje_dresova":
        # for boja in vrednost:
            # print(f"Boja: {boja}")
    # elif kljuc == "brojevi_igraca":
        # for broj in vrednost:
            # print(f"Igrac broj: {broj}")
    # else:
        # print(f"{kljuc.capitalize()}: {vrednost}")

automobil = {
    "marka": "Citroen",
    "model": "C3",
    "boje": ["crvena", "bela", "crna"],
    "alu_felne": False,
    "godiste": 2017,
    "kubikaza": 1.6
}
#Marka: Citroen
#Model: C3
#Boja: crvena
#Boja: bela
#Boja: crna
#Nema alu felne :(
#Godiste: 2017
#Snaga motora je: 1.6
'''
for (kljuc, vrednost) in automobil.items():
    if kljuc == "marka":
        print(f"{kljuc.capitalize()}: {vrednost}")
    elif kljuc == "model":
        print(f"{kljuc.capitalize()}: {vrednost}")    
    elif kljuc == "boje":
        for boja in vrednost:
            print(f"Boja: {boja}")
    elif kljuc == "alu_felne":
        if vrednost == True:
            print("Ima alu felne.")
        else:
            print("Nema alu felne.")        
    elif kljuc == "godiste":
        print(f"{kljuc.capitalize()}: {vrednost}")
    elif kljuc == "kubikaza":
        print(f"Snaga motora je: {vrednost}")

'''
automobili = {
    #kljuc
    "BG-123":   {#vrednost
        "marka": "Citroen",
        "model": "C3",
        "kubikaza": 1.6,
        "boje": ["crvena", "bela", "crna"]
    },#kljuc
     "BG-456": { #vrednost    
        "marka": "Opel",
        "model": "Astra",
        "kubikaza": 2.0,
        "boje": ["plava", "metalik",]
    }, #kljuc
    "BG-789": { #vrednost
        "marka": "Audi",
        "model": "Q2",
        "kubikaza": 2.0,
        "boje": ["srebrna", "metalik"]
    }
}
for reg, detalji in automobili.items():
    print(f"REGISTRACIJA: {reg}")
    # print(f"DETALJI: {detalji}")
    for (stavka, vrednost) in detalji.items():
        print(f"{stavka.capitalize()}: {vrednost}")
        if stavka == "boje":
            for boje in vrednost:
                print(f"Boja: {boje}")
            
        # if stavka == "marka":
        #     print(f"{stavka.capitalize()}: {vrednost}")
        # elif stavka == "model":
        #     print(f"{stavka.capitalize()}: {vrednost}")
        # elif stavka == "kubikaza":
        #     print(f"{stavka.capitalize()}: {vrednost}")
     
kursevi = {
    "PPF": {
        "naziv": "Python Fundamentals",
        "semestar": 1
    },
    "OOP": {
        "naziv": "Python Object Oriented",
        "smestar": 1
    }
}

for id_kursa, detalji in kursevi.items():
    for k, v in detalji.items():
        print(f"{k.capitalize()}: {v}")

#LISTA []
#RECNIK { kljuc: vrednost}
#SKUP / Set {1,2...}
boje_u_ponudi = {"bela","plava","crvena","plava"}
print(boje_u_ponudi)
boje_u_ponudi.add("zuta")
boje_u_ponudi.remove("bela")
print(boje_u_ponudi)
