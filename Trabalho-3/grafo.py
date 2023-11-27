from typing import Iterable


class Grafo:
    rotulos: dict[int, str]
    mapa_vizinhos: dict[int, set[int]]
    mapa_pesos: dict[frozenset[int], float]

    def __init__(self, vertices: Iterable[int] = (), arestas: Iterable[Iterable[int]] = ()):
        self.rotulos = {}
        self.mapa_vizinhos = {}
        self.mapa_pesos = {}

        for v in vertices:
            self.adicionar_vertice(str(v), v)
        
        for aresta in arestas:
            u, v, *w = aresta
            self.adicionar_aresta(u, v, w[0] if w else 0)

    def vertices(self):
        return set(self.rotulos.keys())

    def arestas(self):
        return set(self.mapa_pesos.keys())

    def qtdVertices(self):
        return len(self.rotulos)

    def qtdArestas(self):
        return len(self.mapa_pesos)

    def grau(self, v):
        return len(self.mapa_vizinhos.get(v, set()))

    def rotulo(self, v):
        return self.rotulos.get(v)

    def vizinhos(self, v):
        return self.mapa_vizinhos.get(v, set())

    def hasAresta(self, u, v):
        return frozenset({u, v}) in self.mapa_pesos

    def peso(self, u, v):
        return self.mapa_pesos.get(frozenset({u, v}), 0.0)

    def adicionar_vertice(self, rotulo, index):
        if index in self.rotulos:
            raise ValueError(f"Vertice with index {index} already exists.")

        self.rotulos[index] = rotulo
        self.mapa_vizinhos[index] = set()

    def adicionar_aresta(self, u, v, w):
        key = frozenset({u, v})
        self.mapa_pesos[key] = w

        if not u in self.rotulos:
            self.adicionar_vertice(str(u), u)
        if not v in self.rotulos:
            self.adicionar_vertice(str(v), v)

        self.mapa_vizinhos[u].add(v)
        self.mapa_vizinhos[v].add(u)


class GrafoDirigido:
    rotulos: dict[int, str]
    mapa_vizinhos: dict[int, tuple[int, int]]
    mapa_pesos: dict[tuple[int, int], float]

    def __init__(self):
        self.rotulos = {}
        self.mapa_vizinhos = {}
        self.mapa_pesos = {}

    def vertices(self):
        return set(self.rotulos.keys())

    def arestas(self):
        return set(self.mapa_pesos.keys())

    def qtdVertices(self):
        return len(self.rotulos)

    def qtdArestas(self):
        return len(self.mapa_pesos)

    def grau(self, v):
        return len(self.mapa_vizinhos.get(v, set()))

    def rotulo(self, v):
        return self.rotulos.get(v)

    def vizinhos(self, v):
        return self.mapa_vizinhos.get(v, set())

    def hasAresta(self, u, v):
        return (u, v) in self.mapa_pesos

    def peso(self, u, v):
        return self.mapa_pesos.get((u, v), 0.0)

    def adicionar_vertice(self, rotulo, index):
        if index in self.rotulos:
            raise ValueError(f"Vertice with index {index} already exists.")

        self.rotulos[index] = rotulo
        self.mapa_vizinhos[index] = set()

    def adicionar_aresta(self, u, v, w):
        key = (u, v)
        self.mapa_pesos[key] = w

        if not u in self.rotulos:
            self.adicionar_vertice(str(u), u)
        if not v in self.rotulos:
            self.adicionar_vertice(str(v), v)

        self.mapa_vizinhos[u].add(v)



    def inverter_arestas(self):
        novo_mapa_vizinhos = {}
        novo_mapa_pesos = {}

        for aresta, peso in self.mapa_pesos.items():
            u, v = aresta
            novo_mapa_pesos[(v, u)] = peso

        for v, vizinhos in self.mapa_vizinhos.items():
            novo_mapa_vizinhos[v] = set()

        for u, v in self.arestas():
            novo_mapa_vizinhos[v].add(u)

        self.mapa_vizinhos = novo_mapa_vizinhos
        self.mapa_pesos = novo_mapa_pesos

    def criar_grafo_residual(self):
        grafo_residual = GrafoDirigido()
        grafo_residual.rotulos = self.rotulos.copy()
        grafo_residual.mapa_vizinhos = {v: set() for v in self.vertices()}

        # Adiciona as arestas originais e as arestas residuais com peso 0
        for u, v in self.arestas():
            peso_original = self.peso(u, v)
            grafo_residual.adicionar_aresta(u, v, peso_original)
            if not grafo_residual.hasAresta(v, u):
                grafo_residual.adicionar_aresta(v, u, 0)

        return grafo_residual




        
def ler_arquivo(file_name):
    grafo = None
    vertices = []
    arestas = []

    with open(file_name, "r", encoding="utf-8") as arquivo:
        ler_vertices = False
        ler_arestas = False

        for linha in arquivo:
            linha = linha.strip()

            if linha.startswith("*vertices"):
                ler_vertices = True
                continue

            if ler_vertices:
                partes = linha.split()
                if len(partes) == 2:
                    index, rotulo = partes
                    vertices.append((rotulo, int(index)))

            if linha.startswith("*edges"):
                ler_arestas = True
                ler_vertices = False
                grafo = Grafo()
                continue

            if linha.startswith("*arcs"):
                ler_arestas = True
                ler_vertices = False
                grafo = GrafoDirigido()
                continue

            if ler_arestas:
                partes = linha.split()
                if len(partes) >= 2:
                    str_u, str_v, *resto = partes
                    str_peso = "0" if not resto else resto[0]
                    arestas.append((int(str_u), int(str_v), float(str_peso)))


    for rotulo, nome in vertices:
        grafo.adicionar_vertice(rotulo, nome)
    
    for u, v, w in arestas:
        grafo.adicionar_aresta(u, v, w)

    return grafo