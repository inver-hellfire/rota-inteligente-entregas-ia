import networkx as nx
import numpy as np
import random

def gerar_cidade(num_bairros=30):

    G = nx.Graph()
    posicoes = {}

    for i in range(num_bairros):

        nome = f"Bairro_{i}"

        x = random.uniform(0,100)
        y = random.uniform(0,100)

        posicoes[nome] = (x,y)

        G.add_node(nome,pos=(x,y))

    bairros = list(G.nodes)

    for i in bairros:
        for j in bairros:

            if i != j:

                dist = np.linalg.norm(
                    np.array(posicoes[i]) - np.array(posicoes[j])
                )

                if dist < 35:
                    G.add_edge(i,j,weight=dist)

    return G,posicoes
