import heapq
from typing import Dict


class DjikstraAlgorithm:
    def __init__(self, graph: Dict) -> None:
        self.graph = graph

    def find_shortest_path(self, startingNode: str):
        # Todas as distâncias para infinito porque não sei quais as distâncias ainda
        distances = {node: float("inf") for node in self.graph}
        # Zero porque estou começando a partir daqui, logo distância para node inicial igual a zero
        distances[startingNode] = 0
        # Conjunto para guardar as nodes visitadas
        visited = set()

        # Priority queue que servirá para guardar as distâncias mais curtas
        priorityQueue = [(0, startingNode)]

        while priorityQueue:
            # Pegue uma node não visitada com a menor distância em relação ao início
            current_distance, current_node = heapq.heappop(priorityQueue)

            # Se a node já tiver sido visitada, volte para o início do loop
            if current_node in visited:
                continue

            # Caso não esteja visitado, então sete como visitado
            visited.add(current_node)

            # Atualize as distância de todos os nós vizinhos ao current_node não visitados
            for neighbor, weight in self.graph[current_node].items():
                new_distance = current_distance + weight
                # Se a distância é menor do que aquela distância atual, então
                # atualize a distância e adicione na priority queue a nova distância
                # Só assim poderemos acessar a menor distância depois
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priorityQueue, (new_distance, neighbor))

        return distances


def main():
    graph = {
        "A": {"B": 1, "C": 3},
        "B": {"C": 2, "D": 10, "E": 7},
        "C": {"E": 4},
        "D": {"E": 2},
        "E": {},
    }
    djikstra = DjikstraAlgorithm(graph)
    shortestPath = djikstra.find_shortest_path("A")
    print(shortestPath)


if __name__ == "__main__":
    main()
