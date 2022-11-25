import random
'''
3 Cas Python Fundamentals
x = 10

if x > 0:
    print("x je pozitivan broj.")

else:
    print("x je negativan broj.")
'''
'''
vozilo_u_pokretu = True
brzina = 60

if vozilo_u_pokretu == True:
    print("Vozilo se krece...")
    print("Proverite i brzinu...")
    if brzina > 50:
        print("Prekoracena brzina!")
    print("Ovo izvrsavam kolika god da je brzina")
    if brzina <= 50:
        print("Brzina je ok")

if vozilo_u_pokretu = False:
    print("Vozilo se ne krece...")
'''
#1 - prikaz ; 2 - kupovina; 3 - izlaz
proizvod = "Duks"
cena = 3000

# komanda = int(input("Unesite komandu:  "))

# if komanda == 1:
#     print("Prikazi proizvode")
#     print("Proizvod:", proizvod, "Cena:", cena)
    
# if komanda == 2:
#     print("Kupovina")
#     stanje = int(input("Unesite stanje na racunu:  "))
#     if stanje >= cena:
#         print("Uspesna kupovina!")
        
#     if  stanje < cena:
#         print("Neuspesna kupovina...")

# if komanda == 3:
#     print("Izlaz")

# broj = int(input("Upisite broj: "))
# if broj > 0:
#     print("Broj je veci od nule.")
    
# else:
#     print("Broj je 0 ili manji od nule.")
'''
marija = False
ksenija = False
katarina = True

devojka_na_dejtu = " "

if marija:
    devojka_na_dejtu = "Marija"

elif ksenija:
    devojka_na_dejtu = "Ksenija"

elif katarina:
    devojka_na_dejtu = "Katarina"

else:
    devojka_na_dejtu = "Sofija"

print("Izlazi sa mnom", devojka_na_dejtu)'''

# automobil_polovan = False
# godiste = 2021
# boja = "crna"

# if (automobil_polovan == True or godiste > 2017) and boja == "crna":
#     print("Kupujem")

'''if not automobil_polovan: #not False -> True | not moze da se koristi za ukljucenje ili iskljucenje zvuka ili dark/light mode.
    print("Automobil je polovan.")'''

# prisutan == True -> prisutan | prisutan == False -> not prisutan

# trenutni_rezultat = random.randint(1 , 100)

# moj_broj = int(input("Unesite broj(od 1 do 100): "))

# if moj_broj > 100 or moj_broj < 1:
#     print("Proverite broj, dozvoljeno od 1 do 100.")
# else:
#     print("Broj masina je",trenutni_rezultat)
#     if moj_broj > trenutni_rezultat:
#         print("Pobedili ste!.")
        
#     elif moj_broj == trenutni_rezultat:
#         print("Identicne vrednosti!")
        
#     else:
#         print("Izgubili ste.")

# pol = input("Unesite pol(m ili z): ")
# poruka = " "

# if pol == "m":
#     poruka = "Hey mister!"
    
# else:
#     poruka = "Hey miss!"

# poruka = "Hey mister!" if pol == "m" else "Hey miss!"
# print(poruka)

# popularan_proizvod = ""
# jesen = False
# ako je jesen, tada je ajvar, a ako nije onda sladoled | ternarni operator
# popularan_proizvod = "Ajvar" if jesen else "Sladoled"
# print(popularan_proizvod)

