from grafo import Grafo


def EdmondsKarp(grafo: Grafo, s: int, t:int, grafo_residual: Grafo) -> tuple[dict[int, int], dict[int, int]]:
    #Configurando todos os vertices
    C = set()
    A = {v: None for v in grafo.vertices()}

    #Configurando o verticie de origem
    C.add(s)

    #Preparando fila de visitas
    Q = [s]

    #Propagacao das visitas
    while Q:
        u = Q.pop(0)

        for v in grafo.vizinhos(u):
            if (v not in C) and (grafo_residual.peso(u, v) > 0):
                C.add(v)
                A[v] = u

                #Sorvedouro encontrado. Criar caminho aumentante
                if v == t:
                    p = [t]
                    w = t
                    while w != s:
                        w = A[w]
                        p.insert(0,w)
                    return p
                Q.append(v)

    return  0
