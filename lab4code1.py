# A1: Intraclass Spread and Interclass Distances
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
from scipy.spatial.distance import minkowski

df = pd.read_excel('C:\Users\akars\Desktop\jn\Lab Session Data.xlsx')
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
class_1 = X[y == 'A']
class_2 = X[y == 'B']
sprs_1 = np.std(class_1, axis=0)
sprs_2 = np.std(class_2, axis=0)
cent_1 = np.mean(class_1, axis=0)
cent_2 = np.mean(class_2, axis=0)

dist = np.linalg.norm(cent_1 - cent_2)
print("spread of class 1:", sprs_1)
print("spread of class 2:", sprs_2)
print("The centroid of class 1:", cent_1)
print("The centroid of class 2:", cent_2)
print("dist between centroids in the interclass is:", dist)
