from grafo import Grafo, ler_arquivo
from heapq import heappop, heappush, heapify


def prim(grafo: Grafo):
    r, *_ = grafo.vertices()

    A = {v: None for v in grafo.vertices()}
    K = {v: float("inf") for v in grafo.vertices()}

    K[r] = 0
    
    Q = [(K[v], v) for v in grafo.vertices()]
    heapify(Q)

    visitados = set()

    while len(Q):
        _, u = heappop(Q)

        if u in visitados:
            continue
        visitados.add(u)
        
        for v in grafo.vizinhos(u):
            peso = grafo.peso(u, v)

            if v not in visitados and peso < K[v]:
                A[v] = u
                K[v] = peso
                heappush(Q, (peso, v))

    return A


if __name__ == "__main__":
    grafo = ler_arquivo("entrada.txt")

    A = prim(grafo)
    somatorio = 0
    lista = []

    for k, v in A.items():
        if v == None:
            continue
        somatorio += grafo.peso(k,v)
        lista.append((str(k)+"-"+str(v)))

    print(somatorio)
    print(', '.join(lista))
        

        

