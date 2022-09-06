with open ('2.txt') as f:
    s = f.readline()
    k = 1
    kmax = 0
    for i in range (1,len(s)):
        if s[i] != s[i - 1]:
            k = 1
        else:
            k += 1
            kmax = max(k,kmax)
print(kmax)