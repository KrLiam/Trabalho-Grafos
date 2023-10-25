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


def main():
    grafo = ler_arquivo("entrada.txt")
    
    if not isinstance(grafo, GrafoDirigido):
        print("Entrada é inválida. Espera-se um grafo dirigido ✨")
        return

    antecessores = CFC(grafo)
    componentes = calcular_componentes(antecessores)

    print(
        "\n".join(
            ",".join(str(v) for v in componente)
            for componente in componentes
        )
    )

if __name__ == "__main__":
    main()