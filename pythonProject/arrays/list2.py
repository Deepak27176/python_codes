list2 = list(map(int, input().split(" ")))
s = int(input())
for i in range(0, len(list2)):
    for j in range(i+1, len(list2)):
        if list2[i] == list2[j]:
            pass
        elif list2[i]+list2[j] == s:
            print([i, j])
