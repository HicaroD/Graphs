import heapq
from typing import Dict


class DjikstraAlgorithm:
    def __init__(self, graph: Dict) -> None:
        self.graph = graph

    def find_shortest_path(self, startingNode: str) -> Dict:
        # Todas as distâncias para infinito porque não sei quais as distâncias ainda
        distances = {node: float("inf") for node in self.graph}
        # Zero porque estou começando a partir daqui, logo distância para node inicial igual a zero
        distances[startingNode] = 0
        # Conjunto para guardar as nodes visitadas
        visited_nodes = set()

        # Priority queue que servirá para guardar as distâncias mais curtas
        priority_queue = [(0, startingNode)]

        while priority_queue:
            # Pegue uma node não visitada com a menor distância em relação ao início
            current_distance, current_node = heapq.heappop(priority_queue)

            # Se a node já tiver sido visitada, volte para o início do loop
            if current_node in visited_nodes:
                continue

            # Caso não esteja visitado, então sete como visitado
            visited_nodes.add(current_node)

            # Atualize as distância de todos os nós vizinhos ao current_node não visitados
            for neighbor, weight in self.graph[current_node].items():
                new_neighbor_distance = current_distance + weight
                current_neighbor_distance = distances[neighbor]
                # Se a nova distância é menor do que aquela distância atual, então
                # atualize a distância e adicione na priority queue a nova distância
                # Só assim poderemos acessar a menor distância depois
                if new_neighbor_distance < current_neighbor_distance:
                    distances[neighbor] = new_neighbor_distance
                    heapq.heappush(priority_queue, (new_neighbor_distance, neighbor))

        return distances


def main():
    graph = {
        "A": {"B": 5, "C": 10},
        "B": {"C": 3, "D": 2, "E": 9},
        "C": {"B": 2, "E": 1},
        "D": {"A": 7, "E": 6},
        "E": {"D": 4},
    }
    djikstra = DjikstraAlgorithm(graph)
    shortestPath = djikstra.find_shortest_path("A")
    print(shortestPath)


if __name__ == "__main__":
    main()
