# %% [markdown]
# # Projeto Python IA: Inteligência Artificial e Previsões
# 
# ### Case: Score de Crédito dos Clientes
# 
# Você foi contratado por um banco para conseguir definir o score de crédito dos clientes. Você precisa analisar todos os clientes do banco e, com base nessa análise, criar um modelo que consiga ler as informações do cliente e dizer automaticamente o score de crédito dele: Ruim, Ok, Bom
# 
# Arquivos da aula: https://drive.google.com/drive/folders/1FbDqVq4XLvU85VBlVIMJ73p9oOu6u2-J?usp=drive_link

# %%
#!pip install pandas scikit-learn

# %%
import pandas as pd

tabela = pd.read_csv("clientes.csv")

display(tabela)

#tabela = tabela.drop(columns="id_cliente")

display(tabela.info())

#display(tabela)

# %%
#filtrar score de credito

#label encoder (transforar textos em numeros para IA tratar)
from sklearn.preprocessing import LabelEncoder

codificador = LabelEncoder()

tabela["profissao"] = codificador.fit_transform(tabela["profissao"])

tabela["mix_credito"] = codificador.fit_transform(tabela["mix_credito"])

tabela["comportamento_pagamento"] = codificador.fit_transform(tabela["comportamento_pagamento"])

display(tabela.info())

# %%
#divisões base de dados

#quem quero prever e quem quero usar na previsão?

y = tabela["score_credito"]
x = tabela.drop(columns=["score_credito","id_cliente"])

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)

# %%
#criar a IA

#arvore de decisao

# KNN - Vizinhos proximos

#importa IA
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# criar a IA
modelo_arvore = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

# treinar a IA

modelo_arvore.fit(x_treino,y_treino)
modelo_knn.fit(x_treino,y_treino)

# %%
#testar modelos

previsao_arvore = modelo_arvore.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_teste, previsao_arvore))
print(accuracy_score(y_teste, previsao_knn))


