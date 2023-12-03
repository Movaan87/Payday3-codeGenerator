import os
nappaimet = ["0","1","2","3","4","5","6","7","8","9"]
vaihtoehdot = []

for i in range(len(nappaimet)):
    for j in range(len(nappaimet)):
        for k in range(len(nappaimet)):
            for l in range(len(nappaimet)):
                if not (i == j and i == k and i == l and j == k and j == l and k == l):
                    vaihtoehdot.append((f"{i}", f"{j}", f"{k}", f"{l}"))

while True:
    maara = 0
    numerot = []
    koodit = []
    for i in range(4):
        numero = input(f"Anna {i + 1}. numero: ")
        if numero == "":
            break
        numerot.append(numero)


    for vaihtoehto in vaihtoehdot:
        kelpaa = True
        for digit in vaihtoehto:
            if not digit in numerot:
                kelpaa = False
                break
        for numero in numerot:
            if not numero in vaihtoehto:
                kelpaa = False
                break
        if kelpaa:
            koodit.append(vaihtoehto)

    for koodi in koodit:
        print(' '.join(koodi))
        maara += 1

    print(f"Mahdollisia koodeja yhteensä {maara}kpl")

    if input("Haluatko jatkaa? (Y/N): ").lower() == "n":
        break
    
    os.system("cls")