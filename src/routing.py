import networkx as nx
import numpy as np

def heuristica(a,b,posicoes):

    x1,y1 = posicoes[a]
    x2,y2 = posicoes[b]

    return np.sqrt((x1-x2)**2 + (y1-y2)**2)

def melhor_rota(grafo,origem,destino,posicoes):

    caminho = nx.astar_path(
        grafo,
        origem,
        destino,
        heuristic=lambda a,b: heuristica(a,b,posicoes),
        weight="weight"
    )

    distancia = nx.astar_path_length(
        grafo,
        origem,
        destino,
        weight="weight"
    )

    return caminho,distancia
