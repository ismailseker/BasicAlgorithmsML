from sklearn.preprocessing import MinMaxScaler
import numpy as np

data = np.array([[10], [20], [30], [40], [50], [60], [70], [80], [90]])

scaler = MinMaxScaler()
data_normalized = scaler.fit_transform(data)

print(data_normalized)

from sklearn.preprocessing import StandardScaler

data = np.array([[10], [20], [30], [40], [50], [60], [70], [80], [90]])

scaler = StandardScaler()
data_standardized = scaler.fit_transform(data)

print(data_standardized)

# from sklearn.preprocessing import LabelEncoder

# data = ['Kırmızı', 'Mavi', 'Yeşil', 'Kırmızı', 'Yeşil']

# encoder = LabelEncoder()
# data_encoded = encoder.fit_transform(data)

# print(data_encoded)

# import pandas as pd

# data = pd.Series(['2024-11-01', '2024-11-02', '2024-11-03'])

# data_datetime = pd.to_datetime(data)

# data_year = data_datetime.dt.year
# data_month = data_datetime.dt.month
# data_day = data_datetime.dt.day

# print("Yıl:", data_year)
# print("Ay:", data_month)
# print("Gün:", data_day)

