# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 23:40:53 2019

@author: Kevin
"""

import pandas as pd
# uma variavel, sempre, para receber os atributos previsores e outra para
# receber o(s) atributo(s) classe
previsores = pd.read_csv('entradas-breast.csv')
classe = pd.read_csv('saidas-breast.csv')

from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, \
classe_teste = train_test_split(previsores, classe, test_size = 0.25)

import keras
from keras.models import Sequential # classe para criacao da rede neural
from keras.layers import Dense # camadas densas na rede neural
from keras.utils import plot_model # plotar rede neural
classificador = Sequential()
# units = quantos neuronio vou usar na
# camada oculta: entradas+saidas/2
# camada oculta: funcao de ativacao relu
# atributo classe: funcao de ativacao sigmoid (por ser binario)
classificador.add(Dense(units = 16, activation = 'relu', \
kernel_initializer = 'random_uniform', input_dim = 30)) #camada entrada + camada oculta
classificador.add(Dense(units = 16, activation = 'relu', \
kernel_initializer = 'random_uniform')) # segunda camada oculta
classificador.add(Dense(units = 1, activation = 'sigmoid')) #camada saida
#plot_model(classificador, to_file='model.png')

otimizador = keras.optimizers.Adam(lr = 0.001, decay = 0.0001, clipvalue = 0.5)

classificador.compile(optimizer = otimizador, loss = 'binary_crossentropy',
                      metrics = ['binary_accuracy'])
# treinamento
classificador.fit(previsores_treinamento, classe_treinamento,
                  batch_size = 10, epochs = 100)

pesos0 = classificador.layers[0].get_weights()
print(pesos0)
print(len(pesos0))
pesos1 = classificador.layers[1].get_weights()

# utilizando o sklearn para metricas
previsoes = classificador.predict(previsores_teste)
previsoes = (previsoes > 0.5)
from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)

# atribui a rede neural e efetua os testes de acuracia
# utilizando o keras para metricas
resultado = classificador.evaluate(previsores_teste, classe_teste)

