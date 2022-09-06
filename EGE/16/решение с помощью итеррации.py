s = 100000001 *[0]
for n in range (len(s)):
    if n == 0:
        s[n] = 8
    else:
        if n % 3 == 0:
            s[n] = 5 + s[n // 3]
        else:
            s[n] = s[n // 3]
print(s.count(18))

#count считает сколько раз была произведенаа операция