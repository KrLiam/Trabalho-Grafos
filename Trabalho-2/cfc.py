from grafo import GrafoDirigido, ler_arquivo
from buscaProfundidade import buscaProfundidade

'''
CFC: componentes fortemente conexas
Entrada: grafo G
Saída: lista de componentes fortemente conectados
1. Chama DFS(G) para calcular os tempos de término T[u] para cada vértice u
2. Computa Gt - grafo transposto (arestas invertidas)
3. Chama DFS(Gt), mas no laço principal do DFS, considera os vértices em ordem decrescente de T[u]
4. Dar saída aos vértices de cada árvore da floresta DFS como uma CFC separada
'''

def CFC(grafo: GrafoDirigido):
    visitados = set()
    pilha = []

    for v in grafo.vertices():
        if v not in visitados:
            buscaProfundidade(grafo, v, visitados, pilha)
    
    grafo_transposto = GrafoDirigido()
    for u, v, _ in grafo.arestas():
        grafo_transposto.adicionar_aresta(v, u, 0)

    visitados.clear()
    componentes = []

    while pilha:
        v = pilha.pop()
        if v not in visitados:
            componente = []
            buscaProfundidade(grafo_transposto, v, visitados, componente)
            componentes.append(componente)
    return componentes

if __name__ == "__main__":
    grafo = ler_arquivo("entrada.txt")
    componentes = CFC(grafo)
    print(componentes)