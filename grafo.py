
from dataclasses import dataclass


@dataclass(init=False)
class Grafo:
    rotulos: dict[int, str]
    mapa_vizinhos: dict[int, set[int]]
    mapa_pesos: dict[frozenset[int], float]

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
                        u = int(partes[0])
                        v = int(partes[1])
                        w = float(partes[2])
                        grafo.adicionar_aresta(u, v, w)
        
        return grafo


    def __init__(self):
        self.rotulos = {}
        self.mapa_vizinhos = {}
        self.mapa_pesos = {}

    def vertices(self):
        return set(self.rotulos.keys())

    def qtdVertices(self, ):
        return len(self.rotulos)
    
    def qtdArestas(self, ):
        return len(self.mapa_pesos)
    
    def grau(self, v):
        return len(self.mapa_vizinhos.get(v, set()))
    
    def rotulo(self, v):
        return self.rotulos[v]
    
    def vizinhos(self, v):
        return self.mapa_vizinhos.get(v, set())
    
    def hasAresta(self, u, v):
        return frozenset({u, v}) in self.mapa_pesos
    
    def peso(self, u, v):
        return self.mapa_pesos.get(frozenset({u, v}), 0)

    def adicionar_vertice(self, rotulo, index):
        if index in self.rotulos:
            raise ValueError(f"Vertice with index {index} already exists.")

        self.rotulos[index] = rotulo
        self.mapa_vizinhos[index] = set()

    def adicionar_aresta(self, u, v, w):
        key = frozenset({u, v})
        self.mapa_pesos[key] = w

        self.mapa_vizinhos[u].add(v)
        self.mapa_vizinhos[v].add(u)
