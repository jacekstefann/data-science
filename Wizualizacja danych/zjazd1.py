# numpy
import numpy as np


ll = [1, 2, 3, 4, 5]

print(ll)
# zmiana listy na werktor
v0 = np.array(ll)
print(v0)

print(v0.dtype)


# tworzenie tablicy z zakresu:
v2 = np.arange(1,10,step=0.5)
print(v2)

# linspace - dzieli okreslone przedzialy na kawalki
v3 = np.linspace(0,10, num=10)
print(v3)
# endpoint w powyzszej funkcji nie uwzglednia ostatniej wartosci z przedzialu

# shape powie nam o wielkosci macierzy / liczbie kolumn / wymiar
print(v3.shape)

# tworzenie macierzy
a1 = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(a1)
print(a1.shape)
# wynik (2,4) - dwa wiersze 4 kolumny

a2 = np.array([[1, 2, 3],[5, 6, 7]])
print(a2)
print(a2.shape)

# maciez zerowa
a3 = np.zeros((3,3))
print(a3)

# alternatywna funkcja jest ones tylko, ze tutaj mamy maciez z 1ek

# maciez jednostkowa
a5 = np.eye(5)
print(a5)

# maceiz gdzie na diagonali sa 6
a6 = np.eye(5)*6
print(a6)


# maciez losowa
a7 = np.random.random((2,3))
print(a7)

