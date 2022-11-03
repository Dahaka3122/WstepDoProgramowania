"""Zadanie 8 (8.py) Napisz skrypt, który wyświetli gwiazdki jak poniżej. Liczba wierszy (lub gwiazdek w linii)
powinna być podawana przez użytkownika.
Przykład: 3
* * *
* * *
* * *"""

x = int(input("Liczba wierszy: "))
b = int(input("Liczba gwiazdek w linii: "))

y = "*"

for a in range(x):
    for z in range(b):
        print(y, end=" ")
    print(" ")
