"""Napisz funkcję find(), która w liście sprawdza czy występuje podana wartość. Lista i wartość są
parametrami funkcji. Funkcja ma zwracać listę indeksów, pod którymi wystąpiła wartość. Nie wolno korzystać z
operatora in w celu sprawdzenia czy wartość występuje w liście."""

def find(Lista, wartość):
    x = 0
    index = []
    for i in Lista:
        if i == wartość:
            index.append(x)
        x += 1
    return index
#            print("Wartość",wartość,"znajduje się w liście")
#        else:
#            print("Wartość",wartość,"nie znajduje się w liście")
I = find([1,92,8,13,54],5)
print(I)

