from itertools import combinations
from random import shuffle
from time import sleep
from typing import Generator, Iterable, TypeVar

from grafo import Grafo, ler_arquivo


T = TypeVar("T")


def conjunto_potencia(
    conjunto: set[T], decrescente: bool = False
) -> Generator[frozenset[T], None, None]:
    if not decrescente:
        yield frozenset()

    ordem = range(len(conjunto), 0, -1) if decrescente else range(1, len(conjunto) + 1)
    for n in ordem:
        for subset in combinations(conjunto, n):
            yield frozenset(subset)

    if decrescente:
        yield frozenset()


def get_I(
    vertices: frozenset[int], arestas: set[frozenset[int]]
) -> set[frozenset[int]]:
    R = set()

    # para cada subconjunto X dos vertices do grafo, em ordem crescente de tamanho
    for X in conjunto_potencia(vertices):
        # testa se nenhum par de vértices u, v em X possui uma aresta
        if not any(frozenset((u, v)) in arestas for u in X for v in X):
            # remover todos os subconjuntos de X
            R.difference_update(conjunto_potencia(X))
            # adiciona conjunto X
            R.add(X)

    return R


def filtrar_arestas(arestas: Iterable[Iterable[int]], subvertices: set[int]):
    """
    Retorna o subconjunto de arestas compostas apenas por vértices que
    pertencem ao conjunto `subvertices` fornecido.
    """
    return {
        frozenset((u, v)) for u, v in arestas if u in subvertices and v in subvertices
    }


def lawler_recursivo(
    vertices: set[int],
    arestas: set[frozenset[int]],
    cims: tuple[frozenset[int], ...] = (),
):
    """
    Implementação do algoritmo de Lawler baseada na recorrência.
    Retorna tanto o número cromático como uma tupla contendo os conjuntos
    de vértices de mesma cor.
    """
    
    if not len(vertices):
        return (0, cims)

    c, conjs = min(
        lawler_recursivo(
            V := vertices - I, filtrar_arestas(arestas, V), cims + (I,)
        )
        for I in get_I(vertices, arestas)
    )
    return (c + 1, conjs)


def lawler(grafo: Grafo) -> int:
    """
    Algoritmo 34 da apostila. Este algoritmo não foi utilizado, pois
    a implementação baseada na recorrência é mais eficiente.
    """

    X = {}

    X[hash(frozenset())] = 0

    # subconjuntos em ordem crescente de tamanho
    subsets = conjunto_potencia(grafo.vertices())
    # descarta o conjunto vazio
    next(subsets)

    # para cada subconjunto restante
    for S in subsets:
        s = hash(S)
        X[s] = float("inf")

        for I in get_I(S, filtrar_arestas(grafo.arestas(), S)):
            i = hash(S - I)

            if X[i] + 1 < X[s]:
                X[s] = X[i] + 1

    # retorna o valor em X do último subconjunto
    return X[hash(S)]


def mostrar_coloracao(grafo: Grafo, interval=None):
    import networkx as nx
    from matplotlib.colors import get_named_colors_mapping
    import matplotlib.pyplot as plt

    print("Mostrando grafo...")

    CORES = [
        "red",
        "blue",
        "green",
        "yellow",
        "cyan",
        "magenta",
        "darkblue",
        "darkred",
        "violet",
        "brown",
        "pink",
        "teal",
        "darkviolet",
        "olive",
        "lightblue",
        "lime",
    ]
    _extra_colors = [c for c in get_named_colors_mapping() if c not in CORES]
    shuffle(_extra_colors)
    CORES.extend(_extra_colors)

    ng = nx.Graph()
    ng.add_nodes_from(grafo.vertices())
    ng.add_edges_from(grafo.arestas())

    pos = nx.spring_layout(ng)

    if interval is None:
        interval = 1 / max(1, grafo.qtdVertices())

    cores = {}

    _, grupos = lawler_recursivo(grafo.vertices(), grafo.arestas())
    fig = plt.figure(layout="tight")
    ax = fig.add_subplot(111)

    plt.show(block=False)

    for i, grupo in enumerate(grupos):
        for v in grupo:
            cores[v] = CORES[i]

            ax.clear()
            nx.draw_networkx_nodes(
                ng,
                pos,
                ax=ax,
                node_color=[cores.get(u, "black") for u in ng],
            )
            nx.draw_networkx_edges(ng, pos, ax=ax, alpha=0.25)
            nx.draw_networkx_labels(ng, pos, ax=ax, font_color="white")

            fig.canvas.draw()
            fig.canvas.flush_events()

            sleep(interval)

    plt.show()


if __name__ == "__main__":
    nome_arquivo = input("Arquivo de entrada: ")
    g = ler_arquivo(nome_arquivo, Grafo)

    print("Determinando número cromático do grafo...")
    numero_cromatico, _ = lawler_recursivo(g.vertices(), g.arestas())
    print(f"Número cromático: {numero_cromatico}")

    try:
        mostrar_coloracao(g)
    except ImportError as err:
        print(f"Instale o modulo {err.name} para ver o grafo :D") 
