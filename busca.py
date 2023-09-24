from grafo import Grafo

def buscaLargura (grafo: Grafo, s: int) -> tuple[dict[int, int], dict[int, int]]:
    C = {v: False for v in grafo.vertices()}
    D = {v: float("inf") for v in grafo.vertices()}
    A = {v: None for v in grafo.vertices()}
    D[s] = 0
    Q = []
    Q.append(s)
    while len(Q) > 0:
        u = Q.pop(0)
        for v in grafo.vizinhos(u):
            if C[v] == False:
                C[v] = True
                D[v] = D[u] + 1
                A[v] = u
                Q.append(v)
    return D, A