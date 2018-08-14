#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:57:44 2018

@author: barisesen
"""

import pandas as pd
from sklearn.preprocessing import Imputer

data = pd.read_csv('eksikveriler.csv')

# missing_values veri seti içerisinde eksik verinin nasıl belirtildiği
# strategy = mean => diğer değerlerin ortalamasını alıp eksik alanları dolduracagız.
# axis = 0 kolondaki değerlerin ortalamasını kullanacagımızı belirtiyor.
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)

Age = data.iloc[:, 1:4].values
print(Age)

imputer = imputer.fit(Age[:, 1:4])

Age[:, 1:4] = imputer.transform(Age[:, 1:4])
print(Age)

# NaN olan degerler kolon ortalamasi olan 28,45 ile değiştirildi.