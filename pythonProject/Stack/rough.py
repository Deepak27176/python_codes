list1 = list(map(int, input().split(" ")))

def fun(lis):
    temp1 = []
    temp2 = []
    temp3 = []

    for i in lis:
        if i % 2 == 0:
            if i%5 == 0:
                temp1.append(i)
            else:
                temp2.append(i)
        else:
            temp3.append(i)

    temp1.sort()
    temp1.reverse()
    temp2.sort()
    temp1.extend(temp2)
    temp1.extend(temp3)
    return temp1


print(fun(list1))