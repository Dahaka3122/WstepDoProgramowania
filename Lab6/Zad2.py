"""Zadanie 2. Napisz funkcje oblicz(), która ma dwa parametry i oblicza ich sumę oraz różnicę. Ponadto zwraca
jednocześnie jak wynik dodawania, tak i odejmowania."""

def oblicz(x,y):
    suma = x + y
    różnica = x - y
    return suma,różnica

a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")

wynik = oblicz(12.39,19.34)
print(wynik[0],wynik[1])
