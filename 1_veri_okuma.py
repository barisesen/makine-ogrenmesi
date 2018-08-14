#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:31:21 2018

@author: barisesen
"""

import pandas as pd
import numpy as np

veriler = pd.read_csv('veriler.csv')

boy = veriler[['boy']]
boyKilo = veriler[['boy', 'kilo']]

print(boy)

print(boyKilo)