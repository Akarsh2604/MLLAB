import pandas as pd
import numpy as np
file_path = r"C:\Users\akars\Desktop\jn\Lab Session Data.xlsx"
buy_data = pd.read_excel(file_path, sheet_name = 'Purchase data')
matA = buy_data[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].dropna().values
matC = buy_data['Payment (Rs)'].dropna().values
dimension = matA.shape[1]
n_vec = matA.shape[0]
rank = np.linalg.matrix_rank(matA)
A_pseudo_inv = np.linalg.pinv(matA)
matX = A_pseudo_inv @ matC

print("Dimensionality = : ",dimension)
print("No of vectors = ",n_vec)
print("Rank of matA: ",rank)
print("Cost of products: :")
print(" - Candies: Rs: {:.2f}".format(matX[0]))
print(" - Mangoes: Rs: {:.2f}".format(matX[1]))
print(" - Milk Packets: Rs: {:.2f}".format(matX[2]))
