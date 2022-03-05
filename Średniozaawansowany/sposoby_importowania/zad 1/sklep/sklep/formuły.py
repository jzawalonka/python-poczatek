from sklep.sklep.magazyn import dostepne_produkty


def sprawdz_czy_jest(nazwa):
    while True:
        for i in range(0, 3):
            if nazwa == (dostepne_produkty[i]["nazwa"]):
                return nazwa, i
        nazwa = input("Tego towaru nie ma w sklepie, padaj inny: ")


def nowe_zamowienie():
    nazwa = input("podaj nazwę: ")
    nazwa, i = sprawdz_czy_jest(nazwa)
    ilosc = input(f"Ile {nazwa} chcesz kupić? ")
    ilosc = sprawdz_dostepnosc(ilosc, i)
    cena = (dostepne_produkty[i]["wlasciwosci"]["cena_za_sztuke"])
    return nazwa, ilosc, cena


def sprawdz_dostepnosc(ilosc, i):
    ilosc_w_magazynie = int(dostepne_produkty[i]["wlasciwosci"]["ilosc_dostepnych"])
    ilosc = int(ilosc)
    while ilosc > ilosc_w_magazynie:
        nowa_ilosc = input(f"W magazynie jest jedynie {ilosc_w_magazynie} sztuk, wprowadz ponownie: ")
        ilosc = int(nowa_ilosc)
    return ilosc
