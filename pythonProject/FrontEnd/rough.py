lis = list(map(int, input().split(sep=" ")))
n = len(lis)
lis.sort()
# for i in range(0, len(lis)-1):
#     for j in range(0, n-i-1):
#         if lis[j] > lis[j+1]:
#             lis[j], lis[j+1] = lis[j+1], lis[j]
print(*lis, sep=" ")

k= "".join(map(str, lis))
print(type(k))
def binary_search(f, l, key, lis):
    if f>l:
        return False
    mid = (f+l)//2
    if lis[mid] == key:
        return True
    elif key < lis[mid]:
        return binary_search(f, mid-1, key, lis)
    elif key>lis[mid]:
        return binary_search(mid+1, l, key, lis)

print(binary_search(0,n,7,lis))