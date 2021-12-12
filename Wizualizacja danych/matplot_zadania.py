# Zad1
# Narysuj wykresy dla ciągu funkcji, każdy ciąg umieść na jednym wykresie, n=[1,2,3]:

# Dla każdego wykresu wykonaj:
# Nadaj tytuł, 
# ustal zakresy dla osi, 
# nazwij osie,
# dodaj legendę

import matplotlib.pyplot as mp
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# v=np.linspace(-np.pi, np.pi, 150)

# n=1
# f1 = np.sin(n*v)
# mp.plot(v,f1, color="blue", linewidth=3, linestyle=":", label='sinx')

# n=2
# f2 = np.sin(n*v)
# mp.plot(v,f2, color="red", linewidth=3, linestyle="-", label='sin2x')

# n=3
# f3 = np.sin(n*v)
# mp.plot(v,f3, color="green", linewidth=3, linestyle="-.", label='sin3x')

# mp.ylim(f3.min()*1.2, f3.max()*1.2)
# mp.xlim(v.min()*1.2, v.max()*1.2)
# mp.title("Wykresy z matplotlib")
# mp.legend(loc='best')
# mp.show()

# Zad2.
# W jednym oknie graficznym utwórz 6 wykresów funkcji rozmieszczonych w trzech wierszach i dwóch kolumnach. W pierwszej kolumnie mają znaleźć się funkcje:

# x=np.linspace(-2*np.pi, 2*np.pi, 150)

# f1 = 1 * np.cos(x)
# f2 = 2 * np.cos(x)
# f3 = 3 * np.cos(x)

# f4 = np.cos(1*x)
# f5 = np.cos(2*x)
# f6 = np.cos(3*x)

# mp.subplot(3,2,1)
# mp.plot(x,f1, label='funkcja f1', color="red")

# mp.subplot(3,2,3)
# mp.plot(x,f2, label='funkcja f2', color="red")

# mp.subplot(3,2,5)
# mp.plot(x,f3 , label='funkcja f3', color="red")

# mp.subplot(3,2,2)
# mp.plot(x,f4, label='funkcja f4', color="blue")

# mp.subplot(3,2,4)
# mp.plot(x,f5, label='funkcja f5', color="blue")

# mp.subplot(3,2,6)
# mp.plot(x,f6, label='funkcja f6', color="blue")

# mp.show()

# liczenie wykresow przy powyzszym ulozeniu
# 1 2
# 3 4
# 5 6

# zad 3

# x=np.linspace(-8,8, 450, endpoint=True)
# y=np.linspace(-8,8, 450, endpoint=True)
 
# X = np.meshgrid(x, y)
# Y = np.meshgrid(x, y)

# Z = np.sin(X) + np.cos(Y)

# fig = mp.figure()
# ax = Axes3D(fig)

# ax.plot_surface(X, Y, Z, cmap=mp.cm.hot)

# mp.show()

# zad 4
x=np.linspace(0,10, 50, endpoint=True)
y1 = 1.2*x + np.random.random(x.shape)
y2 = 2*x  + 0.5 + np.random.random(x.shape)
y3 = 2.4*x + 1 + np.random.random(x.shape)

mp.figure()
mp.plot(x,y1, color = 'purple')
mp.plot(x,y2, color = 'green')
mp.plot(x,y3, color = 'red')

mp.fill_between(x, 0, y1, color = 'purple', alpha = 0.1)
mp.fill_between(x, y1, y2, color = 'green', alpha = 0.1)
mp.fill_between(x, y2, y3, color = 'red', alpha = 0.1)
mp.show()