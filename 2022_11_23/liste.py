# osoba = ["Sofija", 25, "plava", False]
# for indeks in range(len(osoba)):
#     print(osoba[indeks])

# for osobina in osoba:
#     print(osobina)

# voce_i_povrce = ["jabuka","beli luk", "crni luk", "banana","mandarina", "krastavac"]
# 1. varijanta
# for stavka in voce_i_povrce:
#     print(stavka)
# 2. varijanta
# for i in range(len(voce_i_povrce)):
#     print("Na indeksu:", i, "nalazi se", voce_i_povrce[i])
# 3. varijanta
# for indeks, vrednost in enumerate(voce_i_povrce):
#     print("Indeks:", indeks, "Stavka:", vrednost) #Stavka = articulo
# import time
# #Primer
# automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo", "Opel", "Opel", "Ferrari"]

# for p_auto, v_auto in enumerate(automobili):
#     if len(v_auto) == 3:
#         print(v_auto)
#     # print("Pozicija:", p_auto, "Auto:", v_auto)

# automobili.append("Mercedes")
# automobili[2] = "Opel Corsa"
# print(automobili[7])
# print(automobili[2])
# automobili[3] = "Kia Sportage"
# print(automobili[3])

# # Uklanjanje clanova liste
# # 1. varijanta
# del automobili[3]
# print(automobili)
# time.sleep(1)
# # 2. varijanta
# automobili.pop(7)
# print(automobili)
# time.sleep(1)
# # 3. varijanta
# automobili.remove("Opel Corsa")
# print(automobili)

# broj_opela = 0
# for indeks in range(len(automobili)):
#     if automobili[indeks] == "Opel":
#         print("Evo ga Opel")
#         broj_opela += 1
# print("Imam ", broj_opela, "na placu.")

# prazan_plac = [] #Uglaste zagrade

# automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo", "Peugeot", "Audi",] #Slice-ovi

# automobili_akcija = []

# for i in range(len(automobili)):
#     if i == 1 or i == 2 or i == 3:
#         automobili_akcija.append(automobili[i])
# print(automobili_akcija)

# automobili_akcija = automobili[1:4]
# print(automobili_akcija)

brojevi = [3,2,4,5,6,7,8]
parni = []
neparni = []
for i in brojevi:
    parni.append(i) if i % 2 == 0 else neparni.append(i)
    # if i % 2 == 0:
    #     parni.append(i)             #append zahteva podatak koji cemo ubaciti u listu odnosno indeks.
    # else:
    #     neparni.append(i)

print("Parni brojevi liste su: ", parni)
print("Neparni brojevi liste su: ", neparni)

# Revisar en casa el operador ternario (Ternary operator)









