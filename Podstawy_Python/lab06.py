# zad 1
# A
# b = [1/x for x in range(1,10)]
# print(b)

# # B
# c = [2**i for i in range(10)]
# print(c)

# # C
# d = [x for x in D if x % 4 == 0]
# print(d)

# # zad 2
# import random as rand

# macierz = [
#             [1,2,3,4],
#             [1,2,3,4],
#             [1,2,3,4],
#             [1,2,3,4]
#             ]

# liczba = rand.randint(1,100)
# macierz = [[rand.randint(1,100) for _ in range(4)] for _ in range(4)]

# poniższe rozwiazanie to jest to samo co powyzej tylko bez python comprehension
# macierz = []
# for _ in range(4):
#     wiersz = []
#     for _ in range(4):
#         wiersz.append(rand.randint(1,100))
#     macierz.append(wiersz)

# zad 4
slow = {
    'jajka': 'szt'
    , 'ziemniaki': 'kg'
    , 'chleb': 'szt'
    , 'mleko': 'szt'
}

wynik = [klucz for klucz in slow.keys() if slow[klucz] == 'szt']

print(wynik)