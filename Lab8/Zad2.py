"""Napisz funkcję sum_of_values(), która policzy i zwróci sumę wartości (values) słownika:
dict1 = {'data1':10, 'data2':-4, 'data3':2}
Nie wolno korzystać z funkcji sum()."""

dict1 = {'data1':10, 'data2':-4, 'data3':2}
dict2 = {'śruba': 365, 'wiertarka': 190, 'stół': -256}
def sum_of_values(wartość):
    j = 0
    for i in wartość.values():
        j = j + i
    return(j)

suma = sum_of_values(dict1)
suma2 = sum_of_values(dict2)
print(suma, suma2)
