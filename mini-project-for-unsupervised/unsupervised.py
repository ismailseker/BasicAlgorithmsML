import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Iris.csv")

df2 = df.drop("Species",axis=1)

df3 = df2.corr()

from sklearn.cluster import KMeans

wcss = []

for k in range(1,15):
    
    kmeans = KMeans(n_clusters=k,random_state=42)
    kmeans.fit(df2)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,15), wcss)
plt.xlabel("number of values")
plt.ylabel("wcss")
# plt.show()

kmeans2 = KMeans(n_clusters=3,random_state=42)
clusters = kmeans2.fit_predict(df2)
df2['label'] = clusters

# plt.plot(range(1,15),wcss)

plt.scatter(df2.PetalWidthCm[df2.label==0],df2.PetalLengthCm[df2.label==0], color="red")
plt.scatter(df2.PetalWidthCm[df2.label==1],df2.PetalLengthCm[df2.label==1], color="green")
plt.scatter(df2.PetalWidthCm[df2.label==2],df2.PetalLengthCm[df2.label==2], color="blue")

# plt.scatter(x="PetalWidthCm",y="PetalLengthCm",c="label", data=df2)
plt.show()


