produse = ["espresso", "latte", "cappuccino", "ceai", "ciocolata calda", "croissant"]
preturi = [8.0, 12.0, 11.0, 7.0, 10.0, 9.0]
stoc = [20, 15, 18, 30, 12, 10]
cant_comanda = [0, 0, 0, 0, 0, 0]

reducere_curenta = 0.0

def afisare_meniu(produse , preturi , stoc):
    print("\n MENIU PRODUSE")
    for i in range(len(produse)):
        print(f"{i}. {produse[i]} - {preturi[i]} lei - {stoc[i]} buc")

def adaugare_produse(cant_comanda , stoc , index , cantitate):
    if 0 <= index < len(produse):
        if cantitate > 0:
            stoc_disponibil = stoc[index] - cant_comanda[index]
            if cantitate <= stoc_disponibil:
                cant_comanda[index] += cantitate
                print(f"Am adaugat {cantitate} {produse[index]}")
            else:
                print(f"Stoc insuficient. Disponibil {stoc_disponibil} buc")
        else:
            print(f"Cantitatea trebuie sa fie mai mare decat 0")
    else:
        print("Index invalid")

def eliminare_produs(cant_comanda  , index , cantitate):
    if 0 <= index < len(cant_comanda):

        if cantitate > 0:
            if cantitatea <= cant_comanda[index]:
                cant_comanda[index] -= cantitate
                print(f"Am eliminat {cantitate} {produse[index]}")
            else:
                print("Cantitate prea mare de eliminat")
        else:
            print("Cantitatea trebuie sa fie mare decat 0")
    else:
        print("Index invalid")

def calcul_total(cant_comanda , preturi):
    total = 0.00
    for i in range(len(cant_comanda)):
        total += cant_comanda[i] * preturi[i]
    return total


def calcul_reducere(total, tip_reducere):
    reducere  = 0.0
    if tip_reducere == "1":
        if total >= 30.00 :
            reducere = 0.10 * total
        else:
            print("Total insuficient pentru student")
    elif tip_reducere == "2":
        if total >= 50.00 :
            reducere = 0.15 * total
        else:
            print("Total insuficient pentru happy")
    elif tip_reducere == "3":
        if total >= 25.00 :
            reducere = 7.00
        else:
            print("Total insuficient pentru cupon")
    if reducere > total:
        reducere  = total
    return reducere

def afisare_bon(produse , cant_comanda , preturi, reducere):
    total_neredus = calcul_total(cant_comanda , preturi)
    print("\n BON FISCAL")
    for i in range  (len(produse)):
        if cant_comanda[i]>0:
            subtotal = cant_comanda[i] * preturi[i]
            print (f"{produse[i]} x {cant_comanda[i]} = {subtotal:.2f} lei ")
    print(f"Subtotal: {total_neredus:.2f} lei ")
    print(f"Reducere: {reducere:.2f} lei ")
    print(f"TOTAL: {total_neredus - reducere:.2f} lei ")



while True:
    print("\nMENU PRINCIPAL:")
    print("1. Afisare meniu produse")
    print("2. Adaugare produs in comanda")
    print("3. Scadere/eliminare produs")
    print("4. Aplicare reducere")
    print("5. Finalizare comanda")
    print("6. Anulare comanda")
    print("0. Iesire")
    choice = input("\nAlegeti o optiune: ")
    if choice == "1":
        afisare_meniu(produse , preturi , stoc)
    elif choice == "2":
        idx = int(input("Index produs: "))
        cant = int(input("Cantitate produs: "))
        adaugare_produse(cant , stoc , idx , cant)
    elif choice == "3":
        idx= int(input("Index produs: "))
        cant = int(input("Cantitate de scazut: "))
        eliminare_produs(cant , idx, cant )
    elif choice == "4":
        total_actual = calcul_total(cant_comanda , preturi)
        if total_actual == 0:
            print("Comanda este goala")
            reducere_curenta = 0.0
        else:
            print("\nSUB-MENIU REDUCERI:")
            print("1. student (10% la total >= 30.00)")
            print("2. happy (15% la total >= 50.00)")
            print("3. cupon (-7.00 lei la total >= 25.00)")
            print("4. fara reducere")
            print("5. inapoi")
            sub_opt = input("Alegeti: ")
            if sub_opt in ["1", "2", "3"]:
                reducere_curenta = stabilire_reducere(total_actual, sub_opt)
            elif sub_opt == "4":
                reducere_curenta = 0.0
                print("Reducerea setata la 0.")
    elif choice == "5":
        total_finalizare = calcul_total(cant_comanda , preturi)
        if total_finalizare == 0:
            print("Nu exista produse in comanda")
        else:
            afisare_bon(produse, cant_comanda, preturi, reducere_curenta)

            for i in range(len(produse)):
                stoc[i] -=cant_comanda[i]
                cant_comanda[i] == 0
            reducere_curenta== 0.0
            print("Comanda a fost finalizata")
    elif choice == "6":
        for i in range(len(cant_comanda)):
            cant_comanda[i]== 0
        reducere_curenta = 0.0
        print("Comanda a fost anulata")
    elif choice == "0":
        print("La revedere!")
        breakc
    else:
        print("Optiune invalida1")



