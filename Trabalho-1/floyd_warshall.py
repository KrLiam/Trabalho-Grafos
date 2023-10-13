from grafo import Grafo


def W(grafo: Grafo, u, v):
    if u == v:
        return 0
    if grafo.peso(u, v):
        return grafo.peso(u, v)
    return float("inf")


def floyd_warshall(grafo: Grafo):
    D_anterior = {}
    D = {v: {u: W(grafo, u, v) for u in grafo.vertices()} for v in grafo.vertices()}

    for k in grafo.vertices():
        D, D_anterior = D_anterior, D
        for u in grafo.vertices():
            for v in grafo.vertices():
                D_u = D.setdefault(u, {})
                D_u[v] = min(D_anterior[u][v], D_anterior[u][k] + D_anterior[k][v])

    return D


if __name__ == "__main__":
    grafo = Grafo.ler_arquivo("entrada.txt")

    D = floyd_warshall(grafo)

    for v in grafo.vertices():
        linha = ",".join(str(x) for x in D[v].values())
        print(f"{v}: {linha}")
