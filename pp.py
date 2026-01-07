class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, src, dest):
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dest not in self.adj_list:
            self.adj_list[dest] = []
        self.adj_list[src].append(dest)

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_helper(start_vertex, visited)

    def _dfs_helper(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        if vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    self._dfs_helper(neighbor, visited)

def main():
    g = Graph()

    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        src = int(input("Enter source vertex: "))
        dest = int(input("Enter destination vertex: "))
        g.add_edge(src, dest)

    start_vertex = int(input("Enter the starting vertex for DFS: "))

    print("DFS Traversal:")
    g.dfs(start_vertex)

if __name__ == "__main__":
    main()
