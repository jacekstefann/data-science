from numpy import concatenate


import numpy as np


a1 = np.arange(0,24,step=1)
print(a1)

# reshape - zmienia uklad ulozenie elementow w macierzy

a1 = np.ones((3,3))
a2 = np.ones((8,3))*2
a3 = np.ones((3,7))*3

# concatenate funckaja do laczenie wartosci z roznych macierzy (dokłada obok)
# funkcja concatenate twrozy nowa macierz

print(a1)
print(a2)
print(a3)

b = np.concatenate((a1, a2))
print(b)

# funkcja stack pozwala na dolozenie nowej osi

v1 = np.arange(1,5)
v2 = np.arange(5,9)
print(v1)
print(v2)

# concatenate dolozyla by wartosci obok, stack stworzy dodatkowe wymiary

vv = np.stack((v1,v2),axis=0)
vh = np.stack((v1,v2),axis=1)
print(vv)
print(vh)

# funkcja split dzieli mi macierz na czesci
# dzieli to na macierz list x elementowych
x = np.arange(15)
xs= np.split(x, 3)
print(xs)

# mozna tez okreslac, po ktorych indeksach ma zostac wykonany podzial
xs = np.split(x, [3, 5, 6, 10])


# funkcja tile doklada to samo do wektora
b = np.array([0, 1, 2])
print(np.tile(b, 2))
print(np.tile(b, (2,2)))