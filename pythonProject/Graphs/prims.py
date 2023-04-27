# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, m, edges, start):
    # Write your code here
    e = 0
    lis = {}
    sum1 = 0
    duplicates = []

    for i in range(m - 1):
        for j in range(m - i - 1):
            if edges[j][2] > edges[j + 1][2]:
                edges[j], edges[j + 1] = edges[j + 1], edges[j]
        if edges[i][0] ==
    # print(*edges, sep='\n')
    for i in edges:
        if i[0] not in lis:
            lis[i[0]] = [i[1]]
        else:
            lis[i[0]].append(i[1])
        if i[1] not in lis:
            lis[i[1]] = [i[0]]
        else:
            lis[i[1]].append(i[0])
        if set(lis[i[0]]) - set(lis[i[1]]) == set(lis[i[0]]):
            print(set(lis[i[0]]) - set(lis[i[1]]))
            if e < n - 1:
                print(i[2])
                sum1 = sum1 + i[2]
                e += 1
            else:
                break

    return sum1


# edges = [[1, 2, 3],
#          [1, 3, 4],
#          [4, 2, 6],
#          [5, 2, 2],
#          [2, 3, 5],
#          [3, 5, 7]]
edges = [[1, 2, 1],
         [1, 4, 100],
         [1, 3, 200],
         [3, 2, 150],
         [4, 3, 99]
         ]
print(prims(4, 5, edges, 1))
