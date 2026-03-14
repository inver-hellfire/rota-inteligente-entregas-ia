import pandas as pd
from sklearn.cluster import KMeans
import random

def gerar_entregas(num_entregas=20):

    entregas = []

    for i in range(num_entregas):

        x = random.uniform(0,100)
        y = random.uniform(0,100)

        entregas.append([i,x,y])

    df = pd.DataFrame(entregas,columns=["id","x","y"])

    return df


def clusterizar_entregas(df,k=3):

    coords = df[["x","y"]]

    modelo = KMeans(n_clusters=k,random_state=42)

    df["cluster"] = modelo.fit_predict(coords)

    return df,modelo
