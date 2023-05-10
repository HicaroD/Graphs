import heapq


class Prim:
    def __init__(self, graph: dict) -> None:
        self.graph = graph

    def find_minimum_spanning_tree(self):
        # Instanciando minha minimum spanning tree
        minimum_spanning_tree = []

        # Conjunto para checar de forma eficiente se vértice foi visitado ou não
        visited = set()

        # Comece por qualquer vértice do grafo
        starting_vertex = list(self.graph.keys())[0]

        # Sete esse vértice como visitado
        visited.add(starting_vertex)

        # Crie uma priority queue com todos os vértices que estão conectados com o vértice inicial
        edges = [
            (starting_vertex, neighbor, weight)
            for neighbor, weight in self.graph[starting_vertex].items()
        ]
        # Transforme o que é apenas uma lista (edges) em uma priority queue
        heapq.heapify(edges)

        # Enquanto ainda tiver elementos não visitados
        while edges:
            # Obtenha a aresta com custo mínimo (graças a priority queue, isso é possível)
            source, target, weight = heapq.heappop(edges)

            if target not in visited:
                visited.add(target)
                minimum_spanning_tree.append((source, target, weight))

                # Adicione todas as conexões vizinhas do vértice na priority queue
                for neighbor, weight in self.graph[target].items():
                    if neighbor not in visited:
                        heapq.heappush(edges, (target, neighbor, weight))

        return minimum_spanning_tree


def main():
    graph = {
        "A": {"B": 1, "C": 3},
        "B": {"C": 2, "D": 10, "E": 7},
        "C": {"E": 4},
        "D": {"E": 2},
        "E": {},
    }
    prim = Prim(graph)
    print(prim.find_minimum_spanning_tree())


if __name__ == "__main__":
    main()
