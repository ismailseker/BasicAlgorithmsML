
# # 1. Equal Width Discretization (Eşit Genişlikte Ayrıklaştırma)

import numpy as np
import pandas as pd


# data = np.array([5, 15, 25, 35, 45, 55, 65, 75, 85, 95])

# bins = np.linspace(data.min(), data.max(), num=4)  # 3 aralık (4 sınır noktası)
# categories = pd.cut(data, bins=bins, labels=["Low", "Medium", "High"])

# print("Veriler:", data)
# print("Bölünmüş Veriler:", categories)

# # 2. Equal Frequency Discretization (Eşit Frekansta Ayrıklaştırma)

# from sklearn.preprocessing import KBinsDiscretizer

# data = np.array([[10], [20], [30], [40], [50], [60], [70], [80], [90], [100]])

# est = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='quantile')  # Equal frequency
# data_binned = est.fit_transform(data)

# print("Orijinal Veri:\n", data.ravel())
# print("Ayrıklaştırılmış Veri:\n", data_binned.ravel())

# # 3. Yakın olan değere göre kümeleme 
# from sklearn.cluster import KMeans

# data = np.array([[10], [20], [30], [40], [50], [60], [70], [80], [90], [100]])

# kmeans = KMeans(n_clusters=3, random_state=42)
# kmeans.fit(data)
# labels = kmeans.predict(data)

# print("Orijinal Veri:\n", data.ravel())
# print("K-Means Grupları:\n", labels)

# 4. Ayırdığımız noktaya göre classification ( sınıflandırma)
 
# data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# bins = [0, 30, 60, 100]  
# labels = ["Low", "Medium", "High"]  
# categories = pd.cut(data, bins=bins, labels=labels, right=False)

# print("Veriler:", data)
# print("Kategoriler:", categories)




