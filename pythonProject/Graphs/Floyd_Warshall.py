import sys
inf = sys.maxsize
graph = [[0, 3, inf, 7],
         [8, 0, 2, inf],
         [5, inf, 0, 1],
         [2, inf, inf, 0]]

for k in range(4):
    for i in range(4):
        for j in range(4):
            if i != k and j != k and i != j:

                graph[i][j] = min(graph[i][j], (graph[i][k]+graph[k][j]))

print(*graph, sep="\n")
print(c)
