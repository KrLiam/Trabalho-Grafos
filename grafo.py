
from dataclasses import dataclass


@dataclass(frozen=True)
class Vertice:
  rotulo: str
  index: int


class Grafo:
    mapa_vizinhos: dict[Vertice, set[Vertice]]
    mapa_pesos: dict[frozenset[Vertice], float]




    @classmethod
    def ler_arquivo(self, file_name):

        vertices = {}
        with open(file_name, 'r') as arquivo:
            ler_vertices = False
            ler_arestas = False

            for linha in arquivo:
                linha = linha.strip()
                
                if linha.startswith('*vertices'):
                    ler_vertices = True
                    continue
                
                if ler_vertices:
                    partes = linha.split()
                    if len(partes) == 2:
                        index, rotulo = partes
                        vertice = Vertice(rotulo, index)
                        vertices[index] = vertice
                
                if linha.startswith('*edges'):
                    ler_arestas = True
                    continue

                if ler_arestas:
                    partes = linha.split()
                    if len(partes) == 3:
                        u = vertices[partes[0]]
                        v = vertices[partes[1]]
                        w = float(partes[2])
                        grafo.adicionar_aresta(u, v, w)
        
        return grafo


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
