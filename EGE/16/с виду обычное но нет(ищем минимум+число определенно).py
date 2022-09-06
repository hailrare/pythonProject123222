def f(n):
    if n <= 1:
        return n
    else:
        if n % 3 == 0:
            return n + f(n / 3)
        else:
            return n + f(n + 3)

for n in range (1,1000):
    try:
        if f(n) > 100:
            print(n)
            break
    except BaseException:
        pass

#тут необходимо написать try перед циклом и except  и название ошибки (можно BaseException) и pass
# это делаеться что бы рекурсия не уходила в бесконечность !!!!!!!