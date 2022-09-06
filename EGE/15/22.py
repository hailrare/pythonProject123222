k = 0
for a in range(1000):
    for x in range (1000):
        if (x % 3 == 0) <= (x % 5 != 0) or (x + a >= 70) == 1:
            k += 1
        if k == 1000000:
            print(a)
            break
