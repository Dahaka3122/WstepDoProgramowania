x = int(input('''Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie
Wpisz numer operacji: '''))
y = float(input("Podaj argument 1: "))
z = float(input("Podaj argument 2: "))

if x == 1:
    wynik = y + z
    exit()
elif x == 2:
    wynik = y - z
    exit()
elif x == 3:
    wynik = y * z
    exit()
elif x == 4:
    if y == 0 or z == 0:
        print("Nie można dzielić przez zero")
        exit()
    else:
        wynik = y / z
        exit()
elif x == 5:
    wynik = y ** z
    exit()
else:
    print("Niepoprawna operacja")
    exit()

print("Wynik operacji: ", wynik)
