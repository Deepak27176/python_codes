import sys
graph = {"a": {"b": 2, "c": 4},
         "b": {"a": 2, "c": 3, "d": 8},
         "c": {"a": 4, "b": 3, "d": 2, "e": 5},
         "d": {"b": 8, "c": 2, "e": 9, "f": 22},
         "e": {"c": 5, "d": 9, "f": 1},
         "f": {"d": 22, "e": 1}

         }


def dijkstra(input_graph, src, des):
    inf = sys.maxsize
    node_data = {}
    for nod in input_graph:
        node_data[nod] = {"cost": inf, "pre": []}
    node_data[src]["cost"] = 0
    temp = src
    visited = []
    for i in range(len(input_graph)):
        if temp not in visited:
            visited.append(temp)
            flag = 0
            for node in graph[temp]:
                if node not in visited:
                    cost = node_data[temp]["cost"] + graph[temp][node]
                    if cost < node_data[node]["cost"]:
                        node_data[node]["cost"] = cost
                        node_data[node]["pre"] = node_data[temp]["pre"] + list(temp)
                    if flag == 0:
                        min_cost = node_data[node]["cost"]
                        pre_temp = node
                        flag += 1
                    elif node_data[node]["cost"] < min_cost:
                        min_cost = node_data[node]["cost"]
                        pre_temp = node

            temp = pre_temp
            node_data[temp]["cost"] = min_cost
    print(node_data[des]["cost"], node_data[des]["pre"]+list(des))


dijkstra(input_graph= graph, src="a", des="e")



