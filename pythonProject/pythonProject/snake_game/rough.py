list1 = input()
list2 = input()
list1 = list(list1)
count1 = 0
for i in range(0, len(list1)):
    if list1[i] == list2[i]:
        count1 += 1
print(count1)