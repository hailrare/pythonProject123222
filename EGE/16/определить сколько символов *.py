k = 0
def f(n):
    global k
    k += 1
    if n >= 1:
        k += 1
        f(n-1)
        f(n-2)
        k += 1

f(35)
print(k)

# тут мы заменяем (принт звездочка) на к +1 и не забываем глобализировать
# почему то через лен не получаеться