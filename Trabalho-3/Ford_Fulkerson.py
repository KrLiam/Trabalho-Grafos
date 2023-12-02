from grafo import GrafoDirigido, ler_arquivo
from Edmonds_Karp import EdmondsKarp


def FordFulkerson(
    grafo: GrafoDirigido, s: int, t: int, grafo_residual: GrafoDirigido
) -> tuple[int, tuple[int, ...]]:
    F = 0
    caminhos = []

    while True:
        # Encontrar um caminho que não fora analisado ainda
        p = EdmondsKarp(grafo, s, t, grafo_residual)
        # print(f"caminho aumentante: {p}")
        if p == 0:
            break

        # Identificando a capacidade do caminho e adicionando-o ao fluxoi atual
        arestas = []
        for i in range(len(p) - 1):
            u = p[i]
            v = p[i + 1]
            arestas.append(grafo_residual.peso(u, v))

        fp = min(arestas)
        F += fp
        # print(f"fluxo aumentado em {fp}")
        caminhos.append(p)

        # Atualizando a capacidade residual
        for i in range(len(p) - 1):
            u = p[i]
            v = p[i + 1]

            grafo_residual.alterar_peso_aresta(u, v, grafo_residual.peso(u, v) - fp)
            grafo_residual.alterar_peso_aresta(v, u, grafo_residual.peso(v, u) + fp)

    return F, caminhos


def mostrar_grafo(grafo: GrafoDirigido):
    import networkx as nx
    import matplotlib.pyplot as plt

    ng = nx.DiGraph()
    ng.add_nodes_from(grafo.vertices())
    ng.add_edges_from(grafo.arestas())

    pos = nx.spring_layout(ng)

    fig = plt.figure(layout="tight")
    ax = fig.add_subplot(111)

    plt.show(block=False)
    nx.draw_networkx_nodes(
        ng,
        pos,
        ax=ax,
        node_color="black",
    )
    nx.draw_networkx_edges(ng, pos, ax=ax, alpha=1)
    nx.draw_networkx_labels(ng, pos, ax=ax, font_color="white")

    plt.show()


if __name__ == "__main__":
    grafo = ler_arquivo("wiki.net")

    # Pedi pro chat gpt fazer essa funcao do grafo residual, entao nao sei se ta funcionando como devia
    grafo_residual = grafo.criar_grafo_residual()

    # Eu não sei como mandar pra função o ultimo vértice do grafo, o vertice t, por isso mandei 100 por enquanto 😁
    A = FordFulkerson(grafo, 1, 7, grafo_residual)
    print(A)
