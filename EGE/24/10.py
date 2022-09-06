with open ('10.txt') as f:
    s = f.readline()
    k = 0
    kmax = 0
    for i in range (len(s)):
        if (s[i] == 'A' and k % 2 == 0) or (s[i] == 'B' and k % 2 == 1):
            k += 1
            kmax = max(k, kmax)
        else:
            k = 0
print(kmax)