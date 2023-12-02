from grafo import Grafo


def dfs(grafo: Grafo,X:list[int],Y:list[int], mate:dict[int,int], x:int, D: dict[int,str], ) -> tuple[dict[int, int], dict[int, int]]:


    if x != 0:
        for y in grafo.vizinhos(x):
            if D[mate[y]] == D[x]+1:
                if dfs(grafo,X,Y,mate,mate[y],D):
                    mate[y] = x
                    mate[x] = y
                    return True
        D[x] = "inf"
        return False
    return True












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

    for u in ordem:
        if u not in C:
            dfs_visit(u)




    return C, T, A, F


