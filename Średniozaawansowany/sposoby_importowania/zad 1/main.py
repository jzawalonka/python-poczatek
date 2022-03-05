from sklep.sklep.formuły import nowe_zamowienie

print("Witaj w sklepie")
nazwa = 0
suma = 0
while nazwa != "x":
    nazwa, ilosc, cena = nowe_zamowienie()
    suma += cena * ilosc
    nazwa = input("Wcisnij dowolny przycisk aby kontynuować, lub 'x' aby zakończyć: ")
print(suma)
