slownik = {"jeden": 1, "dwa": 2}
slownik["jeden"]
a = slownik["jeden"]

#  dodanie nowej wartosci
slownik["trzy"] = 3

# pobieram tylko klucze
slownik.keys()  

# pobieram tylko wartosci
slownik.values()  

# lista wartosci z obiektu slownika
list(slownik.values()) 

# zwracanie elementow slownika item slownika to para key value
print(slownik.items())

# dobranie się do jednego elemtnu
#teraz bedzie blad
# print(slownik.items()[0])

# po zrzutowaniu na liscie i bedzie ok:
print(list(slownik.items())[0])

#  typ zwracanej zmiennej:
print(type(list(slownik.items())[0]))

# slice - wyciaganie x elementow 
print(list(slownik.items())[0:2])
# [start:stop:step]
#  start - wlaczaja indeks start
# stop - z wylaczeniem indeksu stop 
print(list(slownik.items())[::2]) 

lista = [1, 2, 3, 4, 5]
print(lista)
print(lista[0:2])
print(lista[::2])

l = [1, 2, 3, 4, 5, 6]
pierwsza_polowa = l[:3]
druga_polowa = l[3:]

polowa = int(len(l)/2)
pierwsza_polowa = l[:polowa]
druga_polowa = l[polowa:]

print(pierwsza_polowa)
print(druga_polowa)


