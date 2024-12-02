import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% CREATE DATASET
# Gaussian Dağılımı

# Class 1
x1 = np.random.normal(25,5,1000)
y1 = np.random.normal(25,5,1000)
# Class 2
x2 = np.random.normal(55,5,1000)
y2 = np.random.normal(60,5,1000)
# Class 3
x3 = np.random.normal(55,5,1000)
y3 = np.random.normal(15,5,1000)

x = np.concatenate((x1,x2,x3),axis=0)
y = np.concatenate((y1,y2,y3),axis=0)

dictionary = {"x":x,"y":y}

data = pd.DataFrame(dictionary)

# Data visualazation
plt.scatter(x1, y1)
plt.scatter(x2, y2)
plt.scatter(x3, y3)
# plt.show()

# %% Dendogram

from scipy.cluster.hierarchy import linkage,dendrogram

merg = linkage(data,method="ward")
dendrogram(merg,leaf_rotation=90)
plt.xlabel("data points")
plt.ylabel("euclidean distance")
plt.show()

# %% HC

from sklearn.cluster import AgglomerativeClustering

hierarchical_clustering = AgglomerativeClustering(n_clusters=3,linkage="ward")
cluster = hierarchical_clustering.fit_predict(data)

data["label"] = cluster
plt.scatter(data.x[data.label == 0 ],data.y[data.label == 0],color = "red")
plt.scatter(data.x[data.label == 1 ],data.y[data.label == 1],color = "green")
plt.scatter(data.x[data.label == 2 ],data.y[data.label == 2],color = "blue")
plt.show()


