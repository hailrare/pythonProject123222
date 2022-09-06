with open ('3.txt') as f:
    s = f.readline()
    k = 1
    kmax = 1
    for i in range (1 , len(s)):
        if (s[i-1] != 'Y' or s[i] != 'Y'):
            k = 1
        else:
            k += 1
            kmax = max(k, kmax)
print(kmax)