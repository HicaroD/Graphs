class DisjointSet:
    def __init__(self, number_of_vertices: int):
        # Lista para representar o parente de cada node
        self.parent = list(range(number_of_vertices))
        # Lista para guardar a profundidade de cada node na árvore
        self.rank = [0] * number_of_vertices

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, first_node, second_node):
        root_x, root_y = self.find(first_node), self.find(second_node)
        if root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


def main():
    disjoint_set = DisjointSet(5)

if __name__ == "__main__":
    main()
