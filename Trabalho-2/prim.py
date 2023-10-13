from grafo import Grafo
from heapq import heappop, heappush


def prim(grafo: Grafo, s: int):
    r, *_ = grafo.vertices()
    A = {v: None for v in grafo.vertices()}
    K = {v: float("inf") for v in grafo.vertices()}
    K[r] = 0
    Q = [(K[v], v) for v in grafo.vertices()]


    return A

