"""Zadanie 1 (1.py):
• Dla osób poniżej 4 roku życia wstęp jest bezpłatny.
• Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.
• Dla osób powyżej 18 roku życia bilet kosztuje 20zł.
Przykład: Wprowadź wiek klienta: 5
Cena biletu: 10zł"""

"""#wiek
w = int(input("Wprowadź wiek:"))

if w < 4: print("Wstęp bezpłatny")
elif w <= 18: print("Bilet kosztuje: 10zł")
else: print("Bilet kosztuje 20zł")"""

x = int(input("Podaj wiek: "))
if x < 4:
    cena = 0
elif x <= 18:
    cena = 10
else:
    cena = 20

print(f"Cena biletu: {cena}zł")


