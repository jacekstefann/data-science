# **Zadania**

# **Zadanie 1**  
# Stwórz listę z wartościami od 1 do 10. Następnie podziel listę tak, aby pierwsze 5 liczb zostało w oryginalnej liście a pozostałe 5 znalazło się w nowej liście.

# **Zadanie 2**  
# Połącz te listy ponownie. Dodaj do listy wartość „0” na początku. Utwórz kopię połączonej listy i wyświetl listę posortowaną malejąco.

# **Zadanie 3**  
# Za pomocą rzutowania stringa na listę zapisz do listy swoje imię i nazwisko małymi literami jako podlisty (czyli otrzymamy listę dwupoziomową). 
# Następnie zamień pierwsze litery imienia i nazwiska na wielkie litery. W ostatnim kroku korzystając z metody .join() 
# dla klasy string scal obie listy ponownie w imię i nazwisko i wyświetl w odwróconej kolejności korzystając z mechanizmu cięcia (slice).

# **Zadanie 4**  
# Napisz skrypt, gdzie w jednej zmiennej zapiszesz dowolnie długie zdanie (co najmniej 5 wyrazów) a następnie podziel 
# te zdanie na wyrazy tak by zostały zapisane w liście jako jej elementy.


# zad 1

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[5:]
del a[5:]

# zad 2
a.extend(b)
a.insert(0, 0)
c = a[::1]

# zad 3
imie = 'Jacek'
nazwisko = 'Stefan'
lista1 = list(imie)
lista2 = list(nazwisko)

final = lista1 , lista2

for a in final:
    for b in a:
        if a.index(b) == 0:
            a.insert(a.index(b), b.lower())
            a.pop(a.index(b))

print("".join(lista1[::-1])+" "+"".join(lista2[::-1]))

# zad 4

zdanie = "Ala ma kota, a kot ma Ale"

print(zdanie.split(' '))
