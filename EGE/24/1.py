with open('1.txt') as f:
    s = f.readline()
    count = 1
    maxi = 0
    for i in range (1 , len(s)):
        if s[i] == s[i - 1]:
            count = 1
        else:
            count += 1
            maxi = max(count, maxi)
print (maxi)