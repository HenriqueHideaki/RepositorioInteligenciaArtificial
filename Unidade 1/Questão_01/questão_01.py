# -*- coding: utf-8 -*-
"""QUESTÃO_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DAb9cmUTFIjU85zReUqmvOx_PByjcMct

##1-) A tabela de dados abaixo ilustra a aplicação do método Naïve-Bayes. Um determinado banco deve decidir se um cliente deve ou não receber um empréstimo bancário em função da sua condição de bom ou mau pagador. Considerando os dados de treinamento abaixo, aplique o classificador Naive-Bayes, para atribuir a classe (rótulo) para os registros 12 e 13:
"""

from sklearn.naive_bayes import GaussianNB

import pandas as pd

base_risco_credito = pd.read_csv('/content/RiscoCredito.csv', encoding = "UTF-8", sep = ";")

base_risco_credito

X_risco_credito = base_risco_credito.iloc[:, 0:4].values
X_risco_credito

Y_risco_credito = base_risco_credito.iloc[:, 4].values
Y_risco_credito

from sklearn.preprocessing import LabelEncoder
label_encoder_casapropria = LabelEncoder()
label_encoder_estadocivil = LabelEncoder()
label_encoder_carro = LabelEncoder()
label_encoder_rendimentos = LabelEncoder()

X_risco_credito[:,0] = label_encoder_casapropria.fit_transform(X_risco_credito[:,0])
X_risco_credito[:,1] = label_encoder_estadocivil.fit_transform(X_risco_credito[:,1])
X_risco_credito[:,2] = label_encoder_carro.fit_transform(X_risco_credito[:,2])
X_risco_credito[:,3] = label_encoder_rendimentos.fit_transform(X_risco_credito[:,3])

X_risco_credito

import pickle
with open('risco_crdito.pkl', 'wb') as f:
  pickle.dump([X_risco_credito, Y_risco_credito], f)

naive_risco_credito = GaussianNB()
naive_risco_credito.fit(X_risco_credito, Y_risco_credito)

"""## Queremos saber se um cliente que não possui casa própria [0], cujo estado civil é divorciado [1], possui carro [1] e tem um rendimento alto [0], é um bom pagador: """

previsao = naive_risco_credito.predict([[0, 1, 1, 0]])
print(previsao)

"""## Queremos saber se um cliente que possui casa própria [1], cujo estado civil é solteiro [2], não possui carro [0] e tem um rendimento alto [3], é um bom pagador: """

previsao = naive_risco_credito.predict([[1, 2, 0, 3]])
print(previsao)

"""#Resposta da Questão 01:
## O cliente de registro 12 não seria um bom pagador (NÃO) e o cliente de registro 13 seria um bom pagador(SIM)
"""