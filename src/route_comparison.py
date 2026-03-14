import random

def rota_aleatoria(grafo,origem,destino):

    caminho = [origem]
    atual = origem
    visitados = set()

    visitados.add(origem)

    while atual != destino:

        vizinhos = list(grafo.neighbors(atual))

        possiveis = [v for v in vizinhos if v not in visitados]

        if not possiveis:
            break

        proximo = random.choice(possiveis)

        caminho.append(proximo)

        visitados.add(proximo)

        atual = proximo

    distancia = 0

    for i in range(len(caminho)-1):

        distancia += grafo[caminho[i]][caminho[i+1]]["weight"]

    return caminho,distancia
