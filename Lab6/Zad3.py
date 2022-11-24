"""Zadanie 3. Napisz funkcję o zmiennej liczbie parametrów, która wyświetla wartości parametrów na ekranie.
Następnie zmodyfikuj funkcję tak, aby znajdowała i zwracała wartość maksymalną."""

"""def funkcja(*args):
    print(type(args))
    print(args)
    for i in args:
        print(i)

funkcja(49,48.31,"String",[1,3,5])
funkcja()
funkcja(91,196)"""

def max(*args):
    if len(args) == 0:
        return None
    m = args[0]
    for i in args[1:]:
        if i > m:
            m = i
    return m

wynik = max(31,4,19,23)
print(wynik)
print(max())
print(max("Jola", "Maria", "Kilo", "Wieża"))