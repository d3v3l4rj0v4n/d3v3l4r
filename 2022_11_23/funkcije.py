'''
ime = "Sofija"
len(ime) #Funkcija

ime.upper() #Metod
'''
#Metod je funkcija koja se navido tackom. Kad nema tacke onda je funkcija

#Metodi su objektno orijetisano u pajtonu.
#kljucna rec za definisanje funkcije je def(): (Tacke oznacavaju pocetak bloka koda uvek.)

def ispisi_poruke(): #Pravila imenovanja: da pocinje malim slovima, bez razmaka. Potpis/Deklaracija funkcije.
    #telo funkcije
    print("Zdravo")
    print("Danasnji datum je 29.12")
    print("Predavanje pajton")

# Poziv funkcije
ispisi_poruke()


def pozdravna_poruka(ime):
    print(f"Hello {ime}")

pozdravna_poruka("Sofija") #Ulazni parametar funkcija

def prikazi_informacije(ime, poeni=0):
    print(f"Student: {ime}, poeni: {poeni}")

prikazi_informacije("Juan", 80)
prikazi_informacije("Sofija")

def saberi(a = 0, b = 0):
 #   print(a, b)
   print(a + b)

#saberi(10, 20)

#saberi(int(input("Broj a:")), int(input("broj b:")))

#prvi sabirak, drugi, operacija
def kalkulator(a, b, o):
    if o == "+":
       print(a + b)
       return a + b
    elif o == "-":
        print(a - b)
        return a - b 
    elif o == "*":
        print(a * b)
        return a * b
    elif o == "/":
        if b == 0:
            print("Nije dozvoljeno deljenje sa nulom.")
            print("Proverite operaciju (+, -, *, /)")
        else:
            print(a / b)        

kalkulator(input("Unesite operaciju (+, -, *, /): "), int(input("Unesite prvi broj: ")), int(input("Unesite drugi broj: ")))

