
# # marka, model, godiste, parkiran
# class Automobil:
#     def __init__(self, marka, model, godiste, parkiran=False):
#         self.marka = marka
#         self.model = model
#         self.godiste = godiste
#         self.parkiran = parkiran
#     # Marka: ... Model: ... Godiste: ... Parkiran / U pokretu
#     def informacije(self):
#         status = "Parkiran" if self.parkiran else "U Pokretu"
#         return f"Marka: {self.marka}\nModel: {self.model}\nGodiste: {self.godiste}\n{status}"
#     def info_o_automobili():
#         print("Automobili imaju 4 tocka")
#         print("Najcesce se registruju jednom godisnje")
    
    
#     def parkiraj(self):
#         if self.parkiran == True:
#             print("Vec ste parkirani")
#         else:
#             self.Parkiram + True
#     #init

# automobil2 = Automobil("Citroen", "C5", 2021, True)
# # "Marka: Citroen"
# print(f"Model: {automobil2.marka}")
# print(automobil2.model)
# print(automobil2.informacije())

# automobil2 = Automobil("Ford", "Focus", 2020)
# #pozvati metod
# print(automobil2.informacije())
# print(automobil2.info_o_automobili())


#Tip (strg) brih jirusbuta (int) mockup (bool) preuzeta_za rad (bool)

class Aplikacija:
    def __init__(self, tip , broj_korisnika, mockup, preuzeta_za_rad):
        self.tip = tip
        self.broj_korisnika = broj_korisnika
        self.mockup = mockup
        self.preuzeta_za_rad = preuzeta_za_rad

app1 = Aplikacija("Veb aplikacija", 1200, True, False)
app2 = Aplikacija("iOS aplikacija", 1300, False, False)
app3 = Aplikacija("Android aplikacija", 1800, True, False)

class Firma:
    def __init__(self, naziv, broj_zaposlenih, registrovana = False):
        self.naziv = naziv
        self.broj_zaposlenih = broj_zaposlenih
        self.registrovana = registrovana
        
    def zaposli_nove(self,broj_novih):
        if broj_novih <= 0:
            print("Prosledite broj veci od 0.")
        else:
            self.broj_zaposlenih += broj_novih
            print(f"Zaposleno je novih {broj_novih}, trenutni broj je {self.broj_zaposlenih}")
    
    def otkaz(self, broj_otkaza):
        if broj_otkaza > self.broj_zaposlenih or broj_otkaza < 0:
            print("Previse za otpustanje ili neodgovarajuci unos. ")
        else:
            self.broj_zaposlenih -= broj_otkaza
            print(f"Otpusteno je {broj_otkaza}, trenutni broj zaposlenih je {self.broj_zaposlenih} ")
    # Da li aplikacija ima mockup i ako nema, ne uzimam projekat
    def preuzmi_projekat(self, projekat):
        if projekat.mockup:
            print(f"Preuzet je projekat {projekat.tip}")
            projekat.preuzeta_za_rad = True
        else:
            print("Donesite i mockup")
        

moja_firma = Firma("ITAcademy", 300, True)
moja_firma.zaposli_nove(10)
print(moja_firma.broj_zaposlenih)
moja_firma.otkaz(15)
moja_firma.preuzmi_projekat(app3)

#PROIZVOD - NAZIV, OPIS, CENA
# KORPA - SPISAK_PROIZVODA, UKUPNA_CENA

class Proizvod:
    def __init__(self, naziv, opis, cena):
        self.naziv = naziv
        self.opis = opis
        self.cena = cena


#korpa u inicijalizatori prihvata listu proizvoda tipa Proizvod

class Korpa:
    def __init__(self, spisak_proizvoda):
        self.spisak_proizvoda = spisak_proizvoda #svojstvo 1
        res = 0
        for pr in spisak_proizvoda:
            res += pr.cena

        self.ukupna_cena = res      #svojstvo 2

pr1 = Proizvod("Patike", "Fudbalske patike", 27000)
pr2 = Proizvod("Patike", "Kosarkaske patike", 15000)
pr3 = Proizvod("Papuce", "Crocs", 5000)

lista_pr = []
lista_pr.append(pr1)
lista_pr.append(pr2)

korpa = Korpa(lista_pr)
print(korpa.ukupna_cena)

    
    
