lis = list(map(int, input().split(" ")))


def pro_of_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        k = arr[0]
        arr.pop(0)
        return k*pro_of_array(arr)


print(pro_of_array(lis))
