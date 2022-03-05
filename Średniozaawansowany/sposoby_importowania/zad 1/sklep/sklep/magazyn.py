dostepne_produkty = [
    {
        "nazwa": "mleko",
        "wlasciwosci":
            {
                "ilosc_dostepnych": 200,
                "cena_za_sztuke": 20
            },
    },
    {
        "nazwa": "jajka",
        "wlasciwosci":
            {
                "ilosc_dostepnych": 300,
                "cena_za_sztuke": 30
            },
    },
    {
        "nazwa": "bulki",
        "wlasciwosci":
            {
                "ilosc_dostepnych": 100,
                "cena_za_sztuke": 10
            },
    },
]


def aktualizacja_magazynu(nazwa_produktu, zamowiona_ilosc):
    dostepne_produkty[nazwa_produktu]["ilosc"] -= zamowiona_ilosc
