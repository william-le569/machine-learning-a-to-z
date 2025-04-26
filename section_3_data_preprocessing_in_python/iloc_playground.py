import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
print(X)
print("-----")
print(y)
# print(X.isna().sum())


# def numberOfNonNans(data):
#     count = 0
#     for i in data:
#         if not np.isnan(i):
#             count += 1
#     return count 
print(dataset.isnull())

print(dataset.isnull().sum())

print(type(X))