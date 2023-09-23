from grafo import Grafo
from heapq import heappop, heappush


def dijkstra(grafo: Grafo, s: int) -> tuple[dict[int, int], dict[int, int]]:
    D = {v: float("inf") for v in grafo.vertices()}
    A = {}
    C = {}
    
    D[s] = 0
    A[s] = None
    restantes = [(D[s], s)]

    while restantes:
        u_dist, u = heappop(restantes)

        if C.get(u):
            continue
        C[u] = True

        for v in grafo.vizinhos(u):
            if C.get(v):
                continue

            dist = u_dist + grafo.peso(u, v)
            if D[v] > dist:
                D[v] = dist
                A[v] = u
                heappush(restantes, (dist, v))

    return D, A


if __name__ == "__main__":
    grafo = Grafo.ler_arquivo("entrada.txt")

    D, A = dijkstra(grafo, 1)

    for v in grafo.vertices():
        caminho = [v]

        u = A[v]
        while u is not None:
            caminho.append(u)
            u = A[u]

        caminho_str = ",".join(str(i) for i in reversed(caminho))
        print(f"{v}: {caminho_str}; d={D[v]}")
