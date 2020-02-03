# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 09:56:01 2019

@author: Kevin
"""

import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV # busca em grade para descobrir os melhores parametros

# divide a base de dados
previsores = pd.read_csv('entradas-breast.csv')
classe = pd.read_csv('saidas-breast.csv')

# cria a rede neural
def criarRede(optimizer, lose, kernel_initializer, activation, neurons):
    classificador = Sequential()
    classificador.add(Dense(units = neurons, activation = activation, \
    kernel_initializer = kernel_initializer, input_dim = 30)) #1ª camda de neuronios
    classificador.add(Dropout(0.2)) # dropout, tecnica para solucao do overfitting
    classificador.add(Dense(units = neurons, activation = activation,\
    kernel_initializer = kernel_initializer))
    classificador.add(Dropout(0.2)) # dropout
    classificador.add(Dense(units = 1, activation = 'sigmoid')) # saida    
    classificador.compile(optimizer = optimizer, loss = lose,
                          metrics = ['binary_accuracy'])
    return classificador

# rede neural
classificador = KerasClassifier(build_fn = criarRede)

#
parametros = {'batch_size': [10,30],
              'epochs': [50, 100], 
              'optimizer' : ['adam', 'sgd'], 
              'lose':['binary_crossentropy', 'hinge'],
              'kernel_initializer':['random_uniform', 'normal'],
              'activation':['relu', 'tanh'],
              'neurons':[16,8]}

# efetua todas as possiveis combinacoes dos parametros
# demora algumas horas
# em uma aplicacao comercial, os melhores parametros sao assim selecionados
grid_search = GridSearchCV(estimator = classificador,
                           param_grid = parametros,
                           scoring = 'accuracy',
                           cv = 5)
grid_search = grid_search.fit(previsores, classe)
melhores_parametros = grid_search.best_params_
melhor_precisao = grid_search.best_score_