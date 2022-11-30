# #           0       1     2      3
# osoba = ["Sofija", 20, "plava", True ]
# # lista/niz == []
# print(osoba[0])
# print("Godine:", osoba[1])
# print("Boja kose", osoba[2])
# print("Zauzeta(?)", osoba[3])

# automobili = ["Opel", "Citroen", "Mercedes"]
# print(automobili[1])

# Range - opseg - rango
# for x in range(10, 2, -1):
#     print(x)

#String
       #012345
# kurs = "PYTHON"
# for x in kurs:
#     print(x)

# Index
# kurs = "Python"

# for x in range(len(kurs)):
#     print("Na poziciji:", x, kurs[x])

# # print(kurs[0])
# print(kurs[1])
# print(kurs[2])
# print(kurs[3])
# print(kurs[4])
# print(kurs[5])

# ustanova = "IT Academy"
# for index in range(len(ustanova)):
#     print(ustanova[index])

'''
len = operacija nad stringom / prebrojavanje karaktera
'''

# primer = "zadatak1"

# for indeks in range(len(primer)):
#     print(primer[indeks], end=" ")

# broj_karaktera = len(primer)
# print(broj_karaktera)
# indeks = 0
# while indeks < broj_karaktera:
#     print(primer[indeks]) 
#     indeks += 1

# korisnicko_ime = "admin"
# # uneto_kor_ime = input("Unesi korisnicko ime: ").lower()

# if korisnicko_ime == uneto_kor_ime: # ili uneto_kor_ime.lower()
#        print("Dobrodosli!", uneto_kor_ime)
# else:
#        print("Pogresni podaci")


# Sekvence vezba 11.30.2022
# proizvodi = ["Telefon", "Tv","Laptop"]
# cene      = [   100,    200,   300]

# for x in range(len(proizvodi)): #len para ir producto por producto de la lista.
#     print(proizvodi[x], cene[x]) 

# automobili = ["Audi", "BMW", "Yugo", "Citroen", "Kia", "Peugot"]

# for i in range(len(automobili)): # for i in range(6): ...
#     print("Automobil:", automobili[i]) # No es necesario
#     if i == 3:
#         print('Aleksandra vozi automobil', automobili[i],'!')
#     else:
#         continue


#Visedimenzionalne liste
proizvodi = [      # 0            # 1           #2          
                ["Iphone 11", "Samsung s22", "Xiaomi x3"],    # 0 # no o
                ["Acer", "Macbook", "Dell"],                  # 1
                ["Ipad","Samsung galaxy tab","Xiaomi tablet"],# 2
            ]

telefoni = ["Iphone 11", "Samsung s22", "Xiaomi x3"]
laptopovi = ["Acer", "Macbook", "Dell"]
tableti = ["Ipad","Samsung galaxy tab","Xiaomi tablet"]
# Skracena varijanta
#proizvodi = [telefoni, laptopovi, tableti]
# Uglaste zagrade - usamos para las listas y para la iteracion(Iteracija)

# for kategorija in proizvodi:
#     for i in kategorija:
#         print(i)
# for i in range(len(proizvodi)):
    # print(proizvodi[i])
    # for j in range(len(proizvodi[i])):
        # print(proizvodi[i][j])

hrana = [
            ["cokolada","bombone","palacinke"],
            ["sarma","musaka","kiseli kupus"],
            ["pecena paprika","ajvar","sopska"],
        ]

# for kategorija in hrana:
#     for jelo in kategorija:
#         print(jelo)

#formatiran string (f) ispred stringa
# ime = "Sofija"
# poruka = f"Cao {ime}!!!"
# print(poruka)
# -------------------------------------
# a = 10
# b = 15
# sabiranje = f"Sabiranje brojeva {a} i {b} je {a+b}"
# print(sabiranje)

biblioteka = []

while True:
    print("Odaberi komandu: 1-unos, 2-prikaz, 3-brisanje, > 4 izlaz")
    komanda = int(input("Unesite komandu: ")) 

    if komanda == 1:
        naslov = input("Unesite naslov: ")
        autor = input("Unesite autora: ")
        isbn = int(input("Unesite isbn: "))
        biblioteka.append([naslov, autor, isbn])
        print("Dodata knjiga")
    if komanda == 2:
        for knjiga in biblioteka:
            for detalj in knjiga:    
                print(detalj)
    if komanda == 3:
        klj_rec = input("Unesite naziv knjige koju zelite da obrisem: ")
        for knjiga in biblioteka:
            for detalj in knjiga:
                if detalj == klj_rec:
                    biblioteka.remove(knjiga)
                    print("Knjiga je obrisana.")
    if komanda == 4:
        break
#Tuples ()

