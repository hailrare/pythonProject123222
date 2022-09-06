'''самая простая рекурсия
def f(n):
    if n == 1:
        return 2.txt
    if n > 1:
        return f(n - 1) + 5.txt * n ** 2.txt

print(f(39))
'''




''' тут есть несколько условий и с пмощью else  мы исключаем их
def f(n):
    if n < 3:
        return 2.txt * n
    else:
        if n % 2.txt == 0:
            return 3 * n + 5.txt + f(n - 2.txt)
        else:
            return n + 2.txt * f(n - 6)

print (f(61))
'''






'''  тут мы просто описываем 2 а не одну функцию прсто в 2 разных прикола
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2.txt * f(n-1) + g(n - 1) -2.txt * n
def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + 2.txt * g(n - 1) + n

print(f(14) + g(14))
'''



''' тут мы с пощью доп цикла создаем условие (этот цикл пока что неведомым для меня спосбом передает все нужные значения в первую функцию
def f(n):
    if n <= 3:
        return n
    else:
        if n % 2.txt == 0:
            return 2.txt * n + f(n - 1)
        else:
            return n * n +f(n - 2.txt)

k = 0
for i in range (1, 101):
    if f(i) % 3 == 0:
        k += 1
print(k)
'''






