from queue import Queue


class GraphSearch:
    def __init__(self, graph: dict) -> None:
        self.graph = graph

    # Breadth First Search (BFS) é um método para poder atravessar um grafo.
    # A ideia de BFS é a seguinte:
    # Escolhemos um vértice como inicial (qualquer um do grafo), visitamos todos os
    # vértices adjacentes (vizinhos) desse vértice.
    # Depois eu vou visitar o vizinho dos vizinhos, e assim por diante.
    def breadth_first_search(self, initial_node: str) -> list[str]:
        traversion_result = []
        visited = set()
        nodes = Queue()

        nodes.put(initial_node)
        visited.add(initial_node)

        while not nodes.empty():
            current_node = nodes.get()
            traversion_result.append(current_node)

            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    nodes.put(neighbor)
                    visited.add(neighbor)

        return traversion_result

    # Depth First Search (DFS) é um método para poder atravessar um grafo.
    # A ideia de DFS é a seguinte:
    # Escolhemos um vértice inicial (qualquer um do grafo) e vamos a fundo nos vizinhos desse
    # vértice até não conseguir mais. Caso você chegue em um "caminho fechado" (em um vértice onde
    # não possui vizinhos), nós voltamos e continuamos explorando.
    def depth_first_search(self):
        pass


def main() -> None:
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    graph_search = GraphSearch(graph)
    print(graph_search.breadth_first_search("A"))


if __name__ == "__main__":
    main()
