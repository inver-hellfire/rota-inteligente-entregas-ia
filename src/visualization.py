import matplotlib.pyplot as plt
import networkx as nx

def desenhar_cidade(G,pos):

    plt.figure(figsize=(8,6))

    nx.draw(
        G,
        pos,
        node_size=200,
        node_color="skyblue",
        with_labels=False
    )

    plt.title("Mapa da Cidade Simulada")

    plt.show()


def desenhar_rota(G,pos,caminho):

    plt.figure(figsize=(8,6))

    nx.draw(G,pos,node_size=200,node_color="lightgray",with_labels=False)

    edges = list(zip(caminho,caminho[1:]))

    nx.draw_networkx_nodes(G,pos,nodelist=caminho,node_color="red")

    nx.draw_networkx_edges(G,pos,edgelist=edges,width=3,edge_color="red")

    plt.title("Melhor Rota Encontrada (A*)")

    plt.show()


def plot_clusters(df):

    plt.figure(figsize=(6,6))

    plt.scatter(df["x"],df["y"],c=df["cluster"],s=100)

    plt.title("Clusters de Entregas")

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.show()


def grafico_comparacao(dist_random,dist_astar):

    rotas = ["Rota Aleatoria","Rota IA (A*)"]
    valores = [dist_random,dist_astar]

    plt.bar(rotas,valores)

    plt.title("Comparação de Rotas")

    plt.ylabel("Distancia")

    plt.show()
