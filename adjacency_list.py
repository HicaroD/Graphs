class AdjacencyList:
    def __init__(self, number_of_vertices: int) -> None:
        self.number_of_vertices = number_of_vertices
        self.graph = [[] for _ in range(number_of_vertices)]

    def show_graph(self) -> None:
        for self.vertice in self.graph:
            print(self.vertice)

    def add_edge(self, first_vertice: int, second_vertice: int) -> None:
        # TODO: handle index out of range exceptions
        self.graph[first_vertice].append(second_vertice)
        self.graph[second_vertice].append(first_vertice)

    def remove_vertice(self, first_vertice: int, second_vertice: int) -> None:
        # TODO: handle index out of range exceptions
        self.graph[first_vertice].remove(second_vertice)
        self.graph[second_vertice].remove(first_vertice)

    def vertice_exists(self, vertice: int, target_vertice: int) -> bool:
        return vertice in self.graph[target_vertice]

    def get_vertice_degree(self, vertice: int) -> int:
        return len(self.graph[vertice])

    def get_graph_degree(self) -> int:
        return sum(list(map(lambda vertice: len(vertice), self.graph)))

        # Or use a loop, like a normal human being

        # total_degree = 0
        # for vertice in self.graph:
        #     total_degree += len(vertice)
        # return total_degree

    def is_eulerian_graph(self):
        for vertice_index in range(self.graph):
            vertice_degree = self.get_vertice_degree(vertice_index)
            if vertice_degree % 2 != 0:
                return False
        return True


def main():
    graph = AdjacencyList(10)
    graph.add_edge(0, 1)
    assert graph.vertice_exists(0, 1)
    print(graph.get_graph_degree())
    graph.show_graph()


if __name__ == "__main__":
    main()
