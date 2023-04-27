import sys
graph = {"a": {"b": 6, "c": 4, "d": 5},
         "b": {"e": -1},
         "c": {"b": -2, "e": 3},
         "d": {"c": -2, "e": 9, "f": 22},
         "e": {"c": 5, "f": 3},
         "f": {}

         }


def dijkstra(input_graph, src, des):
    inf = sys.maxsize
    node_data = {}
    for nod in input_graph:
        node_data[nod] = {"cost": inf, "pre": []}
    node_data[src]["cost"] = 0

    for i in range(len(input_graph)-1):
        for temp in graph:
            for node in graph[temp]:
                cost = node_data[temp]["cost"] + graph[temp][node]
                if cost < node_data[node]["cost"]:
                    node_data[node]["cost"] = cost
                    node_data[node]["pre"] = node_data[temp]["pre"] + list(temp)

    print(node_data[des]["cost"], node_data[des]["pre"]+list(des))


dijkstra(input_graph= graph, src="a", des="f")



