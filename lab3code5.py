import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import pairwise_distances
from sklearn.preprocessing import LabelEncoder
from scipy.spatial.distance import cosine


file_path = r"C:\Users\akars\Desktop\jn\Lab Session Data.xlsx"
thyroid_data = pd.read_excel(file_path, sheet_name = 'thyroid0387_UCI')

thyroid_data.head()

type_of_attribute = thyroid_data.dtypes
print("attributes:",type_of_attribute)

td_encoded = pd.get_dummies(thyroid_data, drop_first = True)
td_encoded.head()

numeric_summary = thyroid_data.describe()
print(numeric_summary)

missing_values = thyroid_data.isnull().sum()
print(missing_values)

numeric_columns = thyroid_data.select_dtypes(include=['float64','int64']).columns
plt.figure(figsize=(10,8))
sns.boxplot(data=thyroid_data[numeric_columns])
plt.title('Boxplot:')
plt.show()

mean = thyroid_data[numeric_columns].mean()
std_vals = thyroid_data[numeric_columns].std()

print("Mean: ",mean)
print("Std values: ",std_vals)

