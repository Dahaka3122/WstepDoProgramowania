"""Zadanie 5. Utwórz listę punkty będącą listą punktów zdobytych z pewnego egzaminu przez grupę 15 studentów.
Punkty niech będą liczbami rzeczywistymi z przedziału [0; 50]. Następnie
• Wyświetl informację o największej i najmniejszej ilości zdobytych punktów
• Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika. Jeżeli taka liczba
punktów nie występuje na liście, wyświetl odpowiedni komunikat
• Oblicz średnią liczbę punktów z egzaminu
• Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
• Wyświetl punkty poniżej średniej
• Wyświetl punkty powyżej średniej"""

import random
#punkty=[]
x = 15
"""for i in range(x):
    a = random.uniform(0,50)
    a = round(a,2)
    punkty.append(a)"""

punkty=[round(random.uniform(0,50),2) for i in range(x)]
print(punkty)
print(f"Maksymalna wartość: {max(punkty)}")
print(f"Minimalna wartość: {min(punkty)}")

a = float(input("Podaj liczbę: "))
if a in punkty:
    print(punkty.index(a))
else:
    print("Liczba nie występuje w liście")

suma = sum(punkty)
print(f"Zsumowana liczba punktów: {round(suma,2)}")
srednia = suma/15
print(f"Średnia liczba punktów: {round(srednia,2)}")
powyzej=[]
ponizej=[s for s in punkty if s<srednia]
for s in punkty:
    if s>srednia:
        powyzej.append(s)
print(f"Ponkty powyżej średniej: {powyzej}",len(powyzej))
print(f"Punkty poniżej średniej: {ponizej}",len(ponizej))

