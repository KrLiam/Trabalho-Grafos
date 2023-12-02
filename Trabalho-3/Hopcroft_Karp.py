from grafo import Grafo, ler_arquivo
from Hop_bfs import bfs
from Hop_dfs import dfs


def HopcroftKarp(grafo: Grafo, s: int) -> tuple[dict[int, int], dict[int, int]]:

    #nao sei eh pra  definir quem eh o grupo X e o grupo Y assim :)
    X = input("Grupo X: ").split()
    for i in range(len()): X[i]=int(X[i])
    Y = input("Grupo Y: ").split()
    for i in range(len(Y)): Y[i]=int(Y[i])


    D = {v: float("inf") for v in grafo.vertices()}
    mate = {v: None for v in grafo.vertices()}

    #tamanho do emparelhamento
    m = 0   
    while bfs(grafo,X,Y,mate,D):
        for x in X:
            if mate[x] == 0:
                if dfs(grafo,X,Y,mate,x,D):
                    m += 1
    return (m,mate)