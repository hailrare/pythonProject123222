for a in range(1, 1000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if ( (y +2*x != 48)or(a < x) or (x < y)  ) == False:
                flag=False
                break
        if flag == False:
            break
    if flag == True:
        print(a)



