﻿while True:
    try:
        vanus=float(input("Pikkus: "))
        if vanus>0: break
    except:
        print("On vaja numbreid kirjutada, mis on suurem kui 0")
while True:
    try:
        l=float(input("Laius: "))
        if l>0: break
    except:
        print("On vaja numbreid kirjutada, mis on suuream kui 0")
while True:
    try:
        l=float(input("Laius: "))
        if l>0: break 
    except: 
        print("On vaja numbreid kirjutada, mis on suurem kui 0")
while True:
    v=input("Kas tahad remonti teha? ")
    if v.upper()=="JAH":
        while True:
            try:
            hind=float(input("Kui palju maksam m^2"))
            break
    except: TypeError:
        print()
    hind=l*p*hind
    print(f"Remonti hind on {hind}")
else:
    pass
        
###

while True:
    nimi1=input("1. Mis on sinu nimi? ")
    if nimi1.isalpha(): break
while True:
    nimi2=input("2. Mis on sinu nimi? ")
    if nimi2.isalpha(): break
if nimi1=="Anna" and nimi2=="Inna": print("Neid on täna pinginaabrid")



###
while True:
    nimi=input("Mis on sinu nimi? ")
    if nimi.isalpha(): break
if nimi.upper()=="JUKU":
    while True:
        try:
            vanus=int(input("Kui vana sa oled?"))
            break
        except:
            print("On vaja arvude tüüp kasutada")
    if 0<vanus<6:
        print("Tasuta")
    elif 6<=vanus<=14:
        print("Lastepilet")
    elif 15<=vanus<=65:
        print("Täispilet")
    elif 65<=vanus<=100:
        print("Sooduspilet")
    else:
        print("Vanus ei soobi")
else:
    print("Ma otsin Juku!")
###