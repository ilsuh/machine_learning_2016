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

path = r'C:\Users\user\Desktop\svm-data.csv'

datap = pd.read_csv(path, header = None, usecols = list(xrange(1,3)))
datat = pd.read_csv(path, header = None, usecols = [0]).values.reshape(len(datap),)

sv = sklearn.svm.SVC(C=100000, kernel='linear', random_state = 241)
sv.fit(datap, datat)

print sv.support_ + 1