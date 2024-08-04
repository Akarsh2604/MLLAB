import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt

file_path = r"C:\Users\akars\Desktop\jn\Lab Session Data.xlsx"
buy_data = pd.read_excel(file_path, sheet_name = 'IRCTC Stock Price')

data_of_price = buying_data.iloc[:, 3]
mean = statistics.mean(data_of_price)
var = statistics.variance(data_of_price)
print("Mean = ",mean)
print("Variance = ",var)

buy_data['Date'] = pd.to_datetime(buying_data['Date'])
wed = buy_data[buy_data['Date'].dt.day_name() == 'Wednesday']
mean_wed = statistics.mean(wed['Price'])
print(f"Wednesday mean: {mean_wed:.2f}")
print(f"Wednesday Comparison : {mean_wed - mean:.2f}")

apr_data = buy_data[buy_data['Date'].dt.month == 4]
mean_apr = statistics.mean(apr_data['Price'])
print(f"April data: {mean_apr: .2f}")
print(f"April comparison : {mean_apr - mean:.2f}")

chg = buy_data.iloc[:, 8]
loss_prob = np.mean(chg < 0)
print(f"Probability of Loss: {loss_prob:.2f}")

wed_prof = wed[chg < 0].shape[0]
total_wed = wed.shape[0]
prob_wed_prof = 1-(wed_prof/total_wed)
print(f"Probability ofProfit on Wednesday: {prob_wed_prof:.2f}")

prof_if_wed = prob_wed_prof
print(f"Profit if wednesday: {prof_if_wed}")

buy_data['Day of Week'] = buy_data['Date'].dt.day_name()
plt.figure(figsize=(10, 6))
plt.scatter(buying_data['Day of Week'], buying_data['Chg%'])
plt.title('Plot')
plt.xlabel('Day')
plt.ylabel('Chg%')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


