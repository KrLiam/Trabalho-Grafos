
from dataclasses import dataclass


@dataclass(frozen=True)
class Vertice:
  rotulo: str
  index: int

@dataclass(init=False)
class Grafo:
    vertices: dict[int, Vertice]
    mapa_vizinhos: dict[Vertice, set[Vertice]]
    mapa_pesos: dict[frozenset[Vertice], float]

    @classmethod
    def ler_arquivo(self, file_name):
        grafo = Grafo()

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
                        grafo.adicionar_vertice(rotulo, int(index))
                
                if linha.startswith('*edges'):
                    ler_arestas = True
                    continue

                if ler_arestas:
                    partes = linha.split()
                    if len(partes) == 3:
                        u = grafo.vertice(int(partes[0]))
                        v = grafo.vertice(int(partes[1]))
                        w = float(partes[2])
                        grafo.adicionar_aresta(u, v, w)
        
        return grafo


    def __init__(self):
        self.vertices = {}
        self.mapa_vizinhos = {}
        self.mapa_pesos = {}

    def qtdVertices(self, ):
        return len(self.vertices)
    
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

    def vertice(self, index):
        return self.vertices[index]

    def adicionar_vertice(self, rotulo, index):
        if index in self.vertices:
            raise ValueError(f"Vertice with index {index} already exists.")

        vertice = Vertice(rotulo, index)
        self.vertices[index] = vertice
        self.mapa_vizinhos[vertice] = set()

    def adicionar_aresta(self, u, v, w):
        key = frozenset({u, v})
        self.mapa_pesos[key] = w

        self.mapa_vizinhos[u].add(v)
        self.mapa_vizinhos[v].add(u)
