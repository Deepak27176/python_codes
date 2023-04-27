list1 =["abcd", "bcdf", "efgh","dcbe"]

def odd_one(list2):
    for i in list2:
        k = list(i)
        for j in range(0, len(k)-1):
            if ord(k[j])>=ord(k[j+1]):
                return i


print(odd_one(list1))
