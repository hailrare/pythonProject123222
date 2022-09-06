
with open('17.txt') as f:
    chisla = [int(x) for x in f]
    mas = []
    for i in range(1, len(chisla)):
        if chisla[i] % 3 == 0 or chisla[i-1] % 3 == 0:
            mas.append(chisla[i] + chisla[i-1])
    print(len(mas), max(mas))




