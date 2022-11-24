"""Zadanie 4. Napisz funkcję o zmiennej liczbie parametrów nazwanych, która wyświetla ich wartości na ekranie.
Jeśli wśród przekazanych argumentów jest argument end, to oddzielaj wyświetlane wartości przypisaną do end
wartością. W przeciwnym przypadku przypisz do end znak końca stringu.
Wskazówka: użyj parametru ** kwargs, który łączy wszystkie dodatkowe nazwane argumenty, określone
podczas wywoływania funkcji, w słownik. Argument przekazany przez słowo kluczowe jest uważany za
nadmiarowy, jeśli słowo kluczowe, przez które zostało przekazane, nie pasuje do żadnej z nazw
parametrów w definicji funkcji."""

def f1(**kwargs):
    if 'end' in kwargs:
        endF1 = kwargs['end']
    else:
        endF1 = "\n"
    for key, value in kwargs.items():
        print(key,value,end=endF1)
f1(par1=1, par2=2, par3=3, par4=4, par5=5, end=" ")