# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 22:33:04 2020

@author: Kevin
"""

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score


# carregando o dataset
dataframe = pd.read_csv('./googleplaystore_original.csv')

# previsores e classe
classe = dataframe.iloc[:,1].values
dataframe.drop('Category', axis=1, inplace=True)
previsores = dataframe.iloc[:, 1:13].values
dataframe.isnull().any()

# faltantes e inconsistentes
#rating
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(previsores[:, 0:1])
previsores[:, 0:1] = imputer.transform(previsores[:, 0:1])

#type
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer = imputer.fit(previsores[:, 4:5])
previsores[:, 4:5] = imputer.transform(previsores[:, 4:5])


#Content Rating 
#imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer = imputer.fit(previsores[:, 6:7])
previsores[:, 6:7] = imputer.transform(previsores[:, 6:7])

#Current Ver
#imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer = imputer.fit(previsores[:, 9:10])
previsores[:, 9:10] = imputer.transform(previsores[:, 9:10])


#Android Ver
#imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer = imputer.fit(previsores[:, 10:11])
previsores[:, 10:11] = imputer.transform(previsores[:, 10:11])

# normalizacao classe
labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe)

# one hot encoder
column_tranformer = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), [0,1,2,3,4,5,6,7,8,9,10])],remainder='passthrough')
previsores = column_tranformer.fit_transform(previsores).toarray()

# divisao do dataset
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.15, random_state=0)

# treinamento do modelo
classificador = RandomForestClassifier(n_estimators=50, criterion='entropy', random_state=0)
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

# resultados do modelo
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)









