
from itertools import combinations
from math import ceil
from random import shuffle
from time import sleep
from typing import Any, Generator, Iterable, TypeVar

from matplotlib.colors import get_named_colors_mapping
from grafo import Grafo, ler_arquivo


T = TypeVar("T")
def conjunto_potencia(conjunto: set[T], decrescente: bool = False) -> set[frozenset[T]]:
    if not decrescente:
        yield frozenset()

    ordem = range(len(conjunto), 0, -1) if decrescente else range(1, len(conjunto) + 1)
    for n in ordem:
        for subset in combinations(conjunto, n):
            yield frozenset(subset)

    if decrescente:
        yield frozenset()


def get_I(vertices: frozenset[int], arestas: set[frozenset[int]]) -> set[frozenset[int]]:
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

def lawler_recursivo(grafo: Grafo):
    def d(S: frozenset[int], arestas: set[frozenset[int]], cims: tuple[frozenset[int], ...] = ()):
        if not len(S):
            return (0, cims)
        
        c, conjs = min(
            d(Si := S - I, filtrar_arestas(arestas, Si), cims + (I,))
            for I in get_I(S, arestas)
        )

        return (c + 1, conjs)

    return d(grafo.vertices(), grafo.arestas())


def lawler(grafo: Grafo):
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


def coloracao(grafo: Grafo, k_cores: int) -> Generator[tuple[int, int], None, None]:
    vertices = sorted(grafo.vertices(), key=lambda v: -grafo.grau(v))

    cores = {}

    for v in vertices:
        cores_vizinhos = {cor for u in grafo.vizinhos(v) if (cor := cores.get(u))}

        for c in range(1, k_cores+1):
            if c not in cores_vizinhos:
                cores[v] = c
                yield v, c

                break
    
    return cores


def numero_cromatico(grafo: Grafo):
    num_vertices = grafo.qtdVertices()

    c = 0
    def partition(min_k, max_k):
        nonlocal c
        c += 1
        if c > 50:
            return 0

        if min_k == max_k:
            return min_k

        k = (min_k + max_k) // 2
        print(f"{min_k=}, {max_k=}, {k=}")
        num_colorido = len([*coloracao(grafo, k)])
        print(f"{num_colorido=}")

        if num_colorido >= num_vertices:
            return partition(min_k, k)
        else:
            return partition(k+1, max_k)
    
    return partition(0, num_vertices)



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


def mostrar_coloracao(grafo: Grafo, k_cores=None, interval=None):
    import networkx as nx
    import matplotlib.pyplot as plt

    ng = nx.Graph()
    ng.add_nodes_from(grafo.vertices())
    ng.add_edges_from(grafo.arestas())

    pos = nx.spring_layout(ng)

    if interval is None:
        interval = 1 / max(1, grafo.qtdVertices())

    cores = {}

    print("Determinando número cromático do grafo...")
    _, grupos = lawler_recursivo(grafo)
    print(f"k = {len(grupos)}")

    fig = plt.figure(layout="tight")
    ax = fig.add_subplot(111)

    plt.show(block=False)

    for i, grupo in enumerate(grupos):
        for v in grupo:
            cores[v] = CORES[i]
            print(f"Coloriu vértice {v} com {cores[v]}")

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
    g = ler_arquivo("cor4.net")

    print(lawler(g))
    # mostrar_coloracao(g)