thyroid_data_withoutnan = thyroid_data[binary_cols].dropna()
binary_cols = ['FTI', 'T3', 'TSH']
vec1 = thyroid_data_withoutnan.iloc[0].values
vec2 = thyroid_data_withoutnan.iloc[1].values

f00 = np.sum((vec1 == 0)&(vec2 == 0))
f01 = np.sum((vec1 == 0)&(vec2 == 1))
f10 = np.sum((vec1 == 1)&(vec2 == 0))
f11 = np.sum((vec1 == 1)&(vec2 == 1))

JC = f11/(f01+f10+f11)
SMC = (f11+f00)/(f00+f01+f10+f11)

print("JC is: {:.4f}".format(JC))
print("SMC is: {:.4f}".format(SMC))
