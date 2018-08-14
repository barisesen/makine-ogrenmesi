#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 20:58:51 2018

@author: barisesen
"""

import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder

data = pd.read_csv('eksikveriler.csv')

imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)

# numerik dataları ayır.
# numerik datalardan eksik olanları tamamla.
numericData = data.iloc[:, 1:4].values
imputer = imputer.fit(numericData[:, 1:4])
numericData[:, 1:4] = imputer.transform(numericData[:, 1:4])

# Cinsiyet datasını çıkartalım
cinsiyet = data.iloc[:, -1].values

# Ulke verisini numerik hale getirme işlemi
ulke = data.iloc[:, 0:1].values
le = LabelEncoder()
ulke[:, 0] = le.fit_transform(ulke[:, 0])
ohe = OneHotEncoder(categorical_features="all")
ulke = ohe.fit_transform(ulke).toarray()


# Data frame oluşturma

# Ulke frame i oluştur.
ulkeFrame = pd.DataFrame(data = ulke, index = range(22), columns = ['fr', 'tr', 'us'])

# Numerik dataları için frame oluştur.
numericFrame = pd.DataFrame(data = numericData, index = range(22), columns = ['boy', 'kilo', 'yas'])

# Cinsiyet frame oluştur.

cinsiyetFrame = pd.DataFrame(data = cinsiyet, index = range(22), columns = ['cinsiyet'])

# frameleri birleştirme
# default alt alta birleştirir, yan yana eklemek için axis = 1 verilmeli
response = pd.concat([ulkeFrame, numericFrame], axis = 1)

response2 = pd.concat([ulkeFrame, numericFrame, cinsiyetFrame], axis = 1)


# Test ve egitim verisi bolme islemi
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(response, cinsiyetFrame)






