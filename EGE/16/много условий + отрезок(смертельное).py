def f(n):
    if n <= 155:
        return 2 * n * n + 4 * n + 3
    else:
        if n % 3 == 0:
            return f(n - 1) + n * n + 3
        else:
            return f(n - 2) + n - 6

k = 0
for i in range (1, 1001):
    x = str(f(i))
    if len(x) == len([s for s in x if int(s) % 2 != 0]):
        k += 1
print(k)

#  число превращаем в строку и проверяем если количество символов в этой строке
#  ( беру по одоному симовлу изи строчик и превращаем в целочисленный тип и проверяю) видео генератор списков -- чтобы понять








from itertools import(ra)