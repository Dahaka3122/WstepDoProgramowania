"""Zadanie 2.
• Wypisz wszystkie pary klucz:wartość występujące w słowniku:
sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
• Utwórz słownik, wybierając ze słownika sample_dict pary o kluczach zapisanych w liście.
Wskazówki:
− przejdź za pomocą pętli po kluczach zapisanych w liście;
− następnie sprawdź, czy dany klucz występuje w słowniku; jeśli występuje, dodaj go (parę
klucz:wartość) do nowego słownika.
• Usuń ze słownika wartości, których klucze występują w liście.
• Sprawdź, czy wartość „Jones” występuje w słowniku.
• Zmień w słowniku klucz ‘city’ na ‘location’"""

sample_dict = {"name": "Kelly",
               "surname": "Jones",
               "age": 25,
               "salary": 8000,
               "city": "New York"}

"""for k in sample_dict.keys():
    print(k,sample_dict[k])"""

for k, v in sample_dict.items():
    print(f'{k:<8} = {v:>8}')

#sample_dict2={}
list = ["name","age","city","a"]
#for k in list:
#    if k in sample_dict.keys():
#        sample_dict2[k]=sample_dict[k]

sample_dict2 = {k:sample_dict[k] for k in list if k in sample_dict.keys()}
print(sample_dict2)

sample_dict3 = sample_dict.copy()
for i in list:
    if i in sample_dict3:
        sample_dict3.pop(i)
print(sample_dict3)

if "Jones" in sample_dict.values():
    print("Wartość występuje")
else:
    print("Wartość niewystępuje")

sample_dict["location"] = sample_dict["city"]
del sample_dict["city"]
print(sample_dict)