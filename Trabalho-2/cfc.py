from grafo import GrafoDirigido, ler_arquivo
from buscaProfundidade import buscaProfundidade


def CFC(grafo: GrafoDirigido):
    C, T, A, F= buscaProfundidade(grafo, grafo.vertices())
    F_decrescente = list(key for key, value in sorted(F.items(), key=lambda item: item[1], reverse=True))
    grafo.inverter_arestas()
    Ct, Tt, At, Ft = buscaProfundidade(grafo, F_decrescente)

    return At



def calcular_componentes(antecessores: dict[int, int | None]):
    """
    Aplica um algoritmo similar ao Kruskel para determinar os
    conjuntos de vértices das componentes com base no mapa
    de antecessores.
    """

    componentes = {v: {v,} for v in antecessores.keys()}

    for v, u in antecessores.items():
        if u is None:
            continue
    
        componente_v = componentes[v]
        componente_u = componentes[u]

        if componente_v is not componente_u:
            x = componente_v.union(componente_u)
            for y in x:
                componentes[y] = x
    
    # percorrer as componentes de cada vértice e juntar em
    # uma lista sem componentes duplicados.
    resultado = []
    for componente in componentes.values():
        if componente not in resultado:
            resultado.append(componente)
    
    return resultado


if __name__ == "__main__":
    grafo = ler_arquivo("entrada.txt")
    antecessores = CFC(grafo)
    componentes = calcular_componentes(antecessores)

    print(
        "\n".join(
            ",".join(str(v) for v in componente)
            for componente in componentes
        )
    )



# '''
# CFC: componentes fortemente conexas
# Entrada: grafo G
# Saída: lista de componentes fortemente conectados
# 1. Chama DFS(G) para calcular os tempos de término T[u] para cada vértice u
# 2. Computa Gt - grafo transposto (arestas invertidas)
# 3. Chama DFS(Gt), mas no laço principal do DFS, considera os vértices em ordem decrescente de T[u]
# 4. Dar saída aos vértices de cada árvore da floresta DFS como uma CFC separada
# '''

# def CFC(grafo: GrafoDirigido):
#     visitados = set()
#     pilha = []

#     for v in grafo.vertices():
#         if v not in visitados:
#             buscaProfundidade(grafo, v, visitados, pilha)
    
#     grafo_transposto = GrafoDirigido()
#     for u, v, _ in grafo.arestas():
#         grafo_transposto.adicionar_aresta(v, u, 0)

#     visitados.clear()
#     componentes = []

#     while pilha:
#         v = pilha.pop()
#         if v not in visitados:
#             componente = []
#             buscaProfundidade(grafo_transposto, v, visitados, componente)
#             componentes.append(componente)
#     return componentes

# if __name__ == "__main__":
#     grafo = ler_arquivo("entrada.txt")
#     componentes = CFC(grafo)
#     print(componentes)