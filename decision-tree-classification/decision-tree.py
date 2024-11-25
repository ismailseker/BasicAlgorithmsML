# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:39:58 2024

@author: junio
"""

import pandas as pd
import numpy as np

data = pd.read_csv("data.csv")

data.drop(["Unnamed: 32","id"],axis=1,inplace=True)

data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis]

y = data.diagnosis.values

x_data = data.drop(["diagnosis"],axis=1)

x = (x_data - np.min(x_data))/ (np.max(x_data)-np.min(x_data))

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state = 42)

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()

dt.fit(x_train,y_train)

print(f'score : {dt.score(x_test,y_test)}')

