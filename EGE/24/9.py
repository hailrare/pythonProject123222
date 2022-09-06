with open ('9.txt') as f:
    s = f.readline()
    k = 1
    kmax = 1
    for i in range (1,len(s)):
        if s[i] == 'C' and s[i - 1] == 'C':
            k +=1
            kmax = max(k, kmax)
        else:
            k = 1
print(kmax)