class Grafo:
    rotulos: dict[int, str]
    mapa_vizinhos: dict[int, set[int]]
    mapa_pesos: dict[frozenset[int], int]

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

        self.mapa_vizinhos.setdefault(u, set()).add(v)
        self.mapa_vizinhos.setdefault(v, set()).add(u)


class GrafoDirigido:
    rotulos: dict[int, str]
    mapa_vizinhos: dict[int, tuple[int, int]]
    mapa_pesos: dict[tuple[int, int], int]

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
        return self.mapa_pesos.get((u, v), 0)

    def adicionar_vertice(self, rotulo, index):
        if index in self.rotulos:
            raise ValueError(f"Vertice with index {index} already exists.")

        self.rotulos[index] = rotulo
        self.mapa_vizinhos[index] = set()

    def adicionar_aresta(self, u, v, w):
        key = (u, v)
        self.mapa_pesos[key] = w

        self.mapa_vizinhos.setdefault(u, set()).add(v)
        self.mapa_vizinhos.setdefault(u, set()).add(u)

    def inverter_arestas(self):
        novo_mapa_pesos = {}

        for (u, v), peso in self.mapa_pesos.items():
            novo_mapa_pesos[(v, u)] = peso

        self.mapa_pesos = novo_mapa_pesos
        
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
                grafo = Grafo()
                continue

            if linha.startswith("*arcs"):
                ler_arestas = True
                grafo = GrafoDirigido()
                continue

            if ler_arestas:
                partes = linha.split()
                if len(partes) == 3:
                    arestas.append((int(partes[0]), int(partes[1]), int(partes[2])))


    for rotulo, nome in vertices:
        grafo.adicionar_vertice(rotulo, nome)
    
    for u, v, w in arestas:
        grafo.adicionar_aresta(u, v, w)

    return grafo
