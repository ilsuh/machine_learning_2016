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
from sklearn.linear_model import Perceptron
import sklearn
import time

start_time = 0
elapsedTime = 0
start_time = time.time()

path_tr = r'C:\Users\user\Desktop\perceptron-train.csv'
path_tt = r'C:\Users\user\Desktop\perceptron-test.csv'

datap_tr = pd.read_csv(path_tr, header = None, usecols = list(xrange(1,3)))
datat_tr = pd.read_csv(path_tr, header = None, usecols = [0]).values.reshape(len(datap_tr),)

datap_tt = pd.read_csv(path_tt, header = None, usecols = list(xrange(1,3)))
datat_tt = pd.read_csv(path_tt, header = None, usecols = [0]).values.reshape(len(datap_tt),)


prcp = Perceptron(random_state = 241)
prcp.fit(datap_tr, datat_tr)
predictions = prcp.predict(datap_tt)

answ1 = sklearn.metrics.accuracy_score(datat_tt, predictions)
print answ1

scaler = StandardScaler()
datap_tr_scaled = scaler.fit_transform(datap_tr)
datap_tt_scaled = scaler.transform(datap_tt)

prcp.fit(datap_tr_scaled, datat_tr)
predictions_scaled = prcp.predict(datap_tt_scaled)

answ2 = sklearn.metrics.accuracy_score(datat_tt, predictions_scaled)
print answ2

print answ2 - answ1
