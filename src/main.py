from city_generator import gerar_cidade
from routing import melhor_rota
from clustering import gerar_entregas,clusterizar_entregas
from route_comparison import rota_aleatoria
from visualization import (
    desenhar_cidade,
    desenhar_rota,
    plot_clusters,
    grafico_comparacao
)

import random


def main():

    print("Gerando cidade simulada")

    grafo,posicoes = gerar_cidade(30)

    desenhar_cidade(grafo,posicoes)

    bairros = list(grafo.nodes)

    origem = random.choice(bairros)
    destino = random.choice(bairros)

    print("Origem:",origem)
    print("Destino:",destino)

    caminho,distancia = melhor_rota(
        grafo,
        origem,
        destino,
        posicoes
    )

    print("Melhor rota (A*):",caminho)
    print("Distancia A*:",round(distancia,2))

    desenhar_rota(grafo,posicoes,caminho)

    print("\nComparando com rota aleatoria")

    rota_random,dist_random = rota_aleatoria(
        grafo,
        origem,
        destino
    )

    print("Rota aleatoria:",rota_random)
    print("Distancia rota aleatoria:",round(dist_random,2))

    grafico_comparacao(dist_random,distancia)

    print("\nGerando entregas")

    entregas = gerar_entregas(20)

    entregas,modelo = clusterizar_entregas(entregas,3)

    print(entregas)

    plot_clusters(entregas)


if __name__ == "__main__":
    main()
