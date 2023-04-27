class Graph:
    def __init__(self, gdict={}):
        self.gdict = gdict

    def add_edge(self, vertex, edge):
        if vertex in self.gdict:
            self.gdict[vertex].append(edge)
        else:
            self.gdict[vertex] = [edge]

    def bfs(self, vertex):
        visited = [vertex]
        helper_queue = [vertex]
        while helper_queue:
            de_vertex = helper_queue.pop(0)
            print(de_vertex)
            for adjacent in self.gdict[de_vertex]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    helper_queue.append(adjacent)

    def dfs(self, vertex):
        visited = [vertex]
        helper_queue = [vertex]
        while helper_queue:
            de_vertex = helper_queue.pop()
            print(de_vertex)
            for adjacent in self.gdict[de_vertex]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    helper_queue.append(adjacent)

    def sssp(self, start, end):
        helper_queue = []
        helper_queue.append([start])
        while helper_queue:
            path = helper_queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict[node]:
                new_path = list(path)
                new_path.append(adjacent)
                helper_queue.append(new_path)



Dict = {
    "a": ['b'],
    "b": ['a', 'd', 'e'],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["b", "c", "d", "f"]

}
graph = Graph(Dict)

# print(graph.gdict)
graph.add_edge("a", "c")
graph.add_edge("f", "d")
graph.add_edge("f", "e")
# print(graph.gdict)
# graph.dfs("a")
print(graph.sssp("a","f"))


