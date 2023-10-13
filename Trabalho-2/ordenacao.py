from grafo import GrafoDirigido, ler_arquivo


def dfs_ord(grafo: GrafoDirigido) -> tuple[dict[int, int], dict[int, int]]:
    C = set()
    T = {v: float("inf") for v in grafo.vertices()}
    F = {v: float("inf") for v in grafo.vertices()}
    
    tempo = 0
    O = []

    def dfs_visit(v):
        nonlocal tempo

        C.add(v)
        tempo += 1
        T[v] = tempo

        for u in grafo.vizinhos(v):
            if u not in C:
                dfs_visit(u)

        tempo += 1
        F[v] = tempo
        O.insert(0,v)


    for u in grafo.vertices():
        if u not in C:
            dfs_visit(u)

    return O
            

if __name__ == "__main__":
    grafo = ler_arquivo("entrada.txt")

    O = dfs_ord(grafo)

    print(" -> ".join(grafo.rotulo(v) for v in O))
