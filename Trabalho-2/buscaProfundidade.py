from grafo import Grafo


def buscaProfundidade(grafo: Grafo, s: int) -> tuple[dict[int, int], dict[int, int]]:
    C = set()
    T = {v: float("inf") for v in grafo.vertices()}
    A = {v: None for v in grafo.vertices()}

    C.add(s)
    tempo = 0
    S = [s]

    while S:
        tempo += 1
        u = S.pop(len(S)-1)
        T[u] = tempo

        for v in grafo.vizinhos(u):
            if v not in C:
                A[v] = u
                S.append(v)
                C.add(v)

    return C,T, A


if __name__ == "__main__":
    grafo = Grafo.ler_arquivo("entrada.txt")

    C,T, A = buscaProfundidade(grafo, 1)
    for v in grafo.vertices():
        caminho = [v]
    
        u = A[v]
        while u is not None:
            caminho.append(u)
            u = A[u]

        caminho_str = ",".join(str(i) for i in reversed(caminho))
        print(f"{v}: {caminho_str}")
        print(T[v])
