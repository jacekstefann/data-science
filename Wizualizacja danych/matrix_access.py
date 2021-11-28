import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

print(a)

# wybieranie elementy macierzy

print(a[2,3])
b=a[:2,1:3]
print(b)

b[0,1]=10000

print(b)
print(a)

# poprzez b mamy dostep do a. przy zmianie wartosci b zmieniamy a - b odnosi sie do a poprzez referencje

c=np.array(a[:2,1:3]) # tutaj towrzymy nowa macierz - jak zmienimy c to nie zmienimy a 
                        #  alokujemy nowa pamiec dla macierzy c


# poprzez copy() mozna tworzyc kopie

a[1,-5] #jak chce pobrac element od prawej strony i przekrocze zakres to dostane pusta macierz 
# i nie dostajemy błedu

# wektor:
# a[:,1].shape
# macierz 
# a[:,1:2]


