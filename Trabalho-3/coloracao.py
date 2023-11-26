
import networkx as nx
from grafo import Grafo, ler_arquivo
import matplotlib.pyplot as plt 

def show_graph(g: Grafo, colors: dict[int, str] = {}):
    ng = nx.Graph()

    for v in g.vertices():
        ng.add_node(v, color=colors.get(v, "blue"))
    
    for u, v in g.arestas():
        ng.add_edge(u, v)

    ax = plt.subplot(121)
    nx.draw(
        ng,
        ax=ax,
        with_labels=True,
        node_color=[colors.get(v, "blue") for v in ng],
        font_color="white",
    )
    plt.show()
    

if __name__ == "__main__":
    g = ler_arquivo("entrada.txt")
    show_graph(g, {
        1: "red",
        2: "blue",
        3: "green",
        4: "red",
        5: "blue",
        6: "green",
        7: "red",
    })