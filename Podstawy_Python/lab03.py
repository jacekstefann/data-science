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

# wywolanie metody na instancji
'Marianna'.lower()

# wywolanie metody na klasie
# str.lower()

d = 'Marianna'
'Marianna'.lower()
str.lower(d)


#  KROTKA
# zbior wartosci
# definicja krotki
krotka = (1, 2, 3, 'jacek', 'ma')
# wybranie elementu
krotka[0]
# przypisanie wartosci
# krotka[0]=3
# zmieniam krotka na liste
lista_z_krotki = list(krotka)
# zmienaim liste na krotke
krotka = tuple(lista_z_krotki)

# pokazanie w ktorej komorce pamieci jest krotka/obiekt 
enumerate(krotka)
# zwraca wartosc i indeks 
print(list(enumerate(krotka))[0])

for litera in enumerate("Ala"):
    print(litera)

# enumerate zwraca krotke indeks i wartosc elementu
# enumerate pozwala okreslic od ktorego miejsca ma zaczac indeksowac

for litera in enumerate("Ala", start=1):
    print(litera)

# pakowanie krotki
# rozpakowywanie do zmiennych

# pakowanie krotki
t = 5, 6, 7
print(t)

x, y, z = t
print(t)

for zmienna, wartosc in enumerate("Ala", start=1):
    print('Element o id {} = {}'.format(zmienna, wartosc))

# pakowania krotki jednoelementowej
t = 5, 6, 7
print(t)

# rozpakowywanie krotki
x, y, z = t
print(t)
*x, y = krotka
print(x, y)

*x, = krotka
print(x)

x, *y = krotka
print(x, y)

# tutaj otrzymamy krotke 2 elementowa
krot = lista('Ala'),
# tuaj dostaniemy krotke 3 elementowa - elementy zostaną rozpakowane jako osobne
# elementy krotki czyli beda 2 liczy i 1 lista 1 elementowa
krot = tuple([1,2 [3]])

