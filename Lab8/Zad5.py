"""Napisz program działający jak prosty kalkulator. W tym celu utwórz funkcje dodawanie(),
odejmowanie(), mnożenie() oraz dzielenie(). Następnie utwórz słownik, którego kluczem jest działanie, a
wartością – nazwa odpowiedniej funkcji.
Uwaga: funkcja jest obiektem, a nazwa funkcji – nazwą (referencją) tego obiektu"""

def dodawanie(a,b):
    suma = a + b
    return suma

def odejmowanie(a,b):
    odejmowanie = a - b
    return odejmowanie

def mnożenie(a,b):
    mnożenie = a * b
    return mnożenie

def dzielenie(a,b):
    if a == 0 or b == 0:
        return print("Nie dzieli się przez zero")
    else:
        return a / b

dict1 = {'+': dodawanie, "-": odejmowanie, '*': mnożenie, '/': dzielenie}

x = int(input("Podaj liczbę: "))
y = input("Podaj działanie: ")
z = int(input("Podaj drugą liczbę: "))

p = dict1[y](x,z)
print(p)

