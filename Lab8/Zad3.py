"""Napisz funkcję potęga(), która podniesie wartości z pierwszej listy do potęg z drugiej listy. Sprawdź,
czy listy są tej samej długości. Parametrami funkcji są dwie listy. Funkcja ma zwracać listę z wynikami."""

def potęga(liczby, potęgi):
    i = 0
    lista3 = []
    if len(liczby) != len(potęgi):
        print("Listy są różne")
        return lista3
    for i in range(len(liczby)):
        x = liczby[i] ** potęgi[i]
        lista3.append(x)
    return lista3

y = potęga([1,2,3,4,5,6],[2,3,2,5,0])
print(y)