import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, r2_score

path_of_file = r"C:\Users\vvmad\Downloads\5th\ML\lab\Lab Session Data.xlsx"
xl = pd.ExcelFile(path_of_file)

price = pd.read_excel(xl, sheet_name = 'IRCTC Stock Price')
price['Predicted_Price'] = price['Price'].shift(1)
price = price.dropna()

realprice = price['Price'].values
assumedprice = price['Predicted_Price'].values

mse = mean_squared_error(realprice, assumedprice)
rmse = np.sqrt(mse)
mape = mean_absolute_percentage_error(realprice, assumedprice)
r2 = r2_score(realprice, assumedprice)

print("mse is:",mse)
print("rmse is:",rmse)
print("mape is:",mape)
print("r2 score is:",r2)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

path_of_file = r"C:\Users\vvmad\Downloads\5th\ML\HM7 - Java\java_cc_embed_data.csv"
proj_dataset = pd.read_csv(file_path)

feature1 = proj_dataset[['cc_embedding_1', 'cc_embedding_2']].values
feature2 = proj_dataset['Final_Marks'].values  

#A3
feature1_train = feature1[(feature1[:, 0] >= 1) & (feature1[:, 0] <= 10) & (feature1[:, 1] >= 1) & (feature1[:, 1] <= 10)]
feature2_train = y[(feature1[:, 0] >= 1) & (feature1[:, 0] <= 10) & (feature1[:, 1] >= 1) & (feature1[:, 1] <= 10)]

plt.scatter(feature1_train[feature2_train == 0][:, 0], feature1_train[feature2_train == 0][:, 1], color='blue', label='Class 0')
plt.scatter(feature1_train[feature2_train == 1][:, 0], feature1_train[feature2_train == 1][:, 1], color='red', label='Class 1')
plt.xlabel('cc_embedding_1')
plt.ylabel('cc_embedding_2')
plt.legend()
plt.title('Training Data')
plt.show()



#A4
feature1_test = np.array([[x, y] for x in np.arange(1, 10.1, 0.1) for y in np.arange(1, 10.1, 0.1)])
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(feature1_train, feature2_train)
feature2_test_pred = knn.predict(feature1_test)

plt.scatter(feature1_test[feature2_test_pred == 0][:, 0], feature1_test[feature2_test_pred == 0][:, 1], color='blue', label='Class 0')
plt.scatter(feature1_test[feature2_test_pred == 1][:, 0], feature1_test[feature2_test_pred == 1][:, 1], color='red', label='Class 1')
plt.xlabel('cc_embedding_1')
plt.ylabel('cc_embedding_2')
plt.legend()
plt.title('Test data for k=3')
plt.show()



#A5
for k in [1, 5, 7, 9]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(feature1_train, feature2_train)
    feature2_test_pred = knn.predict(feature1_test)

    plt.scatter(feature1_test[feature2_test_pred == 0][:, 0], feature1_test[feature2_test_pred == 0][:, 1], color='blue', label='Class 0')
    plt.scatter(feature1_test[feature2_test_pred == 1][:, 0], feature1_test[feature2_test_pred == 1][:, 1], color='red', label='Class 1')
    plt.xlabel('cc_embedding_1')
    plt.ylabel('cc_embedding_2')
    plt.legend()
    plt.title(f'Test Data for (k={k})')
    plt.show()



#A6
feature1_train = proj_dataset[['cc_embedding_3', 'cc_embedding_4']].values[:20]
feature2_train = proj_dataset['error_count'].values[:20]



#A7
param_grid = {'n_neighbors': np.arange(1, 21)}
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)
grid_search.fit(feature1_train, feature2_train)

best_k = grid_search.best_params_['n_neighbors']
print(f'Best k value found: {best_k}')

best_knn = KNeighborsClassifier(n_neighbors=best_k)
best_knn.fit(feature1_train, feature2_train)
project_feature2_test_pred = best_knn.predict(feature1_test)

plt.scatter(feature1_test[project_feature2_test_pred == 0][:, 0], feature1_test[project_feature2_test_pred == 0][:, 1], color='blue', label='Class 0')
plt.scatter(feature1_test[project_feature2_test_pred == 1][:, 0], feature1_test[project_feature2_test_pred == 1][:, 1], color='red', label='Class 1')
plt.xlabel('cc_embedding_1')
plt.ylabel('cc_embedding_2')
plt.legend()
plt.title(f'Test data for (best k={best_k})')
plt.show()
