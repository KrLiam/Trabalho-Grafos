from grafo import GrafoDirigido, ler_arquivo


def dfs_ord(grafo: GrafoDirigido) -> tuple[dict[int, int], dict[int, int]]:
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


    for u in grafo.vertices():
        if u not in C:
            dfs_visit(u)

    return F, T, A
            

if __name__ == "__main__":
    grafo = ler_arquivo("Trabalho-2/entrada.txt")

    F, T, A = dfs_ord(grafo)

    for v in grafo.vertices():
        caminho = [v]
    
        u = A[v]
        while u is not None:
            caminho.append(u)
            u = A[u]


        caminho_str = ",".join(str(i) for i in reversed(caminho))
        print(f"{v}: {caminho_str}")
        print(f"Inicio: {T[v]} - Fim: {F[v]}")
