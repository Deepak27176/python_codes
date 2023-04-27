n = int(input())

def recursive_Range(m):
    if m == 0:
        return 0
    else:
        return m+recursive_Range(m-1)

print(recursive_Range(n))