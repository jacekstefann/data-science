import numpy as np

# Utwórz tablicę liczb od 1 do 100.
# v = np.arange(1,100)
# print(v)

# Utwórz tablicę liczb dodatnich, podzielnych przez 11 do 1000.
# v= np.arange(1,1000)
# b = v[ np.mod(v,11)==0]
# print(b)

# Utwórz tablice liczb od -5 do 5 składającą się z 70 liczb dzielących ten odcinek na równe części
# v = np.linspace(-5,5, num=70)
# print(v)

# ad2. 
# Utwórz macierze a=[1 2 3] i b=[4 5 6] upewnij się co do wymiarów 
# (shape). Oblicz:
# sumę, różnicę iloczyn, iloraz, transpozycję tablic
#  oraz pierwiastki elementów obu tablic. 
# a+b’, 
# a*b, 
# a*b’, 
# a’*b, 
# a’*b’
 
# a=np.matrix([1, 2, 3])
# a=np.arange([[1, 2, 3]])

# b=np.matrix([4, 5, 6])
# b=np.arange([[4, 5, 6]])


# print(a.shape)
# print(b.shape)

# print(a+b.T)
# print(a*b)
# print(a*b.T)
# print(a.T*b)
# print(a.T*b.T)


# Zad3.
# Wykonaj obliczenia:

# Utwórz tablicę sinusów, cosinusów od 0 do pi co 1/10.
# v = np.sin(np.arange(0,np.pi, step=0.1))
# print(v)
# v = np.cos(np.arange(0,np.pi, step=0.1))
# print(v)

# Oblicz wartości sześcianów liczb z tablicy o elementach 
# -100 do 100 co 2, 

# v= np.power(np.arange(-100,100,step=2),3)
# print(v)

# [-100, -98, -96 … 98, 100]
# Oblicz pierwsze 20 potęg liczby 2 2^0, 2^1,...2^19

# v = np.arange(0,20)
# print(v)
# print(np.power(2,v))

# Utwórz tablicę liczb, w której na pozycji “i” znajduje 
# się suma elementu “i”+ “i-1” 
# [0+1, 1+2, 2+3, ……...99+100]


# nie wiem
# print(np.arange(0,99)+np.arange(1,100))


# Zad4.
# Utwórz po 100 wyrazów ciągów z poszczególnych przykładów
#  dla n=1...100 i oblicz ich sumę (nie możesz używać pętli)

# 1/n (wynik = 5.1773775176396208) 
# Utwórz wektor o elementach [1/1, 1/2,  1/3 … 1/100]
# Oblicz sumę elementów tego ciągu
# 1/sqt(n) ( wynik = 18.489603824784155)
# (1+1/n)^n (wynik = 263.33113457760766)


# v = np.sum(1/np.arange(1,100))
# print(v)

# v=1/np.arange(1,100)
# b = np.array(v)
# c= sum(b)
# print(c)

# v = np.sum(1/np.sqrt(np.arange(1,100)))
# print(v)

# v = np.sum(np.power(1+(1/np.arange(1,100)), np.arange(1,100)))
# print(v)



# Zad5.
# Utwórz macierz A o wymiarach 7x7 (elementy dowolne)
# Znajdź element z 3 wiersza 4 kolumny
# Podstaw za element z 6 wiersza 3 kolumny liczbę π.
# Utwórz macierz B składającą się z 3 pierwszych wierszy i kolumn od 2 do 6 
# Utwórz macierz C – z trzech pierwszych kolumn, 
# Utwórz macierz D – z czterech ostatnich wierszy

a = np.zeros((7,7))+1
# print(a[3,4])

# a[6,3]=np.pi
# print(a)

b = a[1:3,2:6]
print(b)

# c = a[,1:3]
d = a[:-4,]

