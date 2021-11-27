# w pythonie mamy 2 petle: for i while

# petla for -  petla iteracyjna
# range jest funckja, w ktorej nie podawana jest ostatnia wartosc
# range jest generatorem generujacym liste z zadanego przedzialu
from typing import Counter


for i in range (0,3):
    print(i)

# enumerator - zwraca pare (indeks wartosc) na elemencie iterowalnym 
# enumerator - rozpakowuje krotke
# funkcja przyjmuje wartosc start (enumerate(lista, start = x))
# start domyslenie = 0 czyli startuje od poczatku ale mozna to zmienic
# ze np. od 10ego elementu

# slowniki tez sa iterowalne
# iterujemy po key, values, items

krotka = (1, 'Krzysztof', 'Ropiak', 1,2,3,4)
krotka2 = (1, 'Krzysztof', 'Ropiak', 1,2)

id, imie, nazwisko, par1, par2, par3, par4 = krotka
id, imie, nazwisko, *par = krotka2 #dodatkowo rozpakowujemy parametry par
# robimy to w sytuacji gdy chcemy cos wydrukowac, a nie mamy stalej liczby elementow


# petla while
while True:
    counter += 1
    print(counter)
    if counter > 10:
        break
# break  zakonczenie biezacej petli

# petla for dla skonczonego zbioru, while dla zbioru, ktorego wielkosc nie znamy
# continue powoduje zakonczenie biezacej iteracji i przejscie do poczatku petli


