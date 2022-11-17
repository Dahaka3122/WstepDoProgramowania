"""Zadanie 1.
• Utwórz listę values zawierającą liczby 10, 20, 30. Utwórz drugą listę keys zawierającą nazwy tych liczb w
języku angielskim (lub polskim). Dokonaj konwersji tych list w słownik.
Wskazówki:
− użyj funkcji zip(), która pobiera dwie sekwencje (takie jak list, dict, str), łączy je w krotki (pary) i
zwraca;
− lub wykonaj iterację listy za pomocą pętli for i funkcji range(). W każdej iteracji dodaj nową parę kluczwartość do słownika.
• Utwórz drugi słownik metodą słów kluczowych ( dict(klucz1=wartość1, klucz2=wartość2)), gdzie kluczem
będą nazwy liczb 30, 40, 50, a wartościami – liczby 30, 40, 50.
• Połącz dwa słowniki w jeden nowy słownik.
"""

values = [10,20,33]
keys = ["ten","twenty","thirty"]
slownik = dict(zip(keys,values))
print(slownik)

"""x=len(keys)
for i in range(x):
    slownik[keys[i]]=values[i]
print(slownik)"""

slownik2 = dict(thirty=30,forty=40,fifty=50)
slownik3 = slownik.copy()
slownik3.update(slownik2)
print(slownik3)


