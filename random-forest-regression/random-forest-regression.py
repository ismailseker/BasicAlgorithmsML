# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:57:16 2024

@author: junio
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("random-forest-regression.csv",sep=";",header=None)

x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=100,random_state=42)

rf.fit(x,y)

print("What is the price on 7.8 :",rf.predict([[7.8]]))


x_ = np.arange(min(x),max(x),0.01).reshape(-1,1)
y_head = rf.predict(x_)

#visualize
plt.scatter(x, y, color="red")
plt.plot(x_,y_head,color="green")

plt.xlabel("tribun level")
plt.ylabel("ucret")
plt.show()