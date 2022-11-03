"""Zadanie 7 (7.py) Za pomocą pętli for wypisz na ekranie ciągi liczb:
• 1, 2, 3, ... , 99, 100
• 100, 99, ... , 2, 1, 0
• 7, 14, 21, ... , 70, 77
• 20, 18, ... , 2, 0
"""

i = int

for i in range(1,101):
    print(i, end=" ")

print()

for i in range(101,-1,-1):
    print(i, end=" ")

print()

for i in range(7,78,7):
    print(i, end=" ")

print()

for i in range(20,-1,-2):
    print(i, end=" ")

print()