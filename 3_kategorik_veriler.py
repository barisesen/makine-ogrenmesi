#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 20:27:54 2018

@author: barisesen
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

data = pd.read_csv('eksikveriler.csv')

# ulke kolonunu getir.
ulke = data.iloc[:, 0:1].values

# label encoder ile tr, usa vb degelere bir sayısal deger atar.
le = LabelEncoder()
ulke[:, 0] = le.fit_transform(ulke[:, 0])
print(ulke)


# elimizdeki sayısal degerleri bir matris haline getirir.
# degerler kolon ismi haline gelir
# eger karsılık gelen degerı var ise 1 yazılır

# ornek
#[[1]
# [0]
# [2]]
#
#[[0. 1. 0.]
# [1. 0. 0.]
# [0. 0. 1.]]
ohe = OneHotEncoder(categorical_features="all")
ulke = ohe.fit_transform(ulke).toarray()

print(ulke)