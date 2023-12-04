from grafo import GrafoDirigido, ler_arquivo

def EdmondsKarp(
    grafo: GrafoDirigido,
    s: int,
    t:int,
    grafo_residual: GrafoDirigido
) -> tuple[dict[int, int], dict[int, int]]:
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

def FordFulkerson(
    grafo: GrafoDirigido, s: int, t: int, grafo_residual: GrafoDirigido
) -> tuple[int, tuple[int, ...]]:
    F = 0
    caminhos = []

    while True:
        # Encontrar um caminho que não fora analisado ainda
        p = EdmondsKarp(grafo, s, t, grafo_residual)
        # print(f"caminho aumentante: {p}")
        if p == 0:
            break

        # Identificando a capacidade do caminho e adicionando-o ao fluxoi atual
        arestas = []
        for i in range(len(p) - 1):
            u = p[i]
            v = p[i + 1]
            arestas.append(grafo_residual.peso(u, v))

        fp = min(arestas)
        F += fp
        # print(f"fluxo aumentado em {fp}")
        caminhos.append(p)

        # Atualizando a capacidade residual
        for i in range(len(p) - 1):
            u = p[i]
            v = p[i + 1]

            grafo_residual.alterar_peso_aresta(u, v, grafo_residual.peso(u, v) - fp)
            grafo_residual.alterar_peso_aresta(v, u, grafo_residual.peso(v, u) + fp)

    return F, caminhos


if __name__ == "__main__":

    nome_arquivo = input("Arquivo de entrada: ")
    grafo = ler_arquivo(nome_arquivo, GrafoDirigido)
    grafo_residual = grafo.criar_grafo_residual()

    print("\nInforme numero dos vertices 'S' e 'T' (int num):")
    s = int(input("Vertice 'S': "))
    t = int(input("Vertice 'T': "))
    
    A = FordFulkerson(grafo, s, t, grafo_residual)
    print("Tamanho do fluxo:", A)
