"""Zadanie 2.
• Utwórz listę zestaw_1 zawierającą liczby losowe z przedziału [1, 10]. Liczbę elementów listy podaje
użytkownik. Wyświetl listę.
• Utwórz drugą listę zestaw_2 zawierającą liczby losowe z przedziału [5, 15]. Liczbę elementów listy
podaje użytkownik. Wyświetl listę.
• Pobierz od użytkownika liczbę. Napisz instrukcję warunkową, która na podstawie wartości
zapisanych w listach wyświetli jeden z poniższych komunikatów: „Liczba z zestawu 1”, „Liczba z
zestawu 2” albo „Nie ma takiej liczby w obu zestawach”.
• Utwórz listę zestaw_1_2 będącą złączeniem wartości z list zestaw_1 oraz zestaw_2. Posortuj i wyświetl
listę."""

zestaw_1 = []
import random
a = int(input("Podaj liczbę elementów listy: "))
for i in range(a):
    x = random.randint(1,10)
    zestaw_1.append(x)
print(zestaw_1)

b = int(input("Podaj liczbę elementów listy: "))
zestaw_2=[random.randint(5,15) for i in range(b)]
print(zestaw_2)

c = int(input("Podaj liczbę: "))
if c in zestaw_1:
    print("Liczba z zestawu 1")
elif c in zestaw_2:
    print("Liczba z zestawu 2")
else:
    print("Nie ma takiej liczby w obu zestawach")

zestaw_1_2=zestaw_1+zestaw_2
print(zestaw_1_2)
zestaw_1_2.sort()
print(zestaw_1_2)
