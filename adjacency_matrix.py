class AdjacencyMatrix:
    # Em um grafo representado por uma matriz de adjacência, colunas e linhas são
    # vértices.
    def __init__(self, number_of_vertices: int) -> None:
        self.number_of_vertices = number_of_vertices
        self.graph = [
            [0] * self.number_of_vertices for _ in range(self.number_of_vertices)
        ]

    def show_graph(self):
        for vertice in self.graph:
            print(vertice)

    # Para adicionar uma aresta em um grafo de adjacência, precisamos receber como parâmetro
    # dois vértices. Dessa forma, o primeiro vértice irá acessar a linha e o segundo vértice
    # irá acessar a coluna.
    def add_edge(self, first_vertice, second_vertice):
        self.graph[first_vertice - 1][second_vertice - 1] += 1

        # Essa segunda linha é importante, pois estamos lidando com um
        # grafo não direcionado, ou seja, se o primeiro vértice está conectado
        # ao segundo vértice. O contrário também vale, dessa forma, a segunda
        # linha garante a simetria
        self.graph[second_vertice - 1][first_vertice - 1] += 1

    # De forma análoga à adição, acessamos os vértices como se tivéssemos adicionando, mas
    # ao invés de somar um, nós subtraímos
    def remove_edge(self, first_vertice, second_vertice):
        self.graph[first_vertice - 1][second_vertice - 1] -= 1

        # Essa linha de código só é necessária caso o grafo seja não direcionado
        self.graph[second_vertice - 1][first_vertice - 1] -= 1

    # Para checar se um vértice existe, basta acessarmos o vértice e checar se o valor
    # da célula é maior do que 0
    def edge_exists(self, first_vertice, second_vertice):
        return (
            self.graph[first_vertice - 1][second_vertice - 1] > 0
            and self.graph[second_vertice - 1][first_vertice - 1] > 0
        )

    # Como as linhas e colunas são vértices, para obter o grau de um vértice, basta acessarmos
    # o vértice, iterar sobre a lista e checar por valores maiores do que 0
    def get_vertice_degree(self, vertice):
        vertice_degree = 0
        current_vertice = self.graph[vertice - 1]
        for i in range(self.number_of_vertices):
            vertice_degree += current_vertice[i]
        return vertice_degree

    # De forma análoga a pegar o grau de um vértice, para obter o grau de um grafo, basta somar
    # o grau de todos os vértices.
    # Dessa maneira, precisamos passar por todos os vértices do grafo e somar o grau de cada um
    def get_graph_degree(self):
        graph_degree = 0
        for i in range(self.number_of_vertices):
            graph_degree += self.get_vertice_degree(i)
        return graph_degree

    # Loops são arestas para um mesmo vértice. Para checar isso, precisamos analisar a diagonal principal,
    # se existe um vértice na diagonal principal que possui algum valor diferente de zero (> 0), então
    # temos um loop
    def has_loop(self):
        for i in range(self.number_of_vertices):
            if self.graph[i][i] > 0:
                return True
        return False

    # Arestas paralelas são aquelas que possuem o mesmo par de vértices.
    # Dessa forma, se tivermos um vertice 1 conectado a 2, e um vértice 2 conectado a 1, nós temos uma aresta
    # paralela.
    # Um pouco parecido com o algoritmo de checar se existe loop em uma matriz de incidência
    def has_parallel_edge(self):
        for i in range(self.number_of_vertices):
            for j in range(i + 1, self.number_of_vertices):
                if self.graph[i][j] > 1:
                    print(f"Achei uma aresta paralela em {i + 1} e {j + 1}")
                    return True
        return False

    # Um grafo é simples quando não possue loops e arestas paralelas.
    def is_simple(self):
        return not (self.has_loop() or self.has_parallel_edge())


def main():
    grafo = AdjacencyMatrix(4)
    grafo.add_edge(1, 2)
    grafo.add_edge(2, 1)
    grafo.add_edge(1, 3)
    grafo.add_edge(3, 1)
    grafo.add_edge(1, 4)
    grafo.add_edge(2, 2)
    print(grafo.has_parallel_edge())
    print(grafo.get_vertice_degree(1))
    print(grafo.get_graph_degree())
    print(grafo.has_loop())
    print(grafo.is_simple())
    grafo.show_graph()


if __name__ == "__main__":
    main()
