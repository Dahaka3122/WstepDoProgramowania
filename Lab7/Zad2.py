"""Zadanie 2.
• Utwórz losową macierz o wymiarach 5x5. Znajdź największy i najmniejszy element. (patrz tab4_2d;
metoda max(), min())
• Wypisz największe elementy w każdym z wierszy (axis = 1) i w każdej z kolumn (axis = 0).
• Policz sumę wartości w poszczególnych wierszach."""

import numpy as np

macierz = np.random.randint(low=0, high=11, size=(5,5))
print(macierz)
print(f'Maksymalna wartość: {np.max(macierz)}')
print(f'Minimalna wartość: {np.min(macierz)}')
print("Wartości minimalne w wierszach: ", macierz.min(axis = 1))
print("Wartości maksymalne w kolumnach: ", macierz.max(axis = 0))
print("Suma wartości w wierszach: ", macierz.sum(axis = 1))