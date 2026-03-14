# Rota Inteligente: Otimização de Entregas com Algoritmos de IA

Projeto desenvolvido para a disciplina **Artificial Intelligence Fundamentals**.

Este projeto simula um sistema inteligente de otimização de rotas para uma empresa fictícia de delivery chamada **Sabor Express**, utilizando algoritmos clássicos de Inteligência Artificial.

---

# 1. Descrição do Problema

Empresas de delivery frequentemente enfrentam dificuldades para organizar suas rotas de entrega, especialmente em horários de pico. Quando as rotas são definidas manualmente, podem ocorrer:

- atrasos nas entregas
- aumento do custo de combustível
- rotas ineficientes
- insatisfação dos clientes

Neste projeto, desenvolvemos um sistema capaz de sugerir rotas eficientes utilizando técnicas de Inteligência Artificial.

A cidade é representada como um **grafo**, onde:

- **Nós (nodes)** representam bairros ou pontos da cidade
- **Arestas (edges)** representam ruas
- **Pesos (weights)** representam distância entre os locais

---

# 2. Objetivos do Projeto

O objetivo da solução é:

- Modelar uma cidade como um grafo
- Encontrar rotas eficientes entre pontos de entrega
- Agrupar entregas próximas
- Reduzir a distância total percorrida pelos entregadores

---

# 3. Tecnologias Utilizadas

Linguagem:

- Python

Bibliotecas:

- networkx
- numpy
- pandas
- matplotlib
- scikit-learn

---

# 4. Algoritmos de Inteligência Artificial Utilizados

## A* (A-Star)

O algoritmo **A*** é utilizado para encontrar o menor caminho entre dois pontos da cidade.

Ele utiliza uma função heurística:

```
f(n) = g(n) + h(n)
```

onde:

- **g(n)** = custo real até o nó atual
- **h(n)** = estimativa do custo restante

Neste projeto, a heurística utilizada é a **distância euclidiana entre os pontos da cidade**.

O algoritmo A* é amplamente utilizado em:

- navegação GPS
- jogos
- logística
- robótica

---

## K-Means Clustering

Para otimizar múltiplas entregas, utilizamos o algoritmo **K-Means** para agrupar pontos de entrega próximos.

Esse processo divide as entregas em **clusters (zonas de entrega)**, permitindo que cada entregador atenda uma região específica.

Benefícios:

- redução da distância percorrida
- melhor organização das rotas
- maior eficiência operacional

---

# 5. Estrutura do Projeto

```
rota-inteligente-entregas-ia

src/
    main.py
    city_generator.py
    routing.py
    clustering.py
    visualization.py

data/

docs/

requirements.txt
README.md
```

---

# 6. Funcionamento do Sistema

O sistema executa as seguintes etapas:

1. Geração automática de uma cidade simulada com múltiplos bairros
2. Conexão entre bairros formando um grafo
3. Seleção aleatória de origem e destino
4. Aplicação do algoritmo A* para encontrar a melhor rota
5. Geração de múltiplos pontos de entrega
6. Aplicação do algoritmo K-Means para agrupar entregas

---

# 7. Resultados

Ao executar o sistema, são gerados:

- Mapa da cidade simulada
- Melhor rota entre dois pontos usando A*
- Agrupamento de entregas utilizando clustering

Essas visualizações ajudam a demonstrar como algoritmos de Inteligência Artificial podem ser aplicados para melhorar sistemas logísticos.

---

# 8. Como Executar o Projeto

Clone o repositório:

```
git clone https://github.com/seuusuario/rota-inteligente-entregas-ia
```

Instale as dependências:

```
pip install -r requirements.txt
```

Execute o sistema:

```
cd src
python main.py
```

---

# 9. Limitações

Este projeto é uma simulação acadêmica e apresenta algumas limitações:

- não utiliza dados reais de trânsito
- não considera tempo real de tráfego
- não simula múltiplos entregadores simultaneamente

---

# 10. Melhorias Futuras

Possíveis melhorias incluem:

- integração com APIs de mapas (Google Maps ou OpenStreetMap)
- inclusão de dados de trânsito em tempo real
- otimização de múltiplas rotas simultaneamente
- uso de algoritmos genéticos para roteamento

---

# 11. Referências

- Estudo de caso UPS ORION
- ResearchGate – AI Powered Route Optimization
- Medium – Logistics Optimization with Clustering
- Kardinal.ai – Delivery Optimization
