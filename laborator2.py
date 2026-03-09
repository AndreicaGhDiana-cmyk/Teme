glosar = {
  "variabila": {
    "definiție": "nume asociat unei valori",
    "categorie": "fundamente",
    "exemplu": "x = 10"
  },
  "dictionar": {
    "definiție": "structură de date bazată pe perechi cheie-valoare",
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


if __name__ == "__main__":
    while True:
        afisare_meniu()
        optiune = input("Alegeti o optiune: ")


        if optiune == "6":
            afisare_glosar()
        elif optiune == "1":
            adauga_termen()