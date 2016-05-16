# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import KFold
from sklearn.cross_validation import *
from sklearn.preprocessing import *
from sklearn import metrics
import time
start_time = 0
elapsedTime = 0
start_time = time.time()
path = r'C:\Users\user\Desktop\wine.data'
data = pd.read_csv(path, header = None)
datap = pd.read_csv(path, header = None, usecols = list(xrange(1,14)))
datac = pd.read_csv(path, header = None, usecols = [0]).values.reshape(len(datap),)

kf = KFold(len(datap), n_folds = 5, shuffle = True, random_state=42)
acc = []
#acc = sklearn.cross_validation.cross_val_score()
for k in range(1,51):
    #print k
    kn = KNeighborsClassifier(n_neighbors=k)
    kn.fit(datap, datac)
    a = cross_val_score(estimator=kn, X=datap, y=datac, cv=kf)
    a = a.mean() 
    #print a
    acc.append(a)
    
answ_k = 1
answ_acc = max(acc)
print answ_k
print answ_acc

acc1 = []
datap1 = sklearn.preprocessing.scale(datap)
for k1 in range(1,51):
    print k1
    kn = KNeighborsClassifier(n_neighbors=k1)
    kn.fit(datap1, datac)
    a1 = cross_val_score(estimator=kn, X=datap1, y=datac, cv=kf)
    a1 = a1.mean() 
    print a1
    acc1.append(a1)
    
print max(acc1)
