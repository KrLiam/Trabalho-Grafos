from grafo import Grafo


def bfs(grafo: Grafo,X:list[int],Y:list[int], mate:dict[int,int], D: dict[int,str], ) -> tuple[dict[int, int], dict[int, int]]:

    Q = []
    for x in X:
        if mate[x] == 0:
            D[x] = 0
            Q.append(x)
        else:
            D[x] = "inf"

    D[0] = "inf"

    while Q:
        x = Q.pop(0)
        if D[x] < D[0]:
            for y in grafo.vizinhos(x):
                if D[mate[y]] == "inf":
                    D[mate[y]] = D[x]+1
                    Q.append(mate[y])

    return D[0] != "inf"
