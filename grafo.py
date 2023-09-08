
from dataclasses import dataclass


@dataclass(frozen=True)
class Vertice:
  rotulo: str



class Grafo:
    mapa_vizinhos: dict[Vertice, set[Vertice]]
    mapa_pesos: dict[frozenset[Vertice], float]

    @classmethod
    def ler_arquivo(cls, nome: str):
        ...

    def __init__(self):
        self.mapa_vizinhos = {}
        self.mapa_pesos = {}

    def qtdVertices(self, ):
        return len(self.mapa_vizinhos)
    
    def qtdArestas(self, ):
        return len(self.mapa_pesos)
    
    def grau(self, v):
        return len(self.mapa_vizinhos.get(v, set()))
    
    def rotulo(self, v):
        return v.rotulo
    
    def vizinhos(self, v):
        return self.mapa_vizinhos.get(v, set())
    
    def hasAresta(self, u, v):
        return frozenset({u, v}) in self.mapa_pesos
    
    def peso(self, u, v):
        return self.mapa_pesos.get(frozenset({u, v}), 0)

    def adicionar_aresta(self, u, v, w):
        key = frozenset({u, v})
        self.mapa_pesos[key] = w

        if u not in self.mapa_vizinhos:
            self.mapa_vizinhos[u] = set()
        self.mapa_vizinhos[u].add(v)

        if v not in self.mapa_vizinhos:
            self.mapa_vizinhos[v] = set()
        self.mapa_vizinhos[v].add(u)

