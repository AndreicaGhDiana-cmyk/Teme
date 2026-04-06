import csv
import json
import os


def citeste_produse_csv(fisier):
    produse = {}
    try:
        with open(fisier, mode='r', encoding='utf-8') as f:
            cititor = csv.DictReader(f)
            for rand in cititor:
                id_p = rand['id'].strip()
                produse[id_p] = {
                    "nume": rand['nume'].strip(),
                    "pret": float(rand['pret']),
                    "stoc": int(rand['stoc'])
                }
        return produse
    except FileNotFoundError:
        print(f"Eroare: Nu s-a gasit {fisier}")
        return {}

def citeste_reduceri_json(fisier):
    try:
        with open(fisier, mode='r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Eroare: Nu s-a gasit {fisier}")
        return {}


def adauga_produs(comanda, produse, id_p, cantitate):
    if id_p not in produse:
        print("ID inexistent!")
        return False

    stoc_disponibil = produse[id_p]['stoc']
    deja_in_comanda = comanda.get(id_p, 0)

    if cantitate + deja_in_comanda > stoc_disponibil:
        print(f"Stoc insuficient! Mai sunt doar {stoc_disponibil - deja_in_comanda} bucati")
        return False

    comanda[id_p] = deja_in_comanda + cantitate
    print(f"Adaugat: {produse[id_p]['nume']} x {cantitate}")
    return True


def scade_produs(comanda, id_p, cantitate):
    if cantitate <= 0:
        print("Cantitatea nu poate fi negativa")
        return False
    if id_p in comanda:
        if cantitate >= comanda[id_p]:
            del comanda[id_p]
            print("Produsul a fost eliminat  din comandă ")
        else:
            comanda[id_p] -= cantitate
            print("Comanda actualizata.")
        return True
    else:
        print("Acest produs nu se află în comanda")
        return False


def calculeaza_total(comanda, produse):
    total = 0.0
    for id_p, cantitate in comanda.items():
        total += produse[id_p]['pret'] * cantitate
    return total


def calculeaza_reducere(total, tip_reducere, reduceri_config):
    if tip_reducere not in reduceri_config:
        return 0.0

    regula = reduceri_config[tip_reducere]
    if total >= regula['prag']:
        if regula['tip'] == "procent":
            return total * (regula['valoare'] / 100)
        else:
            return float(regula['valoare'])
    return 0.0


def genereaza_bon(comanda, produse, total, reducere):
    bon = "\n" + "=" * 20 + "\n  CAFENEAUA MEA\n" + "=" * 20 + "\n"
    for id_p, cantitate in comanda.items():
        p = produse[id_p]
        bon += f"{p['nume']} x {cantitate} = {p['pret'] * cantitate:.2f} lei\n"

    bon += "-" * 20 + f"\nTotal: {total:.2f} lei\n"
    bon += f"Reducere: {reducere:.2f} lei\n"
    bon += f"TOTAL FINAL: {total - reducere:.2f} lei\n"
    bon += "=" * 20 + "\n"
    return bon


def scrie_bon_txt(fisier, text_bon):
    with open(fisier, mode='w', encoding='utf-8') as f:
        f.write(text_bon)


def goleste_comanda(comanda):
    comanda.clear()


def main():
    produse = citeste_produse_csv('produse.csv')
    reduceri = citeste_reduceri_json('reduceri.json')
    comanda = {}
    reducere_curenta_nume = "fara"

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

        opt = input("Alege o optiune: ")
        if opt == "1":
            for i, info in produse.items():
                print(f"ID {i}: {info['nume']} - {info['pret']} lei (Stoc: {info['stoc']})")

        elif opt == "2":
            id_p = input("ID produs: ")
            try:
                cant = int(input("Cantitate: "))
                adauga_produs(comanda, produse, id_p, cant)
            except ValueError:
                print("Introdu un numar!")


        elif opt == "3":
            print("Produse în comanda curentă:")
            for id_p, cant in comanda.items():
                nume = produse[id_p]['nume']
                print(f"ID {id_p}: {nume} (Cantitate: {cant})")
            id_scade = input("Introdu ID-ul produsului de scăzut: ")
            try:
                cant_scade = int(input("Introdu cantitatea de scăzut: "))
                scade_produs(comanda, id_scade, cant_scade)
            except ValueError:
                print("Eroare: Introdu un număr întreg")

        elif opt == "4":
            print(f"Reduceri disponibile: {list(reduceri.keys())}")
            reducere_curenta_nume = input("Alege reducerea: ")

        elif opt == "5":
            total = calculeaza_total(comanda, produse)
            reducere_val = calculeaza_reducere(total, reducere_curenta_nume, reduceri)
            text_bon = genereaza_bon(comanda, produse, total, reducere_val)

            print(text_bon)
            scrie_bon_txt("bon_final.txt", text_bon)

            # Actualizare stoc in dictionar dupa finalizare
            for id_p, cant in comanda.items():
                produse[id_p]['stoc'] -= cant

            goleste_comanda(comanda)
            print("Bon salvat in 'bon_final.txt'. Comanda finalizata.")

        elif opt == "0":
            break

if __name__ == "__main__":
    main()
