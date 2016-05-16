# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas
import numpy as np
import time
start_time = 0
elapsedTime = 0
start_time = time.time()
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
max1 = 0 
data1 = data[data['Sex'] == 'female']['Name']
#print data1
for s in data1:
    for w in s.split('.')[1].replace('(', '').replace(')', '').replace('"', '').split():
       # data2.setdefault(w)
        data3.append(w)
    
"""new_data1 = {}
for n in new_data:
    for w in a.split('.')[1].replace('(', '').replace(')', '').split():

        new_data1.setdefault(w)
"""        
"""for d in data3:
        c = data3.count(d)
        data2[d] = c"""

for d in data3:
    c = data3.count(d)
    if (c > max1):
        max1 = c
        s = d
        print s

#df = pandas.DataFrame(data2.items(), columns=['Name', 'Count'])
#print df
#df.plot.bar()
#print max(data2, key=data2.get)
#print s
elapsedTime = time.time() - start_time
print elapsedTime