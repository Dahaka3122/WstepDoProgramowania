#Zadanie 2 (2.py) Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała.

litera = input("Wprowadź literę: ")

if len(litera) > 1 or len(litera) == 0:
    print("Nieprawidłowe dane")
    exit()
if 'a' <= litera <= 'z':
    print("Litera jest mała")
elif 'A' <= litera <= 'Z':
    print("Litera jest duża")
else:
    print("To nie jest litera")