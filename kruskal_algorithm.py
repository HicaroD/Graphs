from typing import List, Tuple


class Kruskal:
    def __init__(self, graph: dict) -> None:
        self.graph = graph
        self.parents = [i for i in range(len(self.graph))]

    def find_minimum_spanning_tree(self) -> List[Tuple[int, int, int]]:
        minimum_spanning_tree = []
        sorted_edges = self._get_sorted_edges()

        for start_vertex, end_vertex, weight in sorted_edges:
            start_vertex_parent = self._find_parent(int(start_vertex) - 1)
            end_vertex_parent = self._find_parent(int(end_vertex) - 1)

            if self._does_not_form_a_loop(start_vertex_parent, end_vertex_parent):
                minimum_spanning_tree.append((start_vertex, end_vertex, weight))
                self.parents[start_vertex_parent] = end_vertex_parent
        return minimum_spanning_tree

    def _get_sorted_edges(self) -> List[Tuple[str, str, int]]:
        edges = []
        for start_vertex, neighbors in self.graph.items():
            for end_vertex, weight in neighbors.items():
                edges.append((start_vertex, end_vertex, weight))
        return sorted(edges, key=lambda edge: edge[2])

    def _find_parent(self, node: int) -> int:
        if self.parents[node] == node:
            return node
        return self._find_parent(self.parents[node])

    def _does_not_form_a_loop(self, first_parent: int, second_parent: int) -> bool:
        return first_parent != second_parent


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
