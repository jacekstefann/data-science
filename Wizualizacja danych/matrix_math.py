import numpy as np

x = np.array([1, 2])  # Let numpy choose the datatype
print( x.dtype)         # Prints "int64"

x = np.array([1., 2.])  # Let numpy choose the datatype
print( x.dtype)             # Prints "float64"

x = np.array([1, 127], dtype=np.int8)  # Force a particular datatype
print(x.dtype)       

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print(x+y)

# mnozenie i dzielenie macierzy nie odbywa sie tak jak bysmy myslei, ze kazdy element przez kazdy
# tylko element przez element na danej pozycji

np.sqrt(x) #pierwiastek z kazdej liczby w macierzy

v = np.array([0, 1, 1])
w = np.array([0, 1, 0])
k = np.array([1, 1, 0])

# iloczyn skalarny dwoch wektorow
k.dot(w)
k.dot(v)

x = np.array([[1,2],[3,4]])
# x.dot(v)

# nalezy pamietac o wymiarach macierzy ilosc kolumn w macierzy
# musi być taka sama tj:
# (x) w1 x k1 (y) k1 k2

np.sum(x) #suma wszystkich elemtow macierzy
np.sum(x, axis=0) #suma po wierszach
np.sum(x, axis=1) #suma po kolumnach

np.mean(x) #srednia
np.mean(x, axis=0) # srednia po wierszach
np.mean(x, axis=1) # srednia po kolumnach


# macierz losowa o wymiarach 5x5 
# do kolumn 1 i 3 dodac losowe wartosci 
# policzcie sumy srednie dla kolumn
# ustandaryzowac warotsci w kolumnach (od kazdej wartosci robimy - mean/std)

v1 = np.random.random((5,5))
v2 = np.random.random((5,5))
print(v2)
v2[:,[1,3,4]]=0
print(v2)
v3 = v1+v2
print(v3)
print(np.mean(v3, axis=0))
print(np.sum(v3, axis=0))
print(np.mean(v3, axis=0)/np.sum(v3, axis=0))
print(v3 - np.mean(v3, axis=0)/np.std(v3, axis=0))

# rozw:
# v1 = np.random.random((5,5))
# v2 = np.random.random((5,5))
# v2[:,[1,3,4]]=0
# v3 = v1+v2
# np.mean(v3, axis=0)
# np.sum(v3, axis=0)
# v3 - np.mean(v3, axis=0)/np.std(v3, axis=0)

a = np.arange(24).reshape(4,6)
print(a)

# najpierw wybieram przez zakres, potem przez referencje do kolkretnych kolumn
a[1:3, [1,3,5]]

# referencje mozna powielac
a[1:3, [1,1,3,3,5,5]]

# indeksowanie boolowskie
# dostajemy elementy, te ktore maja true (spelniony warunek)
# najpierw daje macierz true/false
# nastepnie na podstawie waunkow daje wartosci, ktore chcemy
a>11
print(a[a>11])

print([(a>10) & (a<19)])

# transpozycja macierzy
print(a.T)

# funkcja power(2,3) - dwa do potegi 3



