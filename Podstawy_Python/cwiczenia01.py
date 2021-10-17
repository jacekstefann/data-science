# zadanie 1
# 1. Pobierz ze strony https://pl.lipsum.com/ tekst akapitu o tytule „Czym jest Lorem Ipsum” i przypisz go do zmiennej.

tekst = """
Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. 
Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki.
Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. 
Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, 
a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker
"""

# zadanie 2
# 2. Korzystając ze zmiennej z zadania 1 wyświetl na konsoli tekst postaci:
# „W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}” . 
# W miejsca {liczba_liter1} oraz { liczba_liter2} podstaw zmienne, które będą przechowywały liczbę wystąpień danych liter (poszukaj odpowiedniej metody dla typu **str**).
#  Litery, które mają być wyszukane powinny zostać to 4 litera nazwiska oraz 3 litera imienia osoby wykonującej ćwiczenie, 
# np. imie = „Krzysztof”, nazwisko = „Ropiak”, litera_1 = imie[2], litera_2 = nazwisko[3].

imie = 'Jacek'
nazwisko = 'Stefan'

litera_1 = imie[4]
liczba_liter1 = str(tekst.count(litera_1))

litera_2 = nazwisko[3]
liczba_liter2 = str(tekst.count(litera_2))

print('W tekście jest {a} liter {b} oraz {c} liter {d}'.format(a=liczba_liter1, b=litera_1, c=liczba_liter2, d=litera_2))

# zadanie 3
# 3. Przejdź na stronę https://pyformat.info/ a następnie zapisz w oddzielnym pliku .py i wykonaj 5 wybranych przykładów formatowania ciągów oznaczonego jako „New”,
#  których nie było w przykładach z tego podrozdziału (np. z wyrównaniem, ilością pozycji liczby, znakiem itp.).

new = '{} {}'.format('one', 'two')
print(new.count('o'))
print(len(new))
print(new[2:3])
print(new.upper())
print(new.capitalize())