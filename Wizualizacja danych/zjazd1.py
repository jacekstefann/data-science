# numpy
import numpy as np
from numpy.core.fromnumeric import reshape


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

vv =  np.array([np.arange(0,10,step=2), np.arange(10,20,step=2)])
print(vv)


# macierz 3d

b1 = np.array([ 
                [ [1, 2], [3, 4], [5, 6] ],
                [ [11, 12], [13, 14], [15, 16] ],
                [ [21, 22], [23, 24], [25, 26] ],
                [ [31, 32], [33, 34], [35, 36] ],
              ])

print(b1.shape)

a2 = np.arange(12)

# reshape - kompresuje macierz - zmienia jego wymiar

a2 = a2.reshape(3,4)

print(a2)

# dopbieranie sie do elementow macierzy
a2[0,0]

# a[wiersze, kolumny] wymiary liczymy od 0
print(a2[2,3])

# a2[0,:] - z wiersza 0 zwroc wszystko
# a2[0] - wiersz zerowy alternatywa dla powyzszej

# a2[:,1] - wszystko z 2 kolumny

a2[:,1].reshape(3,1)  

wiersze, kolumny = a2.shape

wiersze 

kolumny

a2[:,1].reshape(wiersze,1)  

print(b1)

print(b1[0,0,0])

print(b1[3,2,1])

# pobierac elementy mozna tez od konca
# a2[0,-1]

# zabieranie elementow z kolumn z przedzialu
# a2[-1, 1:-2]

# a2[1, [1,3]] - podawanie wektora do zbierania konkretnych danych 2 kolumna element 2 i 4
 
b1[0] # pobieramy 1 macierz 
#  alternatywa: b1[0, :, :]

b1[:, 0, :]
b1[:, :, 0]
