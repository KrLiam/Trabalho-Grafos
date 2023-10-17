from grafo import GrafoDirigido


def buscaProfundidade(grafo: GrafoDirigido, ordem) -> tuple[dict[int, int], dict[int, int]]:
    C = set()
    T = {v: float("inf") for v in grafo.vertices()}
    F = {v: float("inf") for v in grafo.vertices()}
    A = {v: None for v in grafo.vertices()}
    
    tempo = 0

    def dfs_visit(v):
        nonlocal tempo

        C.add(v)
        tempo += 1
        T[v] = tempo

        for u in grafo.vizinhos(v):
            if u not in C:
                A[u] = v
                dfs_visit(u)

        tempo += 1
        F[v] = tempo

    for u in ordem:
        if u not in C:
            dfs_visit(u)




    return C, T, A, F


