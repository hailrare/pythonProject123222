spasite=set()
def f(x, p):
    global spasite
    if p==3:
        spasite.add(x)
    else:
        f(x+2, p+1)
        f(x*3, p+1)
f(2,0)
print(len(spasite))