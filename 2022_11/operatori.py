import random
# kurs = "Python Fundamentals"
# print(kurs)

# a = 10
# b = 5
# print(a + b)

# rezultat_sabiranja = a + b
# print(rezultat_sabiranja)

# print("Oduzimanje:", a - b)
# print("Mnozenje:", a * b)
# print("Deljenje:", int(a / b)) # int para que sea numero entero.

# # // 
# # **
# # % 
# #Razmak = espacio | operand
# print("Celobrojno deljenje:", a // b)
# print(10 // 3)
# print(10 / 3) #precizniji
# # 10 / 3 = 3 
# # 3 * 3 = 0
# # 9 = 1 = 10
# #Celobrojni ostatak
# print(10 % 3)
# print(5 % 2)
# print(8 % 2)

# #Stepen
# print(a ** 2) # a * a
# print(a ** 3) # a * a * a
# print(- a)
# #

# godine = 25
# #godine + 1

# godine = godine + 1

# godine += 1 #Uvecaj i dodeli novu vrednost. 

# print(godine)

# godine -= 5
# print(godine)

# godine *= 2
# print(godine)

# godine /= 2 # |/=| = decimalna vrednos |//=| = int(cela vrednost)
# print(godine)

# broj1 = 15
# broj2 = 20

# print("Zbir:", broj1 + broj2)

# broj1 = input("Unesite prvi broj: ")
# print(broj1)

# broj2 = input("Unesite drugi broj: ")
# print(broj2)

# print("Rezultat je:", broj1 + broj2)

# r = float(input("Unesite poluprecnik: "))
# pi = 3.14

# pov = r ** 2 * pi
# print("Povrsina kruga je: ", pov)

# unos = input("Unesi nesto: ")
# print(unos.isnumeric())

#Operateri poredjenja
# < , > , <= , >= , == , !=

# stara_kilaza = 80
# nova_kilaza = 99
# print(stara_kilaza > nova_kilaza)
# print(stara_kilaza < nova_kilaza)

# print(nova_kilaza != 100)
# print(stara_kilaza <= 80)

# username = "test"
# password = "abc123"
# print(username == "test")
# print(password == "ABC123") #Python keysensitive

# godine = 20
# print(godine >= 16)

# #Vezba Da li je broj paran ili neparan
# broj = int(input("Unesite broj:"))
# provera = broj % 2 # Revisar en casa %
# print('Paran broj?', provera == 0)

#Vezba 7 ------------------------------------------------------------------------------------
# import random | preporuka je da se ukljuci na pocetku fajla da bi bio dostupan za ceo kod.
# moj_broj = random.randint(1,10)

# korisnik = int(input("Unesite broj od 1 do 10:"))
# racunar = random.randint(1,10)

# print("Korisnik:", korisnik)
# print("Racunar:", racunar)
# print("Pogodak:", korisnik == racunar)

# if korisnik == racunar:
#     print("Pogodili ste broj!")
# else:
#     print("Niste pogodili broj.")
#--------------------------------------------------------------------------------------------

# automobil = 0
# cilj = 50

# print(automobil >= cilj)
# automobil += 10
# print(automobil >= cilj)

# print(automobil >= cilj)
# automobil += 20
# print(automobil >= cilj)

# print(automobil >= cilj)
# automobil += 25
# print(automobil >= cilj)

#----------------------------------------------------------------------------------------------
#Logicki operatori
# #and operator - spaja
# provera_imena = True # ime == sacuvano_ime
# provera_sifra = False # sifra == sacuvana_sifra

# print(provera_imena or / and provera_sifra)

# # and(&) or(|) i not
# lepo_vreme = True
# print(not lepo_vreme)
#Pregledati kod kuce masinski jezik

# # is no lo tengo claro.
# x = [1, 2, 3]
# y = [1, 2, 3]
# print(x is y)

# python 2022 Vezba koriscenja and logickog operatora.
kurs = input("Unesite kurs:")
generacija = int(input("Unesite generaciju:"))

odobreno = kurs == "python" and generacija == 2022
print(odobreno)
