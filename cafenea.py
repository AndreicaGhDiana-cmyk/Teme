# 1 - Initializare
produse = ["espresso", "latte", "cappuccino", "ceai", "ciocolata calda", "croissant"]
preturi = [8.0, 12.0, 11.0, 7.0, 10.0, 9.0]
stoc = [20, 15, 18, 30, 12, 10]
cant_comanda = [0, 0, 0, 0, 0, 0]

reducere_curenta = 0.0
tip_reducere_curenta = "fara"


# 2 - Afisare meniu produse
def afisare_meniu(produse, preturi, stoc):
    print("\n========== MENIU PRODUSE ==========")
    for i in range(len(produse)):
        print(f"{i}. {produse[i]} - {preturi[i]:.2f} lei - stoc: {stoc[i]}")
    print("===================================")


# 3 - Adaugare produs in comanda
def adauga_produs_in_comanda(cant_comanda, stoc, index, cantitate):
    if index < 0 or index >= len(cant_comanda):
        print("Index invalid.")
        return False

    if cantitate <= 0:
        print("Cantitatea trebuie sa fie mai mare decat 0.")
        return False

    stoc_disponibil_real = stoc[index] - cant_comanda[index]

    if cantitate > stoc_disponibil_real:
        print("Stoc insuficient pentru produsul ales.")
        return False

    cant_comanda[index] += cantitate
    print("Produs adaugat in comanda.")
    return True


# 4 - Scadere/eliminare produs din comanda
def scade_produs_din_comanda(cant_comanda, index, cantitate):
    if index < 0 or index >= len(cant_comanda):
        print("Index invalid.")
        return False

    if cantitate <= 0:
        print("Cantitatea trebuie sa fie mai mare decat 0.")
        return False

    if cantitate > cant_comanda[index]:
        print("Nu poti scadea mai mult decat exista in comanda.")
        return False

    cant_comanda[index] -= cantitate
    print("Cantitatea a fost actualizata.")
    return True


# 5 - Calcul total
def calcul_total(cant_comanda, preturi):
    total = 0.0
    for i in range(len(cant_comanda)):
        total += cant_comanda[i] * preturi[i]
    return total


# 6 - Stabilire reducere
def stabilire_reducere(total, tip_reducere):
    reducere = 0.0

    if tip_reducere == "student":
        if total >= 30.0:
            reducere = 0.10 * total
        else:
            print("Total insuficient pentru student.")
            reducere = 0.0

    elif tip_reducere == "happy":
        if total >= 50.0:
            reducere = 0.15 * total
        else:
            print("Total insuficient pentru happy.")
            reducere = 0.0

    elif tip_reducere == "cupon":
        if total >= 25.0:
            reducere = 7.0
        else:
            print("Total insuficient pentru cupon.")
            reducere = 0.0

    elif tip_reducere == "fara":
        reducere = 0.0

    else:
        print("Tip de reducere invalid.")
        reducere = 0.0

    if reducere > total:
        reducere = total

    return reducere


# 7 - Afisare bon
def afisare_bon(produse, preturi, cant_comanda, reducere):
    total = calcul_total(cant_comanda, preturi)
    total_final = total - reducere

    print("\n============= BON =============")
    for i in range(len(produse)):
        if cant_comanda[i] > 0:
            subtotal = cant_comanda[i] * preturi[i]
            print(f"{produse[i]} x {cant_comanda[i]} = {subtotal:.2f} lei")

    print("--------------------------------")
    print(f"Total: {total:.2f} lei")
    print(f"Reducere: {reducere:.2f} lei")
    print(f"Total final: {total_final:.2f} lei")
    print("================================")


# 8 - Finalizare comanda
def finalizare_comanda(stoc, cant_comanda):
    for i in range(len(stoc)):
        stoc[i] -= cant_comanda[i]
        cant_comanda[i] = 0


# 9 - Anulare comanda
def anulare_comanda(cant_comanda):
    for i in range(len(cant_comanda)):
        cant_comanda[i] = 0


# 10 - Meniul principal
while True:
    print("\n========== MENIU PRINCIPAL ==========")
    print("1. Afisare meniu produse")
    print("2. Adaugare produs in comanda")
    print("3. Scadere/eliminare produs din comanda")
    print("4. Aplicare reducere")
    print("5. Finalizare comanda")
    print("6. Anulare comanda")
    print("0. Iesire")
    print("=====================================")

    optiune = input("Alege o optiune: ")

    if optiune == "1":
        afisare_meniu(produse, preturi, stoc)

    elif optiune == "2":
        try:
            index = int(input("Introdu indexul produsului: "))
            cantitate = int(input("Introdu cantitatea: "))
            adauga_produs_in_comanda(cant_comanda, stoc, index, cantitate)
        except ValueError:
            print("Date invalide. Introdu numere intregi.")

    elif optiune == "3":
        try:
            index = int(input("Introdu indexul produsului: "))
            cantitate = int(input("Introdu cantitatea de scazut: "))
            scade_produs_din_comanda(cant_comanda, index, cantitate)
        except ValueError:
            print("Date invalide. Introdu numere intregi.")

    elif optiune == "4":
        total_curent = calcul_total(cant_comanda, preturi)

        if total_curent == 0:
            print("Comanda este goala.")
        else:
            print("\n------ SUB-MENIU REDUCERI ------")
            print("1. student (10% daca total >= 30.00)")
            print("2. happy (15% daca total >= 50.00)")
            print("3. cupon (-7.00 lei daca total >= 25.00)")
            print("4. fara reducere")
            print("5. inapoi")
            print("--------------------------------")

            alegere_reducere = input("Alege reducerea: ")

            if alegere_reducere == "1":
                tip_reducere_curenta = "student"
                reducere_curenta = stabilire_reducere(total_curent, tip_reducere_curenta)
                print(f"Reducerea curenta este: {reducere_curenta:.2f} lei")

            elif alegere_reducere == "2":
                tip_reducere_curenta = "happy"
                reducere_curenta = stabilire_reducere(total_curent, tip_reducere_curenta)
                print(f"Reducerea curenta este: {reducere_curenta:.2f} lei")

            elif alegere_reducere == "3":
                tip_reducere_curenta = "cupon"
                reducere_curenta = stabilire_reducere(total_curent, tip_reducere_curenta)
                print(f"Reducerea curenta este: {reducere_curenta:.2f} lei")

            elif alegere_reducere == "4":
                tip_reducere_curenta = "fara"
                reducere_curenta = 0.0
                print("Reducerea a fost resetata la 0.")

            elif alegere_reducere == "5":
                print("Revenire la meniul principal fara schimbari.")

            else:
                print("Optiune invalida in sub-meniul de reduceri.")

    elif optiune == "5":
        total_curent = calcul_total(cant_comanda, preturi)

        if total_curent == 0:
            print("Nu exista produse in comanda.")
        else:
            reducere_efectiva = stabilire_reducere(total_curent, tip_reducere_curenta)
            afisare_bon(produse, preturi, cant_comanda, reducere_efectiva)
            finalizare_comanda(stoc, cant_comanda)

            reducere_curenta = 0.0
            tip_reducere_curenta = "fara"

            print("Comanda a fost finalizata. Stocul a fost actualizat.")

    elif optiune == "6":
        anulare_comanda(cant_comanda)
        reducere_curenta = 0.0
        tip_reducere_curenta = "fara"
        print("Comanda a fost anulata. Stocul nu a fost modificat.")

    elif optiune == "0":
        print("Program inchis.")
        break

    else:
        print("Optiune invalida.")