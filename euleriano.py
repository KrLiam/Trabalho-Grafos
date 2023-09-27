from grafo import Grafo


def hierholzer(grafo: Grafo) -> tuple[dict[int, int], dict[int, int]]:
    C = set()
    v, *_ = grafo.vertices()

    r, ciclo = BuscaCiclo(grafo, v, C)

    if not r or len(C) < len(grafo.arestas()):
        return (False, None)

    return (True, ciclo)


def BuscaCiclo(grafo, v, C):
    ciclo = [v]
    t = v

    while True:
        arestas = []
        for u in grafo.vizinhos(v):
            aresta = frozenset({v, u})

            if aresta not in C:
                arestas.append(aresta)

        if not arestas:
            return (False, None)

        aresta, *_ = arestas
        a, b = aresta
        v = b if a == v else a

        C.add(aresta)
        ciclo.append(v)

        if v == t:
            break

    for x in ciclo:
        if any(frozenset({x, w}) not in C for w in grafo.vizinhos(x)):
            r, subciclo = BuscaCiclo(grafo, x, C)
            if not r:
                return (False, None)

            i = ciclo.index(x)
            ciclo = ciclo[:i] + subciclo + ciclo[i + 1 :]

    return (True, ciclo)


if __name__ == "__main__":
    grafo = Grafo.ler_arquivo("entrada.txt")

    r, ciclo = hierholzer(grafo)

    print(int(r))
    if r:
        print(",".join(str(x) for x in ciclo))
