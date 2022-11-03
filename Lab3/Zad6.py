"""Zadanie 6 (6.py): Zastosuj instrukcje continue w programie z zad. 5 tak, aby po podaniu liczby punktów spoza
przedziału 0 – 100 pomijać dalsze wykonywanie pętli. Sprawdź działanie programu. Następnie zmień pętlę na
nieskończoną, czyli taką której warunek zawsze jest prawdziwy. Zakończ działanie pętli przy użyciu instrukcji
break."""

n = int(input("Podaj liczbę studentów: "))
i = 1
suma = 0

while True:
    punkty = float(input(f"Podaj liczbę punktów dla studenta {i}: "))
    if punkty <= 0 or punkty >= 100:
        continue
    suma = suma + punkty
    i = i + 1
    if i>n:
        break

srednia = suma / n
print("Średnia punktów wynosi: ", srednia)