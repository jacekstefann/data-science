# uproszczenia i sprawniejsze opisanie

lista = []
for element in range(5):
    if element > 0:
        lista.append(element*element)

# python comprehension:
lista = [element*element for element in range(5) if element > 0]

