# # zad 4

# for i in range(0,51):
#     if i%5==0:
#         print(i)

# # zad 5
# li = input("podaj liczby: ")
# a = li.split(' ')

# for i in a:
#     print(i, int(i)**2)

# # # zad 6
# lista = []
# while True:
#     a = input("podaj liczbe:")
#     if a == 'stop':
#         break
#     else:
#         lista.append(a)
#     print(lista)

# # zad 7
# a = input("podaj liczbe: ")
# b = 0
# for el in a:
#     b+=int(el)

# print(b)

# # zad 8
# b = input("podaj wysokosc: ")
# i=0
# while i < int(b):
#     print("A"*i)
#     i+=1
#     if i == 10:
#         break        


# # zad 9
# for i in range(1,11):
#     print("*"*5," ", i, " ","*"*5)
#     for b in range(1,11):
#         print(i, "*", b, " = ", i*b)
#     print("-"*20)

# licznik = 10

# print('  ', end='')
# for i in range(1,licznik+1):
#     print(f'{i:>4}', end='')
# print()

# for i in range(1,licznik+1):
#     print(f'{i:>2}', end='')
#     for j in range(1,11):
#         print(f'{i*j:>4}', end='')
#     print()



# zad 10
# wym = input("podaj wymiar diamentu (miedzy 3 a 9): ")
# i=1
# while i <= int(wym):
#     print(str("o"*i).center(int(wym)+1)) 
#     i+=2
# i-=4
# while i >= 1:
#     print(str("o"*i).center(int(wym)+1)) 
#     i-=2

def zadanie_10(znak,w):
    if w in [3,5, 7, 9]:
        linie = list(range(1, w+1, 2)) + list(range(w-2,0,-2))

        for i in linie:
            print(f'{znak * i:^{w}}')

zadanie_10("f", 4)