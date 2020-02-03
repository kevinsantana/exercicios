# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:08:53 2019

@author: Kevin
"""

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout

# divide a base de dados
previsores = pd.read_csv('entradas-breast.csv')
classe = pd.read_csv('saidas-breast.csv')

# cria a rede neural
classificador = Sequential()
classificador.add(Dense(units = 8, activation = 'relu', \
kernel_initializer = 'normal', input_dim = 30))
classificador.add(Dropout(0.2))
classificador.add(Dense(units = 8, activation = 'relu',\
kernel_initializer = 'normal'))
classificador.add(Dropout(0.2))
classificador.add(Dense(units = 1, activation = 'sigmoid')) # saida    
classificador.compile(optimizer = 'adam', loss = 'binary_crossentropy',
                          metrics = ['binary_accuracy'])
classificador.fit(previsores, classe, batch_size = 10, epochs = 100)
