# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 07:50:56 2019

@author: Kevin
"""

import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from keras import backend as k
from sklearn.model_selection import cross_val_score

previsores = pd.read_csv('entradas-breast.csv')
classe = pd.read_csv('saidas-breast.csv')

def criarRede():
    k.clear_session()
    classificador = Sequential()
    initializer = keras.initializers.TruncatedNormal(mean=0.0001, stddev=0.02, seed=None) # inicializador dos pesos    
    classificador.add(Dense(units = 8, activation = 'relu', kernel_initializer= initializer, input_dim = 30)) #1ª camda de neuronios
    classificador.add(Dropout(0.20)) # dropout, tecnica para solucao do overfitting
    classificador.add(Dense(units = 8, activation = 'relu', kernel_initializer= initializer))
    classificador.add(Dropout(0.20)) # dropout
    classificador.add(Dense(units = 8, activation = 'relu', kernel_initializer= initializer))
    classificador.add(Dropout(0.20)) # dropout   
    classificador.add(Dense(units = 1, activation = 'sigmoid'))    
    #otimizador = keras.optimizers.Adam(lr = 0.001, decay = 0.0001, clipvalue = 0.5)
    otimizador = keras.optimizers.Adamax(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0)
    classificador.compile(optimizer = otimizador, loss = 'binary_crossentropy', metrics = ['binary_accuracy'])
    return classificador

classificador = KerasClassifier(build_fn = criarRede, epochs = 200, batch_size = 20)
resultados = cross_val_score(estimator = classificador, X = previsores, y = classe, cv = 10, scoring = 'accuracy')
media = resultados.mean()
desvio = resultados.std()