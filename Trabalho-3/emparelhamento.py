from grafo import Grafo, GrafoBipartido, ler_arquivo


def bfs(
    grafo: Grafo,
    X:list[int],
    Y:list[int],
    mate:dict[int,int],
    D: dict[int,str]
) -> tuple[dict[int, int], dict[int, int]]:
    Q = []
    for x in X:
        if mate[x] == None:
            D[x] = 0
            Q.append(x)
        else:
            D[x] = float("inf")

    D[None] = float("inf")

    while Q:
        x = Q.pop(0)
        if D[x] < D[None]:
            for y in grafo.vizinhos(x):
                if D[mate[y]] == float("inf"):
                    D[mate[y]] = D[x]+1
                    Q.append(mate[y])

    return D[None] != float("inf")


def dfs(
    grafo: Grafo,
    X:list[int],
    Y:list[int],
    mate:dict[int,int],
    x:int,
    D: dict[int,str]
) -> tuple[dict[int, int], dict[int, int]]:
    if x != None:
        for y in grafo.vizinhos(x):
            if D[mate[y]] == D[x]+1:
                if dfs(grafo,X,Y,mate,mate[y],D):
                    mate[y] = x
                    mate[x] = y
                    return True
        D[x] = float("inf")
        return False
    return True


def HopcroftKarp(
    grafo: Grafo, X: set[int], Y: set[int]
) -> tuple[int, dict[int, None|int]]:
    D = {v: float("inf") for v in grafo.vertices()}
    mate = {v: None for v in grafo.vertices()}

    #tamanho do emparelhamento
    m = 0   
    while bfs(grafo,X,Y,mate,D):
        for x in X:
            if mate[x] == None:
                if dfs(grafo,X,Y,mate,x,D):
                    m += 1
    return (m,mate)


def main():
    nome_arquivo = input("Arquivo de entrada: ")
    grafo = ler_arquivo(nome_arquivo, GrafoBipartido)

    X = grafo.verticesX()
    Y = grafo.verticesY()

    X_fmt = ','.join(str(n) for n in X)
    Y_fmt = ','.join(str(n) for n in Y)
    print(F"X={X_fmt}\nY={Y_fmt}")

    while True:
        value = input("Deseja-se utilizar estes conjuntos de X e Y? [S/n]: ")

        if not value:
            value = "s"

        if value.strip().lower() in ("s", "n"):
            result = value == "s"
            break
    
    if not result:
        print("Digite os conjuntos de vértices separados por espaços. Exemplo: 1 3 5 7")
        X = [int(n) for n in input("X: ").strip().split()]
        Y = [int(n) for n in input("Y: ").strip().split()]

    m, mate = HopcroftKarp(grafo, X, Y)
    
    arestas = set(frozenset(pair) for pair in mate.items())
    print("Emparelhamento máximo:", m)
    print("Arestas:", ", ".join(f"{u}-{v}" for u, v in arestas))


if __name__ == "__main__":
    main()