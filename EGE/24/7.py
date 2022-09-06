with open ('7.txt') as f:
    s = f.readline()
    k = 1
    kmax = 0
    for i in range (1, len(s)):
        if s[i] == 'A' and s[i - 1] == 'A':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 1
print(kmax)