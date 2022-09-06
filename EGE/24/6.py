with open ('6.txt') as f:
    s = f.readline()
    k = 1
    kmax = 0
    for i in range (1,len(s)):
        if s[i] != s[i-1]:
            k += 1
            kmax = max(k,kmax)
        else:
            k = 1
print(kmax)