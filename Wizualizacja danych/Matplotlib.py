import matplotlib.pyplot as pl
import numpy as np

# define number of samples to generate
n = 256  #na ile elementow bedziemy dzielic przedzial
# create linear space from -pi to pi
X = np.linspace(-np.pi, np.pi, n, endpoint=True)  #zbior naszych danych
# create sine and cosine vectors
C, S = np.cos(X), np.sin(X) #przypisujemy dane na cos i sin
# plot cosine
pl.plot(X, C)   #tworze wykresy dla danych x i y = sin lub cos
# plot sine
pl.plot(X, S)

print("1.1 Simple plotting example")
# show finished plot
pl.show() #na koncu skryptu trzeba wywolac funckje show zeby pokazac wykresy
# bez show wykres sie nie pojawi mozna dodawac x wykresow na siebie i na koniec dac show i wtedy pokazac calosc


