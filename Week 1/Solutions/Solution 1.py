# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas
import numpy as np
path = r'C:\Users\user\Desktop\titanic.csv'
data = pandas.read_csv(path, index_col = 'PassengerId')
#f = float(sum(data['Pclass'] == 1))
#a = float(len(data))
#p = f/a
#m = data['Age'].mean()
#f = (sum(data['Sex'] == 'female'))
#f = len(data) - m
#p = float(sum(data['Survived'])) / float(len(data))
#c = data['SibSp'].corr(data['Parch'], method = 'pearson')
data1 = []
data2 = {}
data3 = []
c = 0
data1 = data[data['Sex'] == 'female']['Name']
for s in data1:
    for w in s.split('.')[1].replace('(', '').replace(')', '').replace('"', '').split():
       data3.append(w) 
   
for d in data3:
        c = data3.count(d)
        data2[d] = c
       
print max(data2, key=data2.get)