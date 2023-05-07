from typing import List, Tuple


class Kruskal:
    def __init__(self, graph: dict) -> None:
        self.graph = graph

    def get_sorted_edges(self) -> List[Tuple[str, str, int]]:
        edges = []
        for start_vertex, neighbors in self.graph.items():
            for end_vertex, weight in neighbors.items():
                edges.append((start_vertex, end_vertex, weight))
        return sorted(edges, key=lambda edge: edge[2])

    def find_minimum_spanning_tree(
        self,
    ) -> List[Tuple[int, int, int]]:
        sorted_edges = self.get_sorted_edges()
        parent = [i for i in range(len(self.graph))]
        minimum_spanning_tree = []

        for u, v, weight in sorted_edges:
            parent_u = self.find_parent(parent, int(u) - 1)
            parent_v = self.find_parent(parent, int(v) - 1)
            if self.does_not_form_a_loop(parent_u, parent_v):
                minimum_spanning_tree.append((u, v, weight))
                parent[parent_u] = parent_v
        return minimum_spanning_tree

    def does_not_form_a_loop(self, first_parent: int, second_parent) -> bool:
        return first_parent != second_parent

    def find_parent(self, parent: List[int], node: int) -> int:
        if parent[node] == node:
            return node
        return self.find_parent(parent, parent[node])


def main():
    graph = {
        "1": {"2": 1, "3": 3},
        "2": {"3": 2, "4": 10, "5": 7},
        "3": {"5": 4},
        "4": {"5": 2},
        "5": {},
    }
    kruskal = Kruskal(graph)
    print(kruskal.find_minimum_spanning_tree())


if __name__ == "__main__":
    main()
