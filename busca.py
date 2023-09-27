from grafo import Grafo

def buscaLargura (grafo: Grafo, s: int) -> tuple[dict[int, int], dict[int, int]]:
    C = set()
    D = {v: float("inf") for v in grafo.vertices()}
    A = {v: None for v in grafo.vertices()}

    D[s] = 0
    C.add(s)
    Q = [s]

    while Q:
        u = Q.pop(0)

        for v in grafo.vizinhos(u):
            if v not in C:
                D[v] = D[u] + 1
                A[v] = u
                Q.append(v)
                C.add(v)

    return D, A


if __name__ == "__main__":
    grafo = Grafo.ler_arquivo("entrada.txt")

    D, A = buscaLargura(grafo, 1)
    for v in grafo.vertices():
        caminho = [v]

        u = A[v]
        while u is not None:
            caminho.append(u)
            u = A[u]
            # print(u)

        caminho_str = ",".join(str(i) for i in reversed(caminho))
        print(f"{v}: {caminho_str}")