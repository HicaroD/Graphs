class IncidenceMatrix:
    # Matriz de incidêNcia é outra forma de representar um grafo,
    # As linhas são vértices e colunas são arestas.

    def __init__(self, number_of_vertices: int, number_of_edges: int) -> None:
        self.number_of_vertices = number_of_vertices
        self.number_of_edges = number_of_edges
        self.graph = [[0] * self.number_of_edges for _ in range(number_of_vertices)]

    def show_graph(self):
        for vertice in self.graph:
            print(vertice, end="\n")

    # Para ligar um vértice a outra, precisamos escolher uma aresta para ligá-los.
    def connect_edge(
        self,
        first_vertice: int,
        second_vertice: int,
        edge_number: int,
    ) -> None:
        self.graph[first_vertice][edge_number] += 1
        self.graph[second_vertice][edge_number] += 1

    # Para remover a ligação entre dois vértices, precisamos fazer a mesma coisa da adição de arestas,
    # mas, dessa vez nós subtraímos os valores.
    def disconnect_edge(
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

    # Esse método irá iterar verticalmente por todas arestas para saber se algumas delas
    # liga os dois vértices em questão
    def get_edge(
        self,
        first_vertice: int,
        second_vertice: int,
    ) -> int:
        for edge in range(self.number_of_edges):
            if self.edge_exists(first_vertice, second_vertice, edge):
                return edge
        return -1

    # O grau do vértice é basicamente a quantidade de arestas que incidem sobre ele.
    # Isso é simples de encontrar em uma matriz de incidência, pois basta iterarmos
    # no vértice e procurar os elementos que são maiores do que 1
    # A soma final é o grau do vértice
    def get_vertice_degree(self, vertice) -> int:
        degree = 0
        for current_edge in self.graph[vertice]:
            degree += current_edge
        return degree

    # Para saber o grau do vértice, nós somamos o grau de todos os vértices
    def get_graph_degree(self) -> int:
        degree = 0
        for vertice in range(self.number_of_vertices):
            degree += self.get_vertice_degree(vertice)
        return degree

    # Um grafo tem loop quando pelo menos um vértice está ligado a si mesmo através de uma aresta
    # Isso é também chamado de laço
    # Um pouco parecido com o algoritmo de checar se existe arestas paralelas em uma matriz de adjacência
    def has_loop(self) -> bool:
        for vertice in range(self.number_of_vertices):
            for edge in range(self.number_of_edges):
                if self.graph[vertice][edge] > 1:
                    return True
        return False

    # Um grafo tem aresta paralela quando ao menos duas arestas possuem o mesmo par de vértices
    def has_parallel_edges(self) -> bool:
        for edge in range(self.number_of_edges):
            previous_vertice_edges = []
            for previous_vertice in range(self.number_of_vertices):
                previous_vertice_edges.append(self.graph[previous_vertice][edge])

            for next_edge in range(edge + 1, self.number_of_edges):
                next_vertice_edge = []
                for next_vertice in range(self.number_of_vertices):
                    next_vertice_edge.append(self.graph[next_vertice][next_edge])
                
                if previous_vertice_edges == next_vertice_edge:
                    return True
        return False

    # Um grafo é simples quando não possui loops, nem arestas paralelas
    def is_simple(self):
        return not (self.has_loop() or self.has_parallel_edges())


def main():
    graph = IncidenceMatrix(number_of_edges=3, number_of_vertices=4)
    graph.connect_edge(0, 2, 2)
    print(graph.has_parallel_edges())
    graph.connect_edge(0, 1, 0)
    print(graph.has_parallel_edges())
    print(graph.get_vertice_degree(1))
    graph.show_graph()


if __name__ == "__main__":
    main()
