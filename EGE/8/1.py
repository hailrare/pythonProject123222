from itertools import product
words = product('апрсу', repeat = 5)
k = 0
for w in words:
    k += 1
    word = ''.join(w)
    if word[0] == 'y' and 'aa' not in word:
        print(k)
        break