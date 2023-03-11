class IncidenceMatrix:
    # Matriz de incidêNcia é outra forma de representar um grafo,
    # As linhas são vértices e colunas são arestas.

    def __init__(self, number_of_vertices: int, number_of_edges: int) -> None:
        self.number_of_vertices = number_of_vertices
        self.number_of_edges = number_of_edges
        self.graph = [
            [0 for _ in range(number_of_edges)] for _ in range(number_of_vertices)
        ]

    def show_graph(self):
        for vertice in self.graph:
            print(vertice, end="\n")

    # Para ligar um vértice a outra, precisamos escolher uma aresta para ligá-los.
    def add_edge(
        self,
        first_vertice: int,
        second_vertice: int,
        edge_number: int,
    ) -> None:
        self.graph[first_vertice][edge_number] += 1
        self.graph[second_vertice][edge_number] += 1

    # Para remover a ligação entre dois vértices, precisamos fazer a mesma coisa da adição de arestas,
    # mas, dessa vez nós subtraímos os valores.
    def remove_edge(
        self,
        first_vertice: int,
        second_vertice: int,
        edge_number: int,
    ) -> None:
        self.graph[first_vertice][edge_number] -= 1
        self.graph[second_vertice][edge_number] -= 1

    # Para saber se existe uma ligação entre dois vértices, precisamos escolher também a aresta, 
    # pois podemos ter qualquer aresta do grafo ligando dois vértices
    def edge_exists(
        self,
        first_vertice: int,
        second_vertice: int,
        edge_number: int,
    ) -> bool:
        return (
            self.graph[first_vertice][edge_number] > 0
            and self.graph[second_vertice][edge_number] > 0
        )


def main():
    graph = IncidenceMatrix(number_of_edges=4, number_of_vertices=4)
    graph.add_edge(1, 2, 3)
    graph.show_graph()


if __name__ == "__main__":
    main()
