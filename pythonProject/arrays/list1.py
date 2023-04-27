list1 = []
for i in range(1,101):
    if i != 55:
        list1.append(i)
print(int((100*101)/2)-sum(list1))