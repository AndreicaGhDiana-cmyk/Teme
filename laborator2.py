glosar = {
  "variabila": {
    "definitie": "nume asociat unei valori",
    "categorie": "fundamente",
    "exemplu": "x = 10"
  },
  "dictionar": {
    "definitie": "structură de date bazată pe perechi cheie-valoare",
    "categorie": "structuri de date",
    "exemplu": "{'a': 1, 'b': 2}"
  }
}

def afisare_meniu():
    print("----MENIU GLOSAR----")
    print("Optiuni:")
    print("1. Adauga termen")
    print("2. Cautare exacta termen")
    print("3. Cautare partiala termeni")
    print("4. Actualizare termen")
    print("5. Stergere termen")
    print("6. Afisare glosar")
    print("7. STATISTICI")
    print("8. Salvare")
    print("9. Incarcare")
    print("0. Iesire")

def afisare_glosar():
    print("----GLOSAR----")
    print(list(glosar.keys()))

def adauga_termen():
    termen = input("Introduceti termenul: ")
    definitie = input("Introduceti definitia: ")
    categorie = input("Introduceti categoria: ")
    exemplu = input("Introduceti exemplu: ")
    if termen in glosar:
        print("Termenul exista deja")
        return
    glosar[termen] = {
        "definitie": definitie,
        "categorie": categorie,
        "exemplu": exemplu
    }

def actualizare_termen():
    termen = input("Alegeti termenul: ")
    if termen in glosar:
        definitie = input("Introduceti definitia noua: ")
        categorie = input("Introduceti categoria noua: ")
        exemplu = input("Introduceti exemplul nou: ")
    else:
        print("Termenul nu exista")

    if termen in glosar:
        glosar[termen]["exemplu"] = exemplu
        glosar[termen]["categorie"] = categorie
        glosar[termen]["definitie"] = definitie

def stergere_termen():
    termen = input("Introduceti termenul de sters: ")
    if termen in glosar:
        del glosar[termen]
    else:
        print("Termenul nu este in glosar")

def cautare_exacta():
    termen = input("Introduceti termenul cautat: ")
    if termen in glosar:
        for a,b in glosar[termen].items():
            print(f"{a}: {b}")
    else:
        print("Termenul nu este in glosar")

def cautare_partiala():
    fragment = input("Introduceti fragmentul cautat: ")
    rezultat = [termen for termen, info in glosar.items() if any (fragment in str(val) for val in info.values())]
    if rezultat:
        print(rezultat)
    else:
        print("Fragmentul nu apartine unui termen")

def statistici():
    general = len(glosar)
    print(f"Glosarul contine in total {general} termeni")
    from collections import Counter
    categorii = [info["categorie"] for info in glosar.values()]
    dupa_categorii = Counter(categorii)
    print(f"sortati dupa categorii: {dict(dupa_categorii)}")

import csv
def salveaza_glosar(glosar, nume_fisier="glosar.csv"):
    campuri = ["termen", "definitie", "categorie", "exemplu"]

    with open(nume_fisier, mode="w", newline="", encoding="utf-8") as fisier:
        writer = csv.DictWriter(fisier, fieldnames=campuri)
        writer.writeheader()

        for termen, info in glosar.items():
            rand = {"termen": termen, **info}
            writer.writerow(rand)

    print(f"Glosarul a fost salvat în {nume_fisier}")


def incarca_glosar(nume_fisier="glosar.csv"):
    glosar_nou = {}
    try:
        with open(nume_fisier, mode="r", encoding="utf-8") as fisier:
            reader = csv.DictReader(fisier)
            for rand in reader:
                termen = rand.pop("termen")
                glosar_nou[termen] = rand
        print("Glosarul a fost incarcat")
        return glosar_nou
    except FileNotFoundError:
        print("Fișierul nu a fost găsit - se returnează un glosar gol")
        return {}

if __name__ == "__main__":
    while True:
        afisare_meniu()
        optiune = input("Alegeti o optiune: ")


        if optiune == "6":
            afisare_glosar()
        elif optiune == "1":
            adauga_termen()
        elif optiune == "4":
            actualizare_termen()
        elif optiune == "5":
            stergere_termen()
        elif optiune == "2":
            cautare_exacta()
        elif optiune == "3":
            cautare_partiala()
        elif optiune == "7":
            statistici()
        elif optiune == "8":
            salveaza_glosar(glosar)
        elif optiune == "9":
            glosar = incarca_glosar()
        elif optiune == "0":
            break


