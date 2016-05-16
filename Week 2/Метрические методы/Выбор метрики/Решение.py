# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.cross_validation import KFold
from sklearn.cross_validation import *
from sklearn.preprocessing import *
from sklearn import metrics
import sklearn

import time
start_time = 0
elapsedTime = 0
start_time = time.time()
boston =  load_boston()
datap = sklearn.preprocessing.scale(boston.data)
datac = boston.target
pf = np.linspace(1, 10, num = 200)

#kng = KNeighborsRegressor(n_neighbors=5, weights='distance')
kf = KFold(len(datap), n_folds = 5, shuffle = True, random_state=42)
acc = []
for i in pf:
    print i
    kng = KNeighborsRegressor(n_neighbors=5, weights='distance', p = i)
    kng.fit(datap, datac)
    a = cross_val_score(estimator=kng, X=datap, y=datac, scoring='mean_squared_error', cv=kf)
    a = a.mean()
    print a
    print "/n"
    acc.append(a)
    
print max(acc)
