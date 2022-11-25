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

primer = "zadatak1"

# for indeks in range(len(primer)):
#     print(primer[indeks], end=" ")

broj_karaktera = len(primer)
print(broj_karaktera)
indeks = 0
while indeks < broj_karaktera:
    print(primer[indeks]) 
    indeks += 1

# korisnicko_ime = "admin"
# # uneto_kor_ime = input("Unesi korisnicko ime: ").lower()

# if korisnicko_ime == uneto_kor_ime: # ili uneto_kor_ime.lower()
#        print("Dobrodosli!", uneto_kor_ime)
# else:
#        print("Pogresni podaci")


