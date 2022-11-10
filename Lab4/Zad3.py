"""Zadanie 3. Utwórz pustą listę zwierzeta. Następnie
• Dodaj kilka nazw zwierząt do listy
• Posortuj listę
• Wyświetl pierwszy oraz trzy ostatnie elementy na liście
• Wyświetl informację o liczbie zwierząt na liście"""

zwierzeta=[]
x = 5

for i in range(x):
    a = input("Podaj nazwę zwierzęcia: ")
    zwierzeta.append(a)

zwierzeta.sort()
print(zwierzeta)
print(zwierzeta[0])
print(zwierzeta[2:])
print(len(zwierzeta))