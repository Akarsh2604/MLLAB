import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_percentage_error
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
import matplotlib.pyplot as plt

path_of_file = r"C:\Users\vvmad\Downloads\5th\ML\HM7 - Java\java_cc_embed_data.csv"
data = pd.read_csv(path_of_file)

print("Top 5 rows:")
print(data.head())

print("Missing values of every column:")
print(data.isnull().sum())

print("Data sets:")
print(data.describe())

feature_set = data.iloc[:, :-1]  
target_set = data.iloc[:, -1]   

feature_set_train, feature_set_test, target_set_train, target_set_test = train_test_split(feature_set, target_set, test_size=0.2, random_state=42)

#A1
model = LogisticRegression()
model.fit(feature_set_train, target_set_train)

target_set_train_pred = model.predict(feature_set_train)
target_set_test_pred = model.predict(feature_set_test)



#A2
mse_train = mean_squared_error(target_set_train, target_set_train_pred)
rmse_train = mse_train ** 0.5
mape_train = mean_absolute_percentage_error(target_set_train, target_set_train_pred)
r2_train = r2_score(target_set_train, target_set_train_pred)

mse_test = mean_squared_error(target_set_test, target_set_test_pred)
rmse_test = mse_test ** 0.5
mape_test = mean_absolute_percentage_error(target_set_test, target_set_test_pred)
r2_test = r2_score(target_set_test, target_set_test_pred)

print(f"\nTraining:mse: {mse_train}, rmse: {rmse_train}, mape: {mape_train}, r2: {r2_train}")
print(f"Testing:mse: {mse_test}, rmse: {rmse_test}, mape: {mape_test}, r2: {r2_test}")



#A3
model.fit(feature_set_train, target_set_train)

target_set_train_pred_multi = model.predict(feature_set_train)
target_set_test_pred_multi = model.predict(feature_set_test)

mse_test = mean_squared_error(target_set_test, target_set_test_pred)
rmse_test = mse_test ** 0.5
mape_test = mean_absolute_percentage_error(target_set_test, target_set_test_pred)
r2_test = r2_score(target_set_test, target_set_test_pred)

# Corrected calculations using the predicted values
mse_test_multi = mean_squared_error(target_set_test, target_set_test_pred_multi)
rmse_test_multi = mse_test_multi ** 0.5
mape_test_multi = mean_absolute_percentage_error(target_set_test, target_set_test_pred_multi)
r2_test_multi = r2_score(target_set_test, target_set_test_pred_multi)

mse_train_multi = mean_squared_error(target_set_train, target_set_train_pred_multi)
rmse_train_multi = mse_train_multi ** 0.5
mape_train_multi = mean_absolute_percentage_error(target_set_train, target_set_train_pred_multi)
r2_train_multi = r2_score(target_set_train, target_set_train_pred_multi)

print(f"Training with many attributes:mse: {mse_train_multi}, rmse: {rmse_train_multi}, mape: {mape_train_multi}, r2: {r2_train_multi}")
print(f"Testing with many attributes:mse: {mse_test_multi}, rmse: {rmse_test_multi}, mape: {mape_test_multi}, r2: {r2_test_multi}")




#A4
kmeans = KMeans(n_clusters=2, random_state=42, n_init="auto").fit(feature_set_train)

lbl = kmeans.labels_
cntr = kmeans.cluster_centers_

print("Lable clusters:", lbl)
print("Centre clusters:", cntr)



#A5
sh_score = silhouette_score(feature_set_train, kmeans.labels_)
ch_score = calinski_harabasz_score(feature_set_train, kmeans.labels_)
db_score = davies_bouldin_score(feature_set_train, kmeans.labels_)

print(f"silhouette-Score: {sh_score}")
print(f"CH-score: {ch_score}")
print(f"DB-score: {db_score}")



#A6
k_values = range(2, 10)
sh_scores = []
ch_scores = []
db_scores = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init="auto").fit(feature_set_train)
    sh_scores.append(silhouette_score(feature_set_train, kmeans.labels_))
    ch_scores.append(calinski_harabasz_score(feature_set_train, kmeans.labels_))
    db_scores.append(davies_bouldin_score(feature_set_train, kmeans.labels_))

print("Silhouette Scores for multiple k values:", sh_scores)
print("Calinski-Harabasz Scores for multiple k values:", ch_scores)
print("Davies-Bouldin Scores for multiple k values:", db_scores)



#A7
distortions = []

for k in range(2, 20):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init="auto").fit(feature_set_train)
    distortions.append(kmeans.inertia_)

plt.plot(range(2, 20), distortions, marker='o')
plt.xlabel('no.of clusters')
plt.ylabel('Distortion')
plt.title('elbow plot for optimal k value')
plt.show()
