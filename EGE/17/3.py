with open('1.txt') as f:
    chisla = [int(x) for x in f]
    mas =[]
    res = []
    for i in range (len(chisla)):
        if chisla[i] % 17 == 0:
            mas.append(chisla[i])
    print(min(mas))