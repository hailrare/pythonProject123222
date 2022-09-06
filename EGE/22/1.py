for i in range (1,101):
    s = i
    p = 10
    q = 8
    k1 = 0
    k2 = 0
    while s <= 100:
        s = s - q
        k2 = k2 + 1
    while s>=q:
        s = s - q
        k2 = k2 +1
    k1 += s
    k2 += s
print(i, k1, k2)